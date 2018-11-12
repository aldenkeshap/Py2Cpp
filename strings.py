from ast import walk, parse, Str
from json import dumps # for putting strings in double quotes
from re import sub

def getStrings(s):
    global it
    for it in walk(parse(s)):
        if isinstance(it, Str) and not it.s.startswith('STRINGREP'):
            yield it.s

def pos2Index(text, lineNo, colOffset):
    lines = text.split('\n')
    lineLen = [len(line) for line in lines]
    return sum(lineLen[0:lineNo-1]) + colOffset + lineNo - 1 # `lineNo - 1` includes newlines

def groupParens(line):
    stack = []
    parens = []
    for index, char in enumerate(line):
        if char in '([{': stack.append(index)
        elif char in ')]}':
            parens.append((stack.pop(), index))
    return parens

def replaceStrings(text):
    fixed = list(text)
    stop = False
    strings = {}
    number = 0
    while not stop: # fix strings
        stop = True
        for item in walk(parse(''.join(fixed))):
            if isinstance(item, Str):
                index = pos2Index(''.join(fixed), item.lineno, item.col_offset)
                strings[f'STRINGREP{number}'] = dumps(eval(''.join(fixed[index:index+len(repr(item.s))])))
                del fixed[index:index+len(repr(item.s))]
                fixed.insert(index, list(f'STRINGREP{number}'))
                fixed = [item for sublist in fixed for item in sublist]
                stop = False
                number += 1
                break
    text = ''.join(fixed)
    return text, strings