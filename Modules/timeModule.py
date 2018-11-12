def time_time():
    return time(NULL)

def time_sleep(a):
    start = clock()
    while (clock() - start) < (a * CLOCKS_PER_SEC):
        pass