for i in range(100):
    out = ''
    if not i % 3:
        out += 'Fizz'
    if not i % 5:
        out += 'Buzz'
    if not out:
        out = i
    print(out)