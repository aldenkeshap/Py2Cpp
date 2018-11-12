from sys import argv
from re import sub, match, search, split, findall
from os import system
from os.path import dirname, abspath
from math import ceil

from strings import *
# from variables import *
from replacements import *
from structures import *

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

text = defText + 'SPLIT\n' + sub(r'def.+\n(?:    .+\n)+', r'', text)

path = dirname(abspath(__file__))

text, strings = replaceStrings(text)

text = simpleReplace(text)

text = replace(text)

variables = {}

text, variables, modules = structure(text, variables)

text = replaceMethodCalls(text, variables, modules)

lines = text.split('\n')
newLines = []
lastIndent = 0

for module in modules:
    with open(f'Modules/{module}Module.cpp') as file:
        baseCode += file.read()
        
for index, line in enumerate(lines): # add braces
    newLine = line
    indent = match(r'\s+', line)
    if index:
        if 'SPLIT' in line:
            newLines.append(line)
            continue
        elif not indent: indent = 0
        else: indent = indent.end()
        if lastIndent < 0: pass
        elif indent > lastIndent:
            newLine = '{' + newLine
        elif indent < lastIndent:
            newLine = ('}' * ceil((lastIndent - indent) / 4) + '\n' + newLine)
    else: indent = 0
    lastIndent = indent
    newLines.append(newLine)

text = '\n'.join(newLines)
text = sub(r'\n{', r' {\n', text)
text = sub(r'([a-zA-Z])\.([a-zA-Z])', r'\1_\2', text)
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
text = '\n'.join(newLines)
for key, val in strings.items():
    text = text.replace(key, val)
for var in variables:
    if variables[var] == str:
        text = sub(rf'!\s+{var}', rf'{var}.empty()', text)
        text = sub(rf'!\s*\(\s*{var}\s*(\)|&&|\|\|)', rf'({var}.empty() \1', text)

if len(argv) > 2 and argv[-1].startswith('m'): # module
    if 'SPLIT' in text: # some function definitions
        defText, text = text.split('SPLIT')
        text = f'{text}\n//SPLT@@@\\n{defText}\n'
    # else the code is done
else: # normal code
    if 'SPLIT' in text: # some function definitions
        defText, text = text.split('SPLIT')
        text = f'{baseCode}{defText}\n//SPLT@@@\nint main() {{\n{text}\n}}'
    else: # no function definitions
        text = f'{baseCode}int main() {{{text}}}'
with open(f'{argv[1][:-3]}.cpp', 'w') as file:
    file.write(text)
if len(argv) > 2 and argv[-1].startswith('r'): # run code immediatly
    system(f'clang -std=c++1z {path}/{argv[1][:-3]}.cpp && .\\a.exe')
if len(argv) > 2 and argv[-1].startswith('c'): # run code immediatly
    system(f'clang -std=c++1z {path}/{argv[1][:-3]}.cpp')

# system('.\\a.exe')