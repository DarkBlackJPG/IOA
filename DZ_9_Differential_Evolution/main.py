import numpy as np
import math
import random
S = [2.424595205726587e-01, 1.737226395065819e-01, 1.315612759386036e-01, 1.022985539042393e-01,
     7.905975891960761e-02, 5.717509542148174e-02, 3.155886625106896e-02, -6.242228581847679e-03,
     -6.565183775481365e-02, -8.482380513926287e-02, -1.828677714588237e-02, 3.632382803076845e-02,
     7.654845872485493e-02, 1.152250132891757e-01, 1.631742367154961e-01, 2.358469152696193e-01,
     3.650430801728451e-01, 5.816044173713664e-01, 5.827732223753571e-01, 3.686942505423780e-01]

S_Test = [7.500000000000008881784197001252,
-7.500000000000012434497875801753,
-9.424777960769388229778087406885,
4.077422742688577628200619074050,
2.999999999999991118215802998748,
-0.999999999999996669330926124530]

F = 0.8
CR = 0.9

Xp1 = 0
Yp1 = 1
Xp2 = 2
Yp2 = 3
A1 = 4
A2 = 5

Xi = []
Yi = []
R0 = 15
N = 20

POPULATION_SIZE = 60
MAX_ITER = 10000


for i in range(0, N):
    Xi.append(R0 * math.cos((2 * math.pi * i) / N))
    Yi.append(R0 * math.sin((2 * math.pi * i) / N))


def opt_func(x):
    condition_1 = math.sqrt(x[Xp1] ** 2 + x[Yp1] ** 2)
    condition_2 = math.sqrt(x[Xp2] ** 2 + x[Yp2] ** 2)
    if condition_1 >= R0 or condition_2 >= R0:
        return 100

    opt_fun_sum = 0
    for i in range(0, N):
        op_1 = x[A1] / math.sqrt((Xi[i] - x[Xp1]) ** 2 + (Yi[i] - x[Yp1]) ** 2)
        op_2 = x[A2] / math.sqrt((Xi[i] - x[Xp2]) ** 2 + (Yi[i] - x[Yp2]) ** 2)
        temp = (op_1 + op_2 - S[i]) ** 2
        opt_fun_sum += temp

    return opt_fun_sum


if __name__ == '__main__':

    print(opt_func(S_Test) * 10e-14)

#%% ---- Initialize population ----
    current_population = []
    for i in range(0, POPULATION_SIZE):
        new_a1 = random.uniform(-15, 15)
        new_a2 = random.uniform(-15, 15)
        new_xp1 = random.uniform(-15, 15)
        new_yp1 = random.uniform(-15, 15)
        new_xp2 = random.uniform(-15, 15)
        new_yp2 = random.uniform(-15, 15)

        condition_1 = math.sqrt(new_xp1 ** 2 + new_yp1 ** 2)
        condition_2 = math.sqrt(new_xp2 ** 2 + new_xp2 ** 2)

        while condition_1 >= R0 or condition_2 >= R0:
            new_xp1 = random.uniform(-15, 15)
            new_yp1 = random.uniform(-15, 15)
            new_xp2 = random.uniform(-15, 15)
            new_yp2 = random.uniform(-15, 15)
            condition_1 = math.sqrt(new_xp1 ** 2 + new_yp1 ** 2)
            condition_2 = math.sqrt(new_xp2 ** 2 + new_xp2 ** 2)
        ok = True
        for j in range(0, len(current_population)):
            if(current_population[0] == new_xp1 and
                current_population[1] == new_yp1 and
                current_population[2] == new_xp2 and
                current_population[3] == new_yp2 and
                current_population[4] == new_a1 and
                current_population[5] == new_a2):
                i -= 1
                ok = False
                break
        if ok:
            current_population.append([new_xp1, new_yp1, new_xp2, new_yp2, new_a1, new_a2])

#%% Main loop
    best_population = current_population.copy()
    for i in range(0, MAX_ITER):
        current_population = best_population.copy()
        for individual in range(0, len(current_population)):

#%% Making temporary population
            candidate_index = list(range(0, len(current_population)))
            candidate_index.remove(individual)
            random_index = random.sample(candidate_index, 3)

            xa = current_population[random_index[0]]
            xb = current_population[random_index[1]]
            xc = current_population[random_index[2]]
            x = current_population[individual]

            xbc = []
            for j in range(0, len(xb)):
                xbc.append(F * (xb[j] - xc[j]))

            new_individual = []

            for j in range(0, len(xa)):
                new_individual.append(xa[j] + xbc[j])

#%% Crossbreeding
            crossbreed = []
            R = random.randint(0, 5)
            for j in range(0, 6):
                ri = random.uniform(0, 1)
                if ri < CR or j == R:
                    crossbreed.append(new_individual[j])
                else:
                    crossbreed.append(x[j])

            if opt_func(crossbreed) < opt_func(best_population[individual]):
                best_population[individual] = crossbreed.copy()
#%% Search for best

        for j in range(0, len(current_population)):
            if opt_func(best_population[j]) < 10e-30:
                print("Goal achieved at generation: " + str(i))
                print("Optimization function is (Non scientific notation): {:.50f}".format(opt_func(best_population[j])))
                print("Optimization function is (Scientific notation): {}".format(opt_func(best_population[j])))
                print("Result: ")
                for jj in range(0, 6):
                    print("{:.30f}".format(best_population[j][jj]))
                exit(0)









