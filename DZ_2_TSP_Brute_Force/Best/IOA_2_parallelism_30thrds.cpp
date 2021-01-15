#include <iostream>
#include <cmath>
#include <algorithm>
#include <limits>
#include <ctime>
#include <thread>
#include <mutex>
#include <list>
#include <tuple>
#include <vector>
#include <chrono>
#include <iomanip>
#include <sstream>


std::list<std::tuple<double, std::vector<int>>> acceptable;
std::mutex list_mutex;
constexpr auto _HOLE_COUNT = 15;

double const positions[18][2] = {
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
double _DISTANCE[_HOLE_COUNT][_HOLE_COUNT];

void thread_body(int first_number, int second_number, std::vector<int> index) {
    std::vector<int> myVector = { first_number, second_number };
    double min_traversal = std::numeric_limits<double>::max();
    std::vector<int> best_traversal;
    double distance = 0;
    do {
        distance = _DISTANCE[first_number][second_number] + _DISTANCE[second_number][index[0]];
        for (int i = 0; i != index.size() - 1; ++i) {
            distance += _DISTANCE[index[i]][index[i + 1]];
        }
        if (distance <= min_traversal) {
            min_traversal = distance;
            best_traversal = index;
        }
    } while (std::next_permutation(index.begin(), index.end()));

    time_t now = time(0);

    best_traversal.insert(best_traversal.begin(), myVector.begin(), myVector.end());

    list_mutex.lock();
    acceptable.push_front(std::make_tuple(min_traversal, best_traversal));

    list_mutex.unlock();
    std::stringstream finished_message;
    finished_message << "\n-------------------------------------------------------------\n       " << first_number << ", " << second_number << "\thas Finished at " << std::put_time(std::localtime(&now), "%Y-%m-%d %X") << "\n-------------------------------------------------------------\n";

    std::cout << finished_message.str();
}

int main() {
    std::thread array[_HOLE_COUNT * (_HOLE_COUNT - 1)];

    std::cout << "Hole count:\t" << _HOLE_COUNT << std::endl;
    for (int i = 0; i < _HOLE_COUNT; i++)
    {
        for (int j = 0; j < _HOLE_COUNT; j++)
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



    auto start = std::chrono::system_clock::now();
    auto in_time_t = std::chrono::system_clock::to_time_t(start);
    std::cout << std::endl << "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" << "\t\t    Begin at:\n\t\t" << std::put_time(std::localtime(&in_time_t), "%Y-%m-%d %X") << "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" << std::endl << std::endl;

    int counter = 0;
    for (int i = 0; i < _HOLE_COUNT; i++)
    {
        
        for (int j = 0; j < _HOLE_COUNT; j++)
        {
            if (j == i) continue;
            
            std::vector<int> tempArr;
            for (int z = 0; z < _HOLE_COUNT; ++z) {
                if (z == i || z == j)
                    continue;
                tempArr.push_back(z);
             }
            array[counter++] = std::thread(thread_body, i, j, tempArr);
        } 
    }
    for (auto& i : array)
    {
        i.join();
    }
    auto end = std::chrono::system_clock::now();
    auto in_time_t_end = std::chrono::system_clock::to_time_t(end);


    std::cout << std::endl << "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" << "\t\tExecution finished at:\n\t\t" << std::put_time(std::localtime(&in_time_t_end), "%Y-%m-%d %X") << "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n" << std::endl << std::endl;


    double min_time = std::numeric_limits<double>::max();

    for (const auto& item : acceptable) {
        double dist;
        std::vector<int> points;

        std::tie(dist, points) = item;

        if (dist < min_time)
        {
            min_time = dist;
        }
        std::cout << "Distance:\t" << dist << "\tPoints:\t";
        for (int& point : points)
            std::cout << point + 1 << ", ";
        std::cout << std::endl;
    }
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "=========================================================" << std::endl;
    std::cout << "=========================================================" << std::endl;
    std::cout << "                         BEST RESULTS                    " << std::endl;
    std::cout << std::endl;

    for (auto const& item : acceptable) {
        double dist;
        std::vector<int> points;

        std::tie(dist, points) = item;

        if (dist == min_time)
        {
            std::cout << "Distance:\t" << dist << "\t || \tPoints:\t";
            for (int& point : points)
                std::cout << point + 1 << ", ";
            std::cout << std::endl;
        }

    }
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;
    auto seconds = std::chrono::duration_cast<std::chrono::seconds>(end - start);
    auto minutes = std::chrono::duration_cast<std::chrono::minutes>(end - start);
    auto hours = std::chrono::duration_cast<std::chrono::hours>(end - start);
    std::cout << "Execution time (seconds): " << seconds.count() << std::endl;
    std::cout << "Execution time (minutes): " << minutes.count() << std::endl;
    std::cout << "Execution time (hrs): " << hours.count() << std::endl;
    std::cout << "=========================================================" << std::endl;
    std::cout << "=========================================================" << std::endl;

    char x;
    std::cin >> x;
}
