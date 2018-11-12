
auto time_time() {
    return time(NULL);
}auto time_sleep(auto a) {
    auto start = clock();
    while ((clock() - start) < (a * CLOCKS_PER_SEC)) {
        ;
}}
//SPLT@@@\n
