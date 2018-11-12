#include <iostream>
#include <string>
#include <vector>
#include <time.h>
#include <math.h>
#include <assert.h>
#include <sstream>

template <typename T>
void print(T t) {
    std::cout << t << std::endl;
}
template<typename T, typename... Args>
void print(T t, Args... args) {
    std::cout << t << " ";
    print(args...);
}

std::string str(int val) {
    return std::to_string(val);
}
std::string str(std::string val) {
    return val;
}
std::string str(std::stringstream val) {
    std::string result(val.str());
    return result;
}

std::vector<int> range(int end) {
    std::vector<int> result;
    for (int i=0; i<end; i++) {
        result.push_back(i);
    }
    return result;
}
std::vector<int> range(int start, int end) {
    std::vector<int> result;
    for (int i=0; i<end-start; i++) {
        result.push_back(i+start);
    }
    return result;
}
std::vector<int> range(int start, int end, int step) {
    std::vector<int> result;
    for (int i=0; i<(end-start)/step; i++) {
        result.push_back(i*step + start);
    }
    return result;
}

template <typename T>
std::string input(T t) {
    std::string result;
    std::cout << t;
    std::cin >> result;
    return result;
}
std::string input() {
    std::string result;
    std::cin >> result;
    return result;
}

auto len(int a[]) {
    // std::vector<int> v(std::begin(a), std::end(a));
    std::cout << *(a + 1) - *a << std::endl;
}
auto len(std::vector<int> a) {
    return a.size();
}
auto len(std::string s) {
    return s.length();
}

auto toBool(std::vector<int> v) {
    return !!len(v);
}
auto toBool(int i) {
    return !!i;
}
auto toBool(std::string s) {
    return s.empty();
}

auto toInt(int i) {
    // std::cout << "toInt(int) " << i << std::endl;
    return i;
}
auto toInt(std::string s) {
    // std::cout << "toInt(string) " << s << std::endl;
    return std::stol(s, nullptr);
}
auto toInt(std::string s, int base) {
    // std::cout << "toInt(string, int) " << s << " " << base << std::endl;
    return std::stol(s, nullptr, base);
}

std::string bin(int n) {
    std::string r;
    bool neg = n < 0;
    n = abs(n);
    while (n!=0) {
        r = str(n % 2) + r;
        n /= 2;
    }
    r = "0b" + r;
    if (neg) {
        r = "-" + r;
    }
    return r;
}

std::string hex(int n) {
    std::stringstream stream;
    stream << std::hex << n;
    std::string s(stream.str());
    return "0x" + s;
}

std::string oct(int n) {
    std::stringstream stream;
    stream << std::oct << n;
    std::string s(stream.str());
    return "0o" + s;
}
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

//SPLT@@@
int main() {


float total = 0.0;
int end = 5;
end = pow(10, end);
auto piSquared = pow(math_pi, 2);
for (auto i : range(1, end + 1)) {
    total += 1 / (piSquared * pow(i, 2) + 1);
}

print(total);
total = 1 / total;
total += 1;
total = math_sqrt(total);
print(total);
print(abs(total - math_e)) ;
print("Hello");

}