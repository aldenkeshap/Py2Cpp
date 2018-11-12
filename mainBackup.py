from sys import argv
from ast import walk, parse, Str
from re import sub, match, search, split, findall, escape, MULTILINE
from itertools import chain
from os import system
from os.path import dirname, abspath
from json import dumps # for putting strings in double quotes
from math import ceil

replacements = {'and':'&&', 'or':'||', 'True':'true', 'False':'false', 'operator':'OPERATORREPLACEMENT',
                'pass':'', 'None':'NULL', '//':'/', 'bool':'toBool', 'int':'toInt'} 
simpeReplacements = {'//':'/'}
types = {int:'int', float:'float', str:'std::string', bool:'bool', tuple:'auto', None:'auto', 'double':'double',
         (tuple, int):'int %var[] = %val', (list, int):'std::vector<int>', (tuple, None):'int %var[] = %val',
         (list, None):'std::vector<int>'}

def getStrings(s):
    global it
    for it in walk(parse(s)):
        if isinstance(it, Str) and not it.s.startswith('STRINGREP'):
            yield it.s

def pos2Index(text, lineNo, colOffset):
    lines = text.split('\n')
    lineLen = [len(line) for line in lines]
    return sum(lineLen[0:lineNo-1]) + colOffset + lineNo - 1 # `lineNo - 1` counts newlines

def groupParens(line):
    stack = []
    parens = []
    for index, char in enumerate(line):
        if char in '([{': stack.append(index)
        elif char in ')]}':
            parens.append((stack.pop(), index))
    return parens
def varType(val):
    typ = None
    if match('^-?[0-9]+$', val):
        typ = int
    elif match('^-?[0-9.]+$', val):
        typ = float
    elif 'STRINGREP' in val:
        typ = str
    elif val in ('False', 'True'):
        typ = bool
    elif val.startswith('(') and val.endswith(')'):
        val = val.replace('(', '{').replace(')', '}')
        item = split(r'\s*,\s*', val[1:-1])[0]
        typ = (tuple, varType(item)[0])
        # print('TYP', typ, val, sep='#')
    elif val.startswith('[') and val.endswith(']'):
        val = val.replace('[', '{').replace(']', '}')
        item = split(r'\s*,\s*', val[1:-1])[0]
        typ = (list, varType(item)[0])
    elif val in variables:
        typ = variables[val]
    # if not typ: print('NONEFAIL', val)
    return typ, val
with open('base.cpp') as file:
        baseCode = file.read()
modules = []
with open(argv[1]) as file:
    text = file.read()
text = sub(r'\n\n+', '\n', text)
text = sub(r'\s*#.*', r'', text)
text += '\n'

defText = ''
for result in findall(r'def.+\n(?:    .+\n)+', text):
    defText += result + '\n'
    # print(4, result)
# print(repr(defText))
text = defText + 'SPLIT\n' + sub(r'def.+\n(?:    .+\n)+', r'', text)

fixed = list(text)
stop = False
number = 0
strings = {}
path = dirname(abspath(__file__))
while not stop: # fix strings
    stop = True
    for item in walk(parse(''.join(fixed))):
        if isinstance(item, Str):
            index = pos2Index(''.join(fixed), item.lineno, item.col_offset)
            strings[f'STRINGREP{number}'] = dumps(eval(''.join(fixed[index:index+len(repr(item.s))])))
            # print(5, ''.join(fixed[index:index+len(repr(item.s))]))
            del fixed[index:index+len(repr(item.s))]
            fixed.insert(index, list(f'STRINGREP{number}'))
            fixed = [item for sublist in fixed for item in sublist]
            stop = False
            number += 1
            break
text = ''.join(fixed)

for key, value in simpeReplacements.items():
    text = text.replace(key, value)
for key in replacements:
    # print('//' in text)
    ot = text
    if key.isalnum():
        start = key[0]
        bKey = fr'\b{escape(key)}\b'.replace(r'\b', r'([\[\](){}.;:\s<>/?\\|=+!@#$%^&*`~ -])')
        text = sub(bKey, fr'\1{escape(replacements[key])}\2', text)
        # print(bKey, fr'\1{escape(replacements[key])}\2', ot==text, sep=';;;;')
    else:
        bKey = fr'\b{key}\b'.replace(r'\b', r'([\[\](){}.;:\s<>/?\\|=+!@#$%^&*`~-])')
        # print(23, bKey)
        text = sub(bKey, fr'\1{replacements[key]}\2', text)
