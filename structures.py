from variables import *
from strings import *

def structure(text, variables): # FIX SOON NOT WORKING
    lines = text.split('\n')
    newLines = [' ' * (len(line) - len(line.lstrip())) for line in lines] # makes each line only the beginning whitespace
    lines = [line.lstrip() for line in lines] # makes each line all but the beginning whitespace
    # originalLines[n] == newLines[n] + lines[n] is ALWAYS true
    variableInitialize = ''
    modules = []
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
            if var in variables: # variable has been seen before
                if variables[var] == str:
                    newLine = f'{var} = str({val})'
                else:
                    newLine = line
            else:
                typ, val = varType(val, variables)
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
    text = '\n'.join(newLines)
    return text, variables, modules