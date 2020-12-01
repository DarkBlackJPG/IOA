import numpy as np
import scipy.optimize as opt
import itertools
import pprint

COND_MATRIX = np.array([
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [480, 650, 580, 390, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 480, 650, 580, 390, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 480, 650, 580, 390]
])

COST_FUN_ARRAY = np.array([
    310,
    380,
    350,
    285,
    310,
    380,
    350,
    285,
    310,
    380,
    350,
    285
])

CONDITION_ARRAY = np.array([
    10,
    16,
    8,
    18,
    15,
    23,
    12,
    6800,
    8700,
    4300
])

def preprocess_array(preprocess_array,non_zero_index_array ):
    for i in range(0, len(preprocess_array)):
        if preprocess_array[i] < 10e-2:
            preprocess_array[i] = 0
        else:
            non_zero_index_array.append(i)
            preprocess_array = np.round(preprocess_array)

    return preprocess_array, non_zero_index_array

def find_best_result(permutation_array, non_zero_index_array, array):
    max_gigaflops = -1
    best_p = []
    best_array = []
    for p in itertools.product(permutation_array, repeat=len(non_zero_index_array)):
        skip = False
        for i in range(0, len(non_zero_index_array)):
            if array[non_zero_index_array[i]] + p[i] < 0:
                skip = True
                break
        if skip is True:
            continue
        else:
            temp = array.copy()
            for i in range(0, len(non_zero_index_array)):
                temp[non_zero_index_array[i]] += p[i]
            temp_teraflops = np.matmul(COST_FUN_ARRAY, temp)
            if temp_teraflops > max_gigaflops:
                Ax = np.matmul(COND_MATRIX, temp)
                skip = False
                for i in range(len(CONDITION_ARRAY)):
                    if Ax[i] > CONDITION_ARRAY[i]:
                        skip = True
                if not skip:
                    max_gigaflops = temp_teraflops
                    best_p = p
                    best_array = temp.copy()

    return max_gigaflops, best_p, best_array

if __name__ == '__main__':
    optimization_result = opt.linprog(-COST_FUN_ARRAY, COND_MATRIX, CONDITION_ARRAY)
    print(optimization_result)
    preprocessed_array, non_zero_index_array = preprocess_array(optimization_result.x, [])
    shift_array = np.arange(-3, 4, 1)
    gigaflops, best_permutation, best_array = find_best_result(shift_array,  non_zero_index_array, preprocessed_array)

    print("==============================")
    print("Gigaflops: "+str(gigaflops))
    print("Best permutation: "+str(best_permutation))
    print("Best array: ")
    pprint.pprint(best_array)
    print("==============================")