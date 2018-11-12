math_e = 2.718281828459045
math_pi = 3.141592653589793
math_tau = 6.283185307179586


def math_ceil(x):
    return ceil(x)

def math_copysign(x, y):
    return copysign(x, y)

def math_fabs(x):
    return abs(x)

def math_factorial(x):
    if x == 1:
        return 1
    return x * math_factorial(x - 1)

def math_floor(x):
    return floor(x)

def math_gcd(x, y):
    if not y:
        return x
    else:
        return math_gcd(y, x%y)

def math_exp(x):
    return math_pow(math_e, x)

def math_log(x):
    return log(x)

def math_log(x, b):
    return log(x) / log(b)

def math_pow(x, y):
    return pow(x, y)

def math_sqrt(x):
    return pow(x, 0.5)

def math_acos(x):
    return acos(x)

def math_asin(x):
    return asin(x)

def math_atan(x):
    return atan(x)

def math_atan2(x, y):
    return atan2(y, x)

def math_cos(x):
    return cos(x)

def math_dist(p, q):
    return sqrt(pow(p[0] - q[0], 2) + pow(p[1] - q[2], 2))

def math_hypot(x):
    return hypot(x)

def math_sin(x):
    return sin(x)

def math_tan(x):
    return tan(x)

def math_degrees(x):
    return x * math_pi / 180

def math_radians(x):
    return x * 180 / math_pi

def math_acosh(x):
    return acosh(x)

def math_asinh(x):
    return asinh(x)

def math_atanh(x):
    return atanh(x)

def math_cosh(x):
    return cosh(x)

def math_sinh(x):
    return sinh(x)

def math_tanh(x):
    return tanh(x)

def math_gamma(x):
    return tgamma(x)

def math_lgammma(x):
    return lgammma(x)

#end of file
