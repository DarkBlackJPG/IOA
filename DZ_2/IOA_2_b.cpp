//
//  main.cpp
//  IOA_2
//
//  Created by Stefan Teslic on 16/10/2020.
//

#include <iostream>
#include <math.h>
#include <algorithm>
#include <limits>
#include <time.h>

constexpr auto HOLE_COUNT = 12;
const double positions[18][2] = {
        {62.0, 58.4}, // 1
        {57.5, 56.0}, // 2
        {51.7, 56.0}, // 3
        {67.9, 19.6}, // 4
        {57.7, 42.1}, // 5
        {54.2, 29.1}, // 6
        {46., 45.1},  // 7
        {34.7, 45.1}, // 8
        {45.7, 25.1}, // 9
        {34.7, 26.4}, // 10
        {28.4, 31.7}, // 11
        {33.4, 60.5}, // 12
        {22.9, 32.7}, // 13
        {21.5, 45.8}, // 14
        {15.3, 37.8}, // 15
        {15.1, 49.6}, // 16
        {9.1, 52.8},  // 17
        {9.1, 40.3},  // 18
};

double _DISTANCE[HOLE_COUNT][HOLE_COUNT];
int main() {
    std::cout << "Execution has begun..." << std::endl;
    int index[HOLE_COUNT];
    double min_traversal = std::numeric_limits<double>::max();
    double best_traversal[HOLE_COUNT];
    for (int i = 0; i < HOLE_COUNT; i++) {
        index[i] = i;
    }
    time_t start_time, end_time;
    for (int i = 0; i < HOLE_COUNT; i++)
    {
        for (int j = 0; j < HOLE_COUNT; j++)
        {
            if (i == j)
            {
                _DISTANCE[i][j] = 0;
            }
            else {
                double dx = positions[i][0] - positions[j][0];
                double dy = positions[i][1] - positions[j][1];
                _DISTANCE[i][j] = std::sqrt(dx * dx + dy * dy);
            }
        }
        
    }
    time(&start_time);
    do {
        double distance = 0.;
        for (int i = 0; i < HOLE_COUNT - 1; i++) {
            distance += _DISTANCE[index[i]][index[i + 1]];
        }
        if (distance <= min_traversal) {
            min_traversal = distance;
            for (int i = 0; i < HOLE_COUNT; i++) {
                best_traversal[i] = index[i];
            }
        }
    } while (std::next_permutation(index, index + HOLE_COUNT));
    time(&end_time);
    std::cout << "Execution has finished..." << std::endl << std::endl << std::endl;
    std::cout << "\tShortest path is:\t" << min_traversal << std::endl << std::endl << std::endl;
    std::cout << "\tPath of traversal:\t";
    for (double a : best_traversal) {
        std::cout << a + 1 << ",";
    }
    std::cout << std::endl;
    std::cout << "\tExecution time:\t" << difftime(end_time, start_time) << " seconds";
    std::cout << std::endl;
    std::cout << std::endl;
    return 0;
}
