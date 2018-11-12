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
//SPLT@@@
int main() {

std::string a = input("A: ");
print(a);

}