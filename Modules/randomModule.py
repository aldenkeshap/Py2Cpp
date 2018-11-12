def random_randint(a, b):
    return rand() % (b - a) + a

def random_choice(seq):
    index = 0
    index = random_randint(0, len(seq))
    return seq[index]

def random_randrange(stop):
    return random_choice(range(stop))

def random_randrange(start, stop):
    return random_choice(range(start, stop))

def random_randrange(start, stop, step):
    return random_choice(range(start, stop, step))

def random_random():
    return (rand() * 1.0) / (RAND_MAX)

def random_seed():
    srand(time(NULL))

def random_seed(a):
    srand(a)