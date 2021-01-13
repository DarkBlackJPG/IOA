import numpy as np
import random


class Organism:
    def __init__(self, array, optfunction):
        self.array = array
        self.optfunction = optfunction

    def __copy__(self):
        return Organism(self.array.copy(), self.optfunction)


GENERATIONS = 50

POPULATION = 2000

ITERATIONS = 20

NUMBER_OF_BITS = 31

K_FACTOR = 0.25

K_BEST = int(POPULATION * K_FACTOR)

x0 = [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1]

# Pronadjena resenja
# x = []
# x.append([1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0])
# x.append([0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0])
# x.append([0.0, 1.0, 0, 1, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0, 1, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0])
# x.append([1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0])
# x.append([0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0, 1, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0])
# x.append([0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0, 1, 1.0, 0.0, 0.0, 1.0])
# x.append([1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0])



def opt(x_array=None):
    global x0
    cross_correlation_sum = 0
    auto_correlation_sum = 0

    # calculate crosscorelation
    for shift in range(0, NUMBER_OF_BITS):
        crosscorelation_same_index = 0
        crosscorelation_different_index = 0
        autocorrelation_same_index = 0
        autocorrelation_different_index = 0
        for i in range(0, NUMBER_OF_BITS):
            if x0[(i + NUMBER_OF_BITS - shift) % NUMBER_OF_BITS] == x_array[i]:
                crosscorelation_same_index += 1
            else:
                crosscorelation_different_index += 1
            if shift >= 1:
                if x_array[i] == x_array[(i + NUMBER_OF_BITS - shift) % NUMBER_OF_BITS]:
                    autocorrelation_same_index += 1
                else:
                    autocorrelation_different_index += 1

        temp = crosscorelation_same_index - crosscorelation_different_index
        if not (-4 < temp < 6):
            if temp >= 6:
                cross_correlation_sum += temp - 5
            else:
                cross_correlation_sum += -3 - temp

        temp = autocorrelation_same_index - autocorrelation_different_index
        if not (-18 < temp < 12):
            if temp >= 12:
                auto_correlation_sum += temp - 11
            else:
                auto_correlation_sum += -17 - temp

    return cross_correlation_sum, auto_correlation_sum


def opt_test(x_array=None):
    global x0
    cross_correlation_sum = 0
    auto_correlation_sum = 0

    # calculate crosscorelation
    #print("crosscor")
    for shift in range(0, NUMBER_OF_BITS):
        crosscorelation_same_index = 0
        crosscorelation_different_index = 0
        for i in range(0, NUMBER_OF_BITS):
            if x0[(i + NUMBER_OF_BITS - shift) % NUMBER_OF_BITS] == x_array[i]:
                crosscorelation_same_index += 1
            else:
                crosscorelation_different_index += 1

        temp = crosscorelation_same_index - crosscorelation_different_index
        #print(shift)
       # print(temp)
       # print()
        if not (-4 < temp < 6):
            cross_correlation_sum += 1000
        else:
            cross_correlation_sum += abs(temp)

    # calculate autocorrelation
    #print("autorcor")
    for shift in range(1, NUMBER_OF_BITS):
        autocorrelation_same_index = 0
        autocorrelation_different_index = 0
        for i in range(0, NUMBER_OF_BITS):
            if x_array[i] == x_array[(i + NUMBER_OF_BITS - shift) % NUMBER_OF_BITS]:
                autocorrelation_same_index += 1
            else:
                autocorrelation_different_index += 1

        temp = autocorrelation_same_index - autocorrelation_different_index
      #  print(shift)
      #  print(temp)
      #  print()
        if not (-18 < temp < 12):
            auto_correlation_sum += 1000
        else:
            auto_correlation_sum += abs(temp)

    return cross_correlation_sum, auto_correlation_sum


BEST_OVERALL = None


def initialize_population():
    global NUMBER_OF_BITS
    global BEST_OVERALL
    population = []
    # if not BEST_OVERALL is None:
    #     population.append(BEST_OVERALL)

    for i in range(0, POPULATION):
        K = random.randint(15, 16)
        arr = np.zeros(NUMBER_OF_BITS)
        arr[:int(K)] = 1
        np.random.shuffle(arr)
        arr = arr.tolist()
        crosscorrelation, autocorrelation = opt(arr)
        opt_fun = crosscorrelation + autocorrelation
        population.append(Organism(arr, opt_fun))

    return population


