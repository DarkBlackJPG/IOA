#include <iostream>
#include <algorithm>
#include <vector>
#include <chrono>
#include <list>

#define BIT_COUNT 31

const int* x0 = new int[BIT_COUNT] {1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1};
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
            }
            else {
                cross_correlation_diff_index++;
            }

            if (shift >= 1) {
                if (x[(i + BIT_COUNT - shift) % BIT_COUNT] == x[i]) {
                    auto_correlation_same_index++;
                }
                else {
                    auto_correlation_diff_index++;
                }
            }
        }
        int cross = cross_correlation_same_index - cross_correlation_diff_index;
        int auto_cor = auto_correlation_same_index - auto_correlation_diff_index;
        if (cross >= 6 || cross <= -4) {
            if (cross >= 6) {
                opt_result += cross - 5;
                break;
            }
            else {
                opt_result += -3 - cross;
                break;
            }
        }
        if (auto_cor >= 12 || auto_cor <= -18) {
            if (auto_cor >= 12) {
                opt_result += auto_cor - 11;
                break;
            }
            else {
                opt_result += -17 - auto_cor;
                break;
            }
        }
    }
    return opt_result;
}

int main() {
    int k = 15;
    int n = 31;
    int i, j;
    bool b;
    int* P = new int[k];

    for (i = 0; i < k; i++)
        P[i] = i + 1;
    do {
        int* ones = new int[BIT_COUNT] {
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        };
        int* zeroes = new int[BIT_COUNT] {
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1
        };
        for (int i = 0; i < 15; i++){
            ones[P[i] - 1] = 1;
            zeroes[P[i] - 1] = 0;
        }
        if (opt_function(ones) == 0) {
            std::cout << std::endl;
            unsigned long long val = 0;
            for (int i = 0; i < BIT_COUNT; i++)
            {
                std::cout << ones[i] << " ";
                val += val * 2 + ones[i];
            }
            std::cout << std::endl;
            std::cout << "Decimal: " << val <<std::endl;
        }
        if (opt_function(zeroes) == 0) {
            std::cout << std::endl;
            unsigned long long val = 0;
            for (int i = 0; i < BIT_COUNT; i++)
            {
                std::cout << zeroes[i] << " ";
                val += val * 2 + zeroes[i];
            }
            std::cout << std::endl;
            std::cout << "Decimal: " << val <<std::endl;
        }
        delete[] ones;
        delete[] zeroes;
        b = false;
        for (i = k - 1; i >= 0; i--) {
            if (P[i] < n - k + 1 + i) {
                P[i]++;
                for (j = i + 1; j < k; j++) {
                    P[j] = P[j - 1] + 1;
                }

                b = true;
                break;
            }
        }
    } while (b);

    if (P != NULL)
        delete[] P;
    return 0;
}