# print(text)
lines = text.split('\n')
newLines = [' ' * (len(line) - len(line.lstrip())) for line in lines]
lines = [line.lstrip() for line in lines]
variables = {}
variableInitialize = ''
# print('HI', repr(text))
for index, line in enumerate(lines): # setup control blocks
    newLine = ''
    if line.startswith('if'):
        newLine = f'if ({line[3:-1]})'
    elif line.startswith('elif'):
        newLine = f'else if ({line[5:-1]})'
    elif line.startswith('else'):
        newLine = 'else'
    elif line.startswith('while'):
        newLine = f'while ({line[6:-1]})'
    elif line.startswith('def'):
        name = line[4:].split('(')[0]
        localVars = split(r',\s*', ''.join(line[:-1].split('(')[1:])[:-1])
        # print(56, name, localVars)
        if localVars[0]: localVars = ', '.join([f'auto {var}' for var in localVars])
        else: localVars = ''
        # print('DEFLV', localVars)
        newLine = f'auto {name}({localVars})'
    elif line.startswith('for'):
        line = line[4:-1]
        var, val = line.split(' in ')
        newLine = f'for (auto {var} : {val})'
    elif line.startswith('import'):
        newLine = ''
        modules.append(line[7:])
    elif line.startswith('assert'):
        newLine = f'assert ({line[7:]})'
    elif search(r'[^=+*/-]=[^=]', line):
        var, val = split(r'(?:[^=+*/-])=(?:[^=])', line)
        typ = None
        if var in variables: # variable has been initialized
            if variables[var] == str:
                newLine = f'{var} = str({val})'
            else:
                newLine = line
        else:
            typ, val = varType(val)
            # print('109!!', line, var, val, typ, sep='|')
            if '%' in types[typ]:
                newLine = types[typ].replace('%val', val).replace('%var', var)
            else:
                newLine = f'{types[typ]} {var} = {val}'
            variables[var] = typ
            # print('#119', typ, newLine)
    elif search(r'[+*/-]=|//=', line):
        op = findall(r'[+*/-]=|//=', line)[0]
        # print(op)
        try: var, val = split(r'\s*(?://=|[+*/-]=)\s*', line)
        except: print(line, split(r'\s*(?://=|[+*/-]=)\s*', line), sep='@'); 1/0
        if variables[var] == str:
            newLine = f'{var} {op} str({val})'
        else:
            newLine = line
    else:
        newLine = line
    if 'not' in newLine:
        for _ in range(newLine.count('not')):
            notIndex = newLine.index('not')
            parens = groupParens(newLine)
            parens = [paren for paren in parens if (paren[0] < notIndex < paren[1])]
            parens = sorted(parens, key=lambda p: p[1] - p[0])
            newLine = list(newLine)
            newLine.insert(notIndex+4, '(')
            newLine.insert(parens[0][1]+1, ')')
            newLine = ''.join(newLine)
            newLine = newLine.replace('not', '!', 1).replace('! ', '!')
    # print('^&^&', newLine)
    newLines[index] += newLine
lines = '\n'.join(newLines)
lines = lines.split('\n')
newLines = []
lastIndent = 0
# print(repr(text))
# print(lines)
# print(lines)

for module in modules:
    # print(module)
    with open(f'Modules/{module}Module.cpp') as file:
        baseCode += file.read()
for index, line in enumerate(lines): # add braces
    newLine = line
    indent = match(r'\s+', line)
    if index:
        # print(index, indent, line)
        if 'SPLIT' in line:
            newLines.append(line)
            continue
        elif not indent: indent = 0
        else: indent = indent.end()
        if lastIndent < 0: pass
        elif indent > lastIndent:
            newLine = '{' + newLine
        elif indent < lastIndent:
            # print(line, ceil((lastIndent - indent) / 4))
            newLine = ('}' * ceil((lastIndent - indent) / 4) + '\n' + newLine)
        # print(index, newLine, indent)
    else: indent = 0
    lastIndent = indent
    newLines.append(newLine)
# breakpoint()
# print(newLines)

text = '\n'.join(newLines)
text = sub(r'\n{', r' {\n', text)
text = sub(r'([a-zA-Z])\.([a-zA-Z])', r'\1_\2', text)
# print(text)
# text = sub(r'}(\s+)', r'\1}\n\1', text)
text = sub(r'}(\s+.+)', r'}\n\1', text)

newLines = []
for index, line in enumerate(text.split('\n')):
    bracket = line.endswith('}') or line.endswith('{') or line.startswith('}') or line.startswith('{')
    empty = match(r'\s*$', line)
    comment = line.lstrip().startswith('//')
    equals = search(r'[^=]=[^=]', line)
    if not comment and not empty and (not bracket or equals) and 'SPLIT' not in line:
        newLines.append(line + ';')
    else:
        newLines.append(line)
    # print()
text = '\n'.join(newLines)
for key, val in strings.items():
    text = text.replace(key, val)
for var in variables:
    if variables[var] == str:
        text = sub(rf'!\s+{var}', rf'{var}.empty()', text)
        text = sub(rf'!\s*\(\s*{var}\s*(\)|&&|\|\|)', rf'({var}.empty() \1', text)
# if 'math' in argv[1]: print(text)
if len(argv) > 2 and argv[-1].startswith('m'): # module
    if 'SPLIT' in text: # some function definitions
        defText, text = text.split('SPLIT')
        text = f'{text}\n//SPLT@@@\\n{defText}\n'
    # else the code is done
else: # normal code
    # print('SPLIT' in text, repr(text))
    if 'SPLIT' in text: # some function definitions
        # print('SPLIT!!')
        defText, text = text.split('SPLIT')
        text = f'{baseCode}{defText}\n//SPLT@@@\nint main() {{\n{text}\n}}'
    else: # no function definitions
        text = f'{baseCode}int main() {{{text}}}'
with open(f'{argv[1][:-3]}.cpp', 'w') as file:
    file.write(text)
if len(argv) > 2 and argv[-1].startswith('r'): # run code immediatly
    system(f'cd Py2C++ && g++ -std=c++17 {path}\\{argv[1][:-3]}.cpp && .\\a.exe')
if len(argv) > 2 and argv[-1].startswith('c'): # run code immediatly
    system(f'cd Py2C++ && g++ -std=c++17 {path}\\{argv[1][:-3]}.cpp')

# system('.\\a.exe')