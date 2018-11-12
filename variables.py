from re import *

types = {int:'int', float:'float', str:'std::string', bool:'bool', tuple:'auto', None:'auto', 'double':'double',
         (tuple, int):'int %var[] = %val', (list, int):'std::vector<int>', (tuple, None):'int %var[] = %val',
         (list, None):'std::vector<int>'}

def varType(val, variables):
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