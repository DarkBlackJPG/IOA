import numpy as np
import math
import random
import matplotlib.pyplot as plt
import pprint

FILES = [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708,
         631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602,
         144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845,
         486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382,
         8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936,
         1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
         2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078,
         1841018, 1915571]

a = np.linspace(0.94, 0.96, num=100000)


def optimization_function(X):
    F = 2 ** 26
    for i in range(0, len(X)):
        F -= X[i] * FILES[i]
    if (F >= 0):
        return F
    else:
        return 2 ** 26


def simulated_anealing(X):
    T = 32 * 1024 * 1024

    cummulative_minimum = []

    iterations = 100000

    current_x = X.copy()
    current_x_function = optimization_function(current_x)
    cummulative_minimum.append(current_x_function)
    current_minimum_combination = current_x.copy()

    h_min = 5
    h_max = 45

    current_iteration = 1

    while current_iteration < iterations:
        neighbour_hamming_distance = (h_min - h_max) / (iterations - 1) * (current_iteration - 1) + h_max
        neighbour_data = random.sample(range(64), int(neighbour_hamming_distance))
        neighbour_X = current_x.copy()

        for i in neighbour_data:
            if neighbour_X[i] == 0:
                neighbour_X[i] = 1
            else:
                neighbour_X[i] = 0

        current_x_function = optimization_function(current_x)
        neighbour_x_function = optimization_function(neighbour_X)

        dE = neighbour_x_function - current_x_function

        if dE < 0:
            current_x = neighbour_X
            current_x_function = neighbour_x_function
        else:
            temp = -dE / T
            p = math.exp(temp)
            if dE == 0:
                p = 0.5
            if random.random() < p:
                current_x = neighbour_X
                current_x_function = neighbour_x_function
        T = a[current_iteration] * T

        current_iteration += 1

        if cummulative_minimum[len(cummulative_minimum) - 1] > current_x_function:
            cummulative_minimum.append(current_x_function)
            current_minimum_combination = current_x.copy()
        else:
            cummulative_minimum.append(cummulative_minimum[len(cummulative_minimum) - 1])

        if 32 > current_x_function >= 0:
            break
    print("==============================")
    print("Minimum for iteration: " + str(cummulative_minimum[len(cummulative_minimum) - 1]))
    print("Best combination: " + str(current_minimum_combination))
    print("==============================")
    return current_x_function, cummulative_minimum, current_minimum_combination


if __name__ == '__main__':

    tuple_data = []

    for i in range(0, 20):
        init_array = np.zeros(64)
        number_of_ones = np.round(random.uniform(0, 64))
        for i in range(0, int(number_of_ones)):
            init_array[i] = 1

        np.random.shuffle(init_array)
        optimization_best, cumulative_minimum, best_combination = simulated_anealing(init_array.astype(int))
        tuple_data.append([optimization_best, cumulative_minimum, best_combination])

    average_cumulative_array = []
    iteration = 0

    for i in range(0, len(tuple_data[0][1])):
        average = 0
        count = 0
        for j in tuple_data:
            count += 1
            if i >= len(j[1]):
                average += j[1][len(j[1]) - 1]
            else:
                average += j[1][i]
        average /= count
        average_cumulative_array.append(average)

    plt.figure(1, dpi=200, figsize=[10.8, 9])
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(color='lightgray', linestyle='-', linewidth=1)
    plt.axhline(32, linestyle='--', color='lightgreen')
    plt.title("Kumulativni minimum")
    plt.xlabel("Iteracija")
    plt.ylabel("Vrednost")
    x_values = np.arange(0, 100000)
    for i in tuple_data:
        temp = i[1][len(i[1]) - 1]
        while len(i[1]) != 100000:
            i[1].append(temp)
        plt.plot(x_values, i[1])
    plt.show()
    plt.figure(2, dpi=200, figsize=[10.8, 9])
    plt.axhline(32, linestyle='--', color='lightgreen')
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(color='lightgray', linestyle='-', linewidth=1)
    plt.title("Srednji kumulativni minimum")
    plt.xlabel("Iteracija")
    plt.ylabel("Vrednost")
    x_values = np.arange(0, 100000)
    plt.plot(x_values, average_cumulative_array)
    plt.show()
    plt.figure(3, dpi=200, figsize=[10.8, 9])
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(color='lightgray', linestyle='-', linewidth=1)
    plt.title("Vrednost 'a' kroz iteracije")
    plt.xlabel("Iteracija")
    plt.ylabel("Vrednost")
    x_values = np.arange(0, 100000)
    plt.plot(x_values, a)
    plt.show()
    sorted_data = sorted(tuple_data, key=lambda x: x[0])
    print("===================")
    print("Najbolje resenje: " + str(sorted_data[0][0]))
    print("--------------------")
    print("Dobijeno sa vrednostima: ")
    print(tuple_data[0][2])
    print("====================")
