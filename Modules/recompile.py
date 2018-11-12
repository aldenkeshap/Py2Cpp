from os import system
modules = 'random', 'time', 'math'

for module in modules:
    system(f'cd Py2C++ && python main.py Modules/{module}Module.py m')