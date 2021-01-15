#include <iostream>
#include <vector>
#include <limits>

#define PRINT(x,y) for(int i = 0; i < x; i++) { std::cout << y[i] << ", ";} \ std::cout<<std::endl;

int matrix[10][10] = {
    { 0,    374  ,200,  223,  108 , 178,  252,  285 , 240 , 356},
    { 374,  0    ,255,  166,  433 , 199,  135,  95  , 136 , 17},
    { 200,  255  ,0  ,  128,  277 , 821,  180,  160 , 131 , 247},
    { 223,  166  ,128,  0  ,  430 , 47 ,  52 ,  84  , 40  , 155},
    { 108,  433  ,277,  430,  0   , 453,  478,  344 , 389 , 423},
    { 178,  199  ,821,  47 ,  453 , 0  ,  91 ,  110 , 64  , 181},
    { 252,  135  ,180,  52 ,  478 , 91 ,  0  ,  114 , 83  , 117},
    { 285,  95  , 160,  84 ,  344 , 110,  114,  0   , 47  , 78},
    { 240,  136,  131,  40 ,  389 , 64 ,  83 ,  47 ,  0   , 118},
    { 356,  17,   247,  155,  423 , 181,  117,  78,   118 , 0}
};


int main(int argc, char** argv)
{
    constexpr int n = 10;
    constexpr int k = 8;
    int min_cost = INT_MAX;
    int* Tres = new int[2 * (k + 1)];
    std::cout << "Begin execution" << std::endl;
    int q;

    int P[k];
    for (int i = 0; i < k; i++)
        P[i] = 1;
    unsigned long long a = 0;
    do {
        int inc = 0;
        int* V = new int[n];
        int* VV = new int[n];
        int* T = new int[2 * (k + 1)];
        for (int i = 0; i < n; i++) {
            V[i] = 0;
            VV[i] = 0;
        }

        for (int i = 0; i < k; i++) {
            V[P[i] - 1] += 1;
        }

        for (int i = 0; i < k; i++) {
            for (int j = 0; j < n; j++) {
                if (V[j] == 0) {
                    V[j] = -1;
                    T[inc++] = j + 1;
                    T[inc++] = P[i];

                    V[P[i] - 1]--;
                    break;
                }
            }
        }

        int j = 0;
        for (int i = 0; i < n; i++) {
            if (V[i] == 0 && j == 0) {
                T[inc++] = i + 1;
               
                j++;
            }
            else if (V[i] == 0 && j == 1) {
                T[inc++] = i + 1;
               
                break;
            }
        }
        delete[] V;
        int cost = 0;
        for (int i = 0; i < 2 * k + 1; i += 2) {
            VV[T[i] - 1] ++;
            VV[T[i + 1] - 1] ++;

        }
        for (int i = 0;i < 2 * k + 1; i+=2) {
            if (VV[T[i] - 1] >= 4) {
                cost += matrix[T[i] - 1][T[i + 1] - 1] + 100 * (VV[T[i] - 1] * 3);
            } else if (VV[T[i + 1] - 1] >= 4) {
                cost += matrix[T[i] - 1][T[i + 1] - 1] + 100 * (VV[T[i + 1] - 1] * 3);
            }
            else {
                cost += matrix[T[i] - 1][T[i + 1] - 1];
            }

        }
        if (min_cost > cost) {
            min_cost = cost;
            for (int i = 0; i < 2 * (k + 1); i++)
                Tres[i] = T[i];
        }

        delete[] VV;
        delete[] T;

        q = k - 1;
        while (q >= 0) {
            P[q]++;
            if (P[q] > n) {
                P[q] = 1;
                q--;
            }
            else break;
        }
    } while (q >= 0);
    std::cout << min_cost << std::endl;
    for (int i = 0; i < 2 * k + 2; i++) {
        std::cout << " " << Tres[i];
        if ((i + 1) % 2 == 0 && i < 2 * k)
            std::cout << " - ";
    }
    std::cout << "\nEnd execution" << std::endl;
}