def genetic_algorithm():
    population = initialize_population()

    cummulative_minimum = []
    cummulative_minimum_maybe = []

    current_generation = 0
    current_minimum = 2 ** 26 + 1
    current_min = Organism([], 2 ** 26 + 1)

    while True:
        current_generation += 1

        population = sorted(population, key=lambda x: x.optfunction)

        if current_minimum >= population[0].optfunction:
            current_minimum = population[0].optfunction

        if current_generation >= GENERATIONS:
            return population[0], cummulative_minimum, cummulative_minimum_maybe
        current_elite = population[0:K_BEST]
        elite_parents = current_elite.copy()

        while len(current_elite) <= POPULATION:
            parent_one = int(random.randint(0, len(elite_parents) - 1))
            parent_two = int(random.randint(0, len(elite_parents) - 1))

            while parent_two == parent_one:
                parent_one = int(random.randint(0, len(elite_parents) - 1))
                parent_two = int(random.randint(0, len(elite_parents) - 1))

            parent_one = elite_parents[parent_one]
            parent_two = elite_parents[parent_two]

            if random.random() < 0.8:
                ONE_POINT_CROSSOVER = random.randint(0, NUMBER_OF_BITS - 1)
                while True:
                    offspring_one = parent_two.array[0: ONE_POINT_CROSSOVER] + parent_one.array[ONE_POINT_CROSSOVER:]
                    offspring_two = parent_one.array[0: ONE_POINT_CROSSOVER] + parent_two.array[ONE_POINT_CROSSOVER:]
                    ones_first = 0
                    ones_second = 0

                    for i in range(0, NUMBER_OF_BITS):
                        ones_first += offspring_one[i]
                        ones_second += offspring_two[i]
                    zeros_first = NUMBER_OF_BITS - ones_first
                    zeros_second = NUMBER_OF_BITS - ones_second

                    if abs(zeros_first - ones_first) == 1 and abs(zeros_second - ones_second) == 1:
                        cross_first, auto_first = opt(offspring_one)
                        temp_first = cross_first + auto_first
                        current_elite.append(Organism(offspring_one, temp_first))
                        cross_second, auto_second = opt(offspring_two)
                        temp_second = cross_second + auto_second
                        current_elite.append(Organism(offspring_two, temp_second))
                        break
                    else:
                        ONE_POINT_CROSSOVER = (ONE_POINT_CROSSOVER + 1) % NUMBER_OF_BITS

        while len(current_elite) > POPULATION:
            current_elite.pop()

        for elite_object in current_elite:
            mutation_probability = random.random()
            if mutation_probability < 0.1:
                systemRandom = random.SystemRandom()

                random_mutation_index = systemRandom.randint(0, NUMBER_OF_BITS - 1)

                if elite_object.array[random_mutation_index] == 0:
                    elite_object.array[random_mutation_index] = 1
                    i = 1
                    while elite_object.array[(random_mutation_index + i) % NUMBER_OF_BITS] != 1:
                        i += 1
                    elite_object.array[(random_mutation_index + i) % NUMBER_OF_BITS] = 0
                else:
                    elite_object.array[random_mutation_index] = 0
                    i = 1
                    while elite_object.array[(random_mutation_index + i) % NUMBER_OF_BITS] != 0:
                        i += 1
                    elite_object.array[(random_mutation_index + i) % NUMBER_OF_BITS] = 1

                cross, auto = opt(elite_object.array)
                elite_object.optfunction = cross + auto

        population = current_elite.copy()
        current_elite.clear()



# if __name__ == '__main__':
#     for i in x:
#         opt_test(i)
#         value = 0
#         for j in range(0, len(i)):
#             value = 2 * value + i[j]
#         print(value)

if __name__ == '__main__':

    organisms = []
    the_force = []

    for i in range(0, ITERATIONS):
        minimums = []
        best, cummulative_minimum, disturbance_in_the_force = genetic_algorithm()
        print("======== " + str(i + 1) + " ========")
        print("Best: " + str(best.optfunction))
        print("Array: " + str(best.array))
        print("====================")
        organisms.append(best)

    min = 2 ** 24 + 1
    index = 0
    for i in range(0, len(organisms)):
        if (organisms[i].optfunction < min):
            min = organisms[i].optfunction
            index = i + 1

    print("=====================")
    print("======== " + str(index) + " ========")
    print("Best: " + str(min))
    print("Array: " + str(organisms[index - 1].array))
    value = 0
    for j in organisms[index - 1].array:
        value = 2 * value + j
    print("Decimal: " + str(value))
    print("====================")
