import numpy
import random
import matplotlib.pyplot as plt


def first_opt_fun(x1, x2):
    return 2 * x1 ** 2 + x2 ** 2


def second_opt_fun(x1, x2):
    return -(x1 - x2) ** 2


MAX_ELEM = 10000

if __name__ == '__main__':
    points = []
    points2 = []

    print("Generating points...")
    for i in range(0, MAX_ELEM):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        point = {'x': first_opt_fun(x, y), 'y': second_opt_fun(x, y)}
        points.append(point)

        while not (x * y + 1/4 >= 0):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

        point2 = {'x': first_opt_fun(x, y), 'y': second_opt_fun(x, y)}
        points2.append(point2)

    print("Points generated...")

    print("Plotting first plot...")
    plt.figure(1)
    for i in range(0, len(points)):
        foundDom = False
        for j in range(0, len(points)):
            if points[i]['x'] > points[j]['x'] and points[i]['y'] > points[j]['y']:
                foundDom = True
                break

        if not foundDom:
            plt.scatter(points[i]['x'], points[i]['y'], s=2, c='red')
        else:
            plt.scatter(points[i]['x'], points[i]['y'], s=1, c='black')

    print("Plotting second plot...")
    plt.figure(2)
    for i in range(0, len(points2)):
        foundDom = False
        for j in range(0, len(points2)):
            if points2[i]['x'] > points2[j]['x'] and points2[i]['y'] > points2[j]['y']:
                foundDom = True
                break

        if not foundDom:
            plt.scatter(points2[i]['x'], points2[i]['y'], s=2, c='red')
        else:
            plt.scatter(points2[i]['x'], points2[i]['y'], s=1, c='black')

    plt.show()
    print("Finish...")
