import numpy
import random
import matplotlib.pyplot as plt


def first_opt_fun(x1, x2):
    return 2 * x1 ** 2 + x2 ** 2


def second_opt_fun(x1, x2):
    return -(x1 - x2) ** 2


MAX_ELEM = 10000

if __name__ == '__main__':
    points_x = []
    points_y = []
    points2_x = []
    points2_y = []

    print("Generating points...")
    for i in range(0, MAX_ELEM):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        points_x.append(first_opt_fun(x, y))
        points_y.append(second_opt_fun(x, y))

        while not (x * y + 1/4 >= 0):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

        points2_x.append(first_opt_fun(x,y))
        points2_y.append(second_opt_fun(x,y))

    print("Points generated...")

    print("Finding points...")

    first_light_x = []
    first_light_y = []
    first_red_x = []
    first_red_y = []
    second_light_x = []
    second_light_y = []
    second_red_x = []
    second_red_y = []
    for i in range(0, MAX_ELEM):
        foundDom = False
        for j in range(0, MAX_ELEM):
            if points_x[i] > points_x[j] and points_y[i] > points_y[j]:
                foundDom = True
                break
        if not foundDom:
            first_red_x.append(points_x[i])
            first_red_y.append(points_y[i])
        else:
            first_light_x.append(points_x[i])
            first_light_y.append(points_y[i])


    for i in range(0, MAX_ELEM):
        foundDom = False
        for j in range(0, MAX_ELEM):
            if points2_x[i] > points2_x[j] and points2_y[i] > points2_y[j]:
                foundDom = True
                break
        if not foundDom:
            second_red_x.append(points2_x[i])
            second_red_y.append(points2_y[i])
        else:
            second_light_x.append(points2_x[i])
            second_light_y.append(points2_y[i])

    print("Points found")
    print("Generating plots")

    plt.figure(1, dpi=320, figsize=[26.7, 15])
    plt.grid()
    plt.scatter(first_light_x, first_light_y, marker='o', s=1, c='lightgray')
    plt.scatter(first_red_x, first_red_y, marker='x',s=1, c='red')

    plt.figure(2, dpi=320, figsize=[26.7, 15])
    plt.grid()
    plt.scatter(second_light_x, second_light_y, marker='o',s=1, c='lightgray')
    plt.scatter(second_red_x, second_red_y, marker='x',s=1, c='red')
    plt.show()
    print("Finish...")
