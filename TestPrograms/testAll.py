from subprocess import check_output
from os import listdir

files = listdir('TestPrograms/')
files.remove('testAll.py')
files = [file for file in files if file.endswith('.py')]
skipWords = 'random', 'input', 'pi'
failed = skipped = succeeded = 0
for file in files:
    if any([(word in file.lower()) for word in skipWords]):
        print(f'{file} skipped.')
        skipped += 1
        continue
    python = check_output(f'python TestPrograms/{file}')
    cpp = check_output(f'python main.py TestPrograms/{file} r')
    if cpp == python:
        print(f'{file} succeeded.')
        succeeded += 1
    else:
        print(f'{file} failed.')
        failed += 1

print(f'Total, {failed} failed, {succeeded} succeeded and {skipped} skipped.')