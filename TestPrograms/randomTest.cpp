#include <iostream>
#include <string>
#include <vector>
#include <time.h>

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

auto len(int a[]) {
    // std::vector<int> v(std::begin(a), std::end(a));
    std::cout << *(a + 1) - *a << std::endl;
}
auto len(std::vector<int> a) {
    return a.size();
}auto random_randint(auto a, auto b) {
    return rand() % (b - a) + a;
}

auto random_choice(auto seq) {
    int index = 0;
    index = random_randint(0, len(seq));
    return seq[index];
}

auto random_randrange(auto stop) {
    return random_choice(range(stop));
}

auto random_randrange(auto start, auto stop) {
    return random_choice(range(start, stop));
}

auto random_randrange(auto start, auto stop, auto step) {
    return random_choice(range(start, stop, step));
}

auto random_random() {
    return (rand() * 1.0) / (RAND_MAX);
}

auto seed() {
    srand(time(NULL));
}

auto seed(auto a) {
    srand(a);
}
//SPLT@@@
int main() {


seed();
print(random_random());

}