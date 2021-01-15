#include <iostream>
#include <algorithm>
#include <vector>
#include <list>

#define BIT_COUNT 31

const int* x0 = new int[BIT_COUNT] {1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1};

int next_permutation(const int N, int *P) {
    int s;
    int *first = &P[0];
    int *last = &P[N - 1];
    int *k = last - 1;
    int *l = last;
    //find larges k so that P[k]<P[k+1]
    while (k > first) {
        if (*k < *(k + 1)) {
            break;
        }
        k--;
    }
    //if no P[k]<P[k+1], P is the last permutation in lexicographic order
    if (*k > *(k + 1)) {
        return 0;
    }
    //find largest l so that P[k]<P[l]
    while (l > k) {
        if (*l > *k) {
            break;
        }
        l--;
    }
    //swap P[l] and P[k]
    s = *k;
    *k = *l;
    *l = s;
    //reverse the remaining P[k+1]...P[N-1]
    first = k + 1;
    while (first < last) {
        s = *first;
        *first = *last;
        *last = s;

        first++;
        last--;
    }

    return 1;
}

double opt_function(int* x) {
    int opt_result = 0;

    for (int shift = 0; shift < BIT_COUNT; ++shift) {
        int cross_correlation_same_index = 0;
        int cross_correlation_diff_index = 0;
        int auto_correlation_same_index = 0;
        int auto_correlation_diff_index = 0;

        for (int i = 0; i < BIT_COUNT; ++i) {
            if (x0[(i + BIT_COUNT - shift) % BIT_COUNT] == x[i]) {
                cross_correlation_same_index++;
            } else {
                cross_correlation_diff_index++;
            }

            if (i >= 1) {
                if (x[(i + BIT_COUNT - shift) % BIT_COUNT] == x[i]) {
                    auto_correlation_same_index++;
                } else {
                    auto_correlation_diff_index++;
                }
            }
        }
        int cross = cross_correlation_same_index - cross_correlation_diff_index;
        int auto_cor = auto_correlation_same_index - auto_correlation_diff_index;
        if (cross >= 6 || cross <= -4) {
            if (cross >= 6) {
                opt_result += cross - 5;
            } else {
                opt_result += -3 - cross;
            }
        }
        if (auto_cor >= 12 || auto_cor <= -18) {
            if (auto_cor >= 12) {
                opt_result += auto_cor - 11;
            } else {
                opt_result += -17 - auto_cor;
            }
        }
    }
    return opt_result;
}

int main() {
    int* ones_15 = new int[15];
    int* ones_16= new int[16];
    std::vector<int*> results;
    for (int i = 0; i < 16; ++i) {
        ones_16[i] = i;
        if (i < 15) {
            ones_15[i] = i;
        }
    }
    std::cout << "Begin 15..." << std::endl;
    do {
        int* array = new int[BIT_COUNT];
        for (int i = 0; i < 15; ++i) {
            array[ones_15[i]] = 1;
        }
        if (opt_function(array) == 0) {
            std::cout << "Found!" << std::endl;
            int val = 0;
            for (int i = 0; i < BIT_COUNT; ++i) {
                std::cout << array[i]<< ", ";
                val += val*2 + array[i];
            }
            std::cout << "\n" << "Decimal: " << val << std::endl;
        }
    } while (next_permutation(15, ones_15));
    std::cout << "End 15..." << std::endl;
    std::cout << "Begin 16..." << std::endl;
    do {
        int* array = new int[BIT_COUNT];
        for (int i = 0; i < 16; ++i) {
            array[ones_16[i]] = 1;
        }
        if (opt_function(array) == 0) {
            std::cout << "Found!" << std::endl;
            results.emplace_back(array);
        }
    } while (next_permutation(16, ones_16));
    std::cout << "End 15..." << std::endl;
    return 0;
}
