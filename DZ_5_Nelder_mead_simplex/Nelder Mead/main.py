from pickletools import optimize

import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt


def out(w_array, x_in):
    function_param_temp = 0.
    for i in range(5, 10):
        function_param_temp += w_array[i] * np.tanh(w_array[i - 5] * x_in)
    return np.tanh(function_param_temp)


def train(xin):
    return 1 / 2 * np.sin(np.pi * xin)


def optimization_function(w_arr):
    sum_squares = 0.
    x_ins = np.arange(-1., 1.1, 0.1)
    for elem in w_arr:
        if abs(elem) > 10:
            return 10e14
    for elem in x_ins:
        sum_squares += np.power((out(w_arr, elem) - train(elem)), 2)

    return np.sqrt(sum_squares)


if __name__ == '__main__':
    while True:
        w_array = np.random.uniform(low=-10, high=10, size=(10,))
        simplex_alg = opt.minimize(optimization_function, w_array, method="Nelder-Mead",
                                   options={'xatol': 1e-14, 'maxfev': 1e10, 'disp': True, 'ftol': 1e-7})
        result = simplex_alg.x
        cost_fun = simplex_alg.fun
        if simplex_alg.fun < 10e-3:
            break

    print("===========================================")
    print("Current weight distribution:\n")
    count = 0
    for i in result:
        print('W' + str(count + 1) + ' {:.20f}'.format(i))
        count += 1
    print()
    print("Cost function is: " + str(cost_fun))
    print("===========================================")
    x_ins = np.arange(-1., 1.1, 0.1)

    x_train = []
    x_out = []
    for x in x_ins:
        x_train.append(train(x))
        x_out.append(out(result, x))

    plt.figure(dpi=300, figsize=[10.8, 9.60])
    plt.grid(color='lightgray', linestyle='-', linewidth=2)
    plt.plot(x_ins, x_train)
    plt.plot(x_ins, x_out)
    plt.show()
