import numpy as np
import matplotlib.pyplot as plt


FILES = [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708,
    631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602,
    144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845,
    486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382,
    8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936,
    1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
    2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078,
    1841018, 1915571]

class Organism:
    def __init__(self, array, optfunction):
        self.array = array
        self.optfunction = optfunction



def optimization_function(array):
    global FILES

    F = 2 ** 26
    for i in range(0, len(array)):
        F -= array[i] * FILES[i]
    if F >= 0:
        return F
    else:
        return 2 ** 26


GENERATIONS = 50

POPULATION = 2000

ITERATIONS = 20

NUMBER_OF_FILES = 64

def initialize_population():
    global NUMBER_OF_FILES
    population = []
    for i in range(0, POPULATION):
        K = np.random.uniform(1, 64)
        arr = np.zeros(NUMBER_OF_FILES)
        arr[:K] = 1
        np.random.shuffle(arr)
        opt_fun = optimization_function(arr)
        population.append(Organism(arr, opt_fun))

    return population



def genetic_algorithm():
    population = initialize_population()
    print(population)

