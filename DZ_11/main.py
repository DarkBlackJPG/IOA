import numpy as np
import random as rand
import math

A = [1, 5, 1]
B = [3, 2, 0]
C = [5, 7, 1]
D = [6, 3, 3]

dimensions = 3
minXValue = 1
maxXValue = 6
minYValue = 2
maxYValue = 7
minZValue = 0
maxZValue = 3

percent = 0.1

maxVelocityX = (maxXValue - minXValue) * percent
maxVelocityY = (maxYValue - minYValue) * percent
maxVelocityZ = (maxZValue - minZValue) * percent

# Initial points value
points = {
    'S1': [np.random.uniform(minXValue, maxXValue),
           np.random.uniform(minYValue, maxYValue),
           np.random.uniform(minXValue, maxYValue)],
    'S2': [np.random.uniform(minXValue, maxXValue),
           np.random.uniform(minYValue, maxYValue),
           np.random.uniform(minXValue, maxYValue)]
}


def calc_distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)


def cost_function(points_value):
    S1_local = points_value['S1']
    S2_local = points_value['S2']
    distanceA_S1 = calc_distance(A, S1_local)
    distanceB_S1 = calc_distance(B, S1_local)
    distanceC_S2 = calc_distance(C, S2_local)
    distanceD_S2 = calc_distance(D, S2_local)
    distanceS1_S2 = calc_distance(S1_local, S2_local)

    return sum([distanceA_S1,
                distanceB_S1,
                distanceC_S2,
                distanceD_S2,
                distanceS1_S2])


class Agent:
    def __init__(self):
        self.position = None
        self.velocity = None
        self.cost = None
        self.best_cost = None
        self.best_position = None

    def change_position(self, new_point):
        self.position = new_point.copy()
        self.cost = cost_function(self.position)
        if self.best_cost is None or self.cost < self.best_cost:
            self.best_position = self.position.copy()
            self.best_cost = self.cost

    def calc_new_velocity(self, w, c1, c2, g_best):
        S1_local = self.position['S1']
        S2_local = self.position['S2']
        best_S1 = self.best_position['S1']
        best_S2 = self.best_position['S2']
        g_best_S1 = g_best['points']['S1']
        g_best_S2 = g_best['points']['S2']

        # S1_local

        self.velocity[0][0] = min(w * self.velocity[0][0] +
                                  c1 * rand.uniform(0, 1) * (best_S1[0] - S1_local[0]) +
                                  c2 * rand.uniform(0, 1) * (g_best_S1[0] - S1_local[0]), maxVelocityX)

        self.velocity[0][1] = min(w * self.velocity[0][1] +
                                  c1 * rand.uniform(0, 1) * (best_S1[1] - S1_local[1]) +
                                  c2 * rand.uniform(0, 1) * (g_best_S1[1] - S1_local[1]), maxVelocityY)

        self.velocity[0][2] = min(w * self.velocity[0][2] +
                                  c1 * rand.uniform(0, 1) * (best_S1[2] - S1_local[2]) +
                                  c2 * rand.uniform(0, 1) * (g_best_S1[2] - S1_local[2]), maxVelocityZ)

        # S2
        self.velocity[1][0] = min(w * self.velocity[1][0] +
                                  c1 * rand.uniform(0, 1) * (best_S2[0] - S2_local[0]) +
                                  c2 * rand.uniform(0, 1) * (g_best_S2[0] - S2_local[0]), maxVelocityX)

        self.velocity[1][1] = min(w * self.velocity[1][1] +
                                  c1 * rand.uniform(0, 1) * (best_S2[1] - S2_local[1]) +
                                  c2 * rand.uniform(0, 1) * (g_best_S2[1] - S2_local[1]), maxVelocityY)

        self.velocity[1][2] = min(w * self.velocity[1][2] +
                                  c1 * rand.uniform(0, 1) * (best_S2[2] - S2_local[2]) +
                                  c2 * rand.uniform(0, 1) * (g_best_S2[2] - S2_local[2]), maxVelocityZ)


def pso(iterations=100, flock_size=100, c1=1.494, c2=1.494, w=0.729):
    g_best = {
        'points': points,
        'cost': cost_function(points)
    }
    flock = []
    #   initialize flock
    for i in range(0, flock_size):
        flock_agent = Agent()
        flock_agent.velocity = [np.zeros(dimensions), np.zeros(dimensions)]

        new_S1 = [np.random.uniform(minXValue, maxXValue),
                  np.random.uniform(minYValue, maxYValue),
                  np.random.uniform(minZValue, maxZValue)]

        new_S2 = [np.random.uniform(minXValue, maxXValue),
                  np.random.uniform(minYValue, maxYValue),
                  np.random.uniform(minZValue, maxZValue)]

        flock_agent.change_position({'S1': new_S1, 'S2': new_S2})

        if flock_agent.best_cost < g_best['cost']:
            g_best['cost'] = flock_agent.best_cost
            g_best['points'] = flock_agent.best_position.copy()

        flock.append(flock_agent)

    # PSO Loop
    current_iteration = 0
    for i in range(0, iterations):
        current_iteration += 1
        for agent in flock:

            agent.calc_new_velocity(w, c1, c2, g_best)

            new_pos = {
                'S1': [agent.position['S1'][0] + agent.velocity[0][0],
                       agent.position['S1'][1] + agent.velocity[0][1],
                       agent.position['S1'][2] + agent.velocity[0][2]],

                'S2': [agent.position['S2'][0] + agent.velocity[1][0],
                       agent.position['S2'][1] + agent.velocity[1][1],
                       agent.position['S2'][2] + agent.velocity[1][2]]
            }
            agent.change_position(new_pos)

            if agent.best_cost < g_best['cost']:
                g_best['points'] = agent.best_position.copy()
                g_best['cost'] = agent.best_cost

    return g_best


if __name__ == '__main__':

    test = False
    if not test:
        best = pso(iterations=2000, flock_size=100)
        np.set_printoptions(precision=20)
        print("Best position S1: {}".format(best['points']['S1']))
        print("Best position S2: {}".format(best['points']['S2']))
        print("Cost is: {}".format(best['cost']))
    else:
        S1 = [3.17271137, 3.32322492, 1.78075342]
        S2 = [4.51546244, 3.96841183, 4.00000000]
        print(cost_function({'S1': S1, 'S2': S2}))
