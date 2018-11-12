def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)
#FAKE
i = 0
while i < 10:
    print(fib(i))
    i += 1