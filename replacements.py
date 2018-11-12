from re import escape, sub

replacements = {'and':'&&', 'or':'||', 'True':'true', 'False':'false', 'operator':'OPERATORREPLACEMENT',
                'pass':'', 'None':'NULL', '//':'/', 'bool':'toBool', 'int':'toInt'} 

simpeReplacements = {'//':'/'}

def simpleReplace(text):
    for key, value in simpeReplacements.items():
        text = text.replace(key, value)
    return text

def replace(text):
    for key in replacements:
        ot = text
        if key.isalnum():
            start = key[0]
            bKey = fr'\b{escape(key)}\b'.replace(r'\b', r'([\[\](){}.;:\s<>/?\\|=+!@#$%^&*`~ -])')
            text = sub(bKey, fr'\1{escape(replacements[key])}\2', text)
        else:
            bKey = fr'\b{key}\b'.replace(r'\b', r'([\[\](){}.;:\s<>/?\\|=+!@#$%^&*`~-])')
            text = sub(bKey, fr'\1{replacements[key]}\2', text)

    return text

def replaceMethodCalls(text, variables, modules):
    text = sub(r"(STRINGREP[0-9]+)\.(\w+)\((\w+?)\)", r"METHOD_\2(\1, \3)", text)
    text = sub(r"(STRINGREP[0-9]+)\.(\w+)\(\)", r"METHOD_\2(\1)", text)
    for key in variables.keys():
        text = sub(rf"{key}\.(\w+)\((\w+)\)", rf"METHOD_\1({key}, \2)", text)
        text = sub(rf"{key}\.(\w+)\(\)", rf"METHOD_\1({key})", text)
    return text