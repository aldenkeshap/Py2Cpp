
auto math_e = 2.718281828459045;
auto math_pi = 3.141592653589793;
auto math_tau = 6.283185307179586;
auto math_ceil(auto x) {
    return ceil(x);
}auto math_copysign(auto x, auto y) {
    return copysign(x, y);
}auto math_fabs(auto x) {
    return abs(x);
}auto math_factorial(auto x) {
    if (x == 1) {
        return 1;
}
    return x * math_factorial(x - 1);
}auto math_floor(auto x) {
    return floor(x);
}auto math_gcd(auto x, auto y) {
    if (!(y)) {
        return x;
}
    else {
        return math_gcd(y, x%y);
}}auto math_exp(auto x) {
    return math_pow(math_e, x);
}auto math_log(auto x) {
    return log(x);
}auto math_log(auto x, auto b) {
    return log(x) / log(b);
}auto math_pow(auto x, auto y) {
    return pow(x, y);
}auto math_sqrt(auto x) {
    return pow(x, 0.5);
}auto math_acos(auto x) {
    return acos(x);
}auto math_asin(auto x) {
    return asin(x);
}auto math_atan(auto x) {
    return atan(x);
}auto math_atan2(auto x, auto y) {
    return atan2(y, x);
}auto math_cos(auto x) {
    return cos(x);
}auto math_dist(auto p, auto q) {
    return sqrt(pow(p[0] - q[0], 2) + pow(p[1] - q[2], 2));
}auto math_hypot(auto x) {
    return hypot(x);
}auto math_sin(auto x) {
    return sin(x);
}auto math_tan(auto x) {
    return tan(x);
}auto math_degrees(auto x) {
    return x * math_pi / 180;
}auto math_radians(auto x) {
    return x * 180 / math_pi;
}auto math_acosh(auto x) {
    return acosh(x);
}auto math_asinh(auto x) {
    return asinh(x);
}auto math_atanh(auto x) {
    return atanh(x);
}auto math_cosh(auto x) {
    return cosh(x);
}auto math_sinh(auto x) {
    return sinh(x);
}auto math_tanh(auto x) {
    return tanh(x);
}auto math_gamma(auto x) {
    return tgamma(x);
}auto math_lgammma(auto x) {
    return lgammma(x);
}

//SPLT@@@\n
