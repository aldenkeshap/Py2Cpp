
auto random_randint(auto a, auto b) {
    return rand() % (b - a) + a;
}auto random_choice(auto seq) {
    int index = 0;
    index = random_randint(0, len(seq));
    return seq[index];
}auto random_randrange(auto stop) {
    return random_choice(range(stop));
}auto random_randrange(auto start, auto stop) {
    return random_choice(range(start, stop));
}auto random_randrange(auto start, auto stop, auto step) {
    return random_choice(range(start, stop, step));
}auto random_random() {
    return (rand() * 1.0) / (RAND_MAX);
}auto random_seed() {
    srand(time(NULL));
}auto random_seed(auto a) {
    srand(a);
}
//SPLT@@@\n
