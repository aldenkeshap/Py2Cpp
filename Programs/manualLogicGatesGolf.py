def op(a, b, operator):
    if operator == 0: # multiplication
        return a * b
    elif operator == 1: # floor division
        return a // b
    elif operator == 2: # right shift
        return a >> b
    elif operator == 3: # left shift
        return a << b
    elif operator == 4: # modulo
        return a % b
    elif operator == 5: # bitwise xor
        return a ^ b
    elif operator == 6: # bitwise and
        return a & b
    elif operator == 7: # bitwise or
        return a | b

a = 2
keys = (371, 372, 373, 321, 322, 323, 449, 450, 451, 409, 410, 411, 487, 488, 489, 399, 400, 401)
vals = (0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0)
code = 0
fail = False
while a < 100:
    b = 2
    a += 1
    print(a)
    while b < 100:
        c = 2
        b += 1
        # print(a, b)
        while c < 100:
            d = 2
            c += 1
            while d < 100:
                ops = -1
                d += 1
                while ops < 4096:
                    ops += 1
                    index = -1
                    fail = False
                    while index < 18:
                        opCode = ops
                        index += 1
                        code = keys[index]
                        code = op(code, a, opCode % 8)
                        opCode //= 8
                        code = op(code, b, opCode % 8)
                        opCode //= 8
                        code = op(code, c, opCode % 8)
                        opCode //= 8
                        code = op(code, d, opCode % 8)
                        code = code % 2
                        if vals[index] != code:
                            fail = True
                            index = 20
                    if not fail:
                        print('END!', a, b, c, d, ops)
