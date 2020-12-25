import numpy as np
import random as rand
import math

A = [1, 5, 1]
B = [3, 2, 0]
C = [5, 7, 1]
D = [6, 3, 3]
dimensions = 3
minValue = 0
maxValue = 10

# Initial points value
points = {
    'S1': np.random.uniform(minValue, maxValue, dimensions),
    'S2': np.random.uniform(minValue, maxValue, dimensions)
}


def calc_distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 +(x[2] - y[2]) ** 2)


def cost_function(points):
    S1 = points['S1']
    S2 = points['S2']

    distanceA_S1 = calc_distance(A, S1)
    distanceB_S1 = calc_distance(B, S1)
    distanceC_S2 = calc_distance(C, S2)
    distanceD_S2 = calc_distance(D, S2)
    distanceS1_S2 = calc_distance(S1, S2)

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
            self.best_position = self.position
            self.best_cost = self.cost
    def calc_new_velocity(self, w, c1, c2, gbest):
        S1 = self.position['S1']
        S2 = self.position['S2']
        best_S1 = self.best_position['S1']
        best_S2 = self.best_position['S2']
        gbest_S1 = gbest['points']['S1']
        gbest_S2 = gbest['points']['S1']

        # S1
        self.velocity[0] = w * self.velocity[0] + \
                        c1 * rand.random() * (best_S1 - S1) + \
                        c2 * rand.random() * (gbest_S1 - S1)
        # S2
        self.velocity[1] = w * self.velocity[1] + \
                        c1 * rand.random() * (best_S2 - S2) + \
                        c2 * rand.random() * (gbest_S2 - S2)


def PSO(iterations=100, flock_size=100, c1=1.494, c2=1.494, w=0.729):
    gbest = {
        'points': points,
        'cost': cost_function(points)
    }
    flock = []
#   initialize flock
    for i in range(0, flock_size):
        flock_agent = Agent()
        flock_agent.velocity = [np.zeros(dimensions), np.zeros(dimensions)]
        new_S1 = np.random.uniform(minValue, maxValue, dimensions)
        new_S2 = np.random.uniform(minValue, maxValue, dimensions)
        flock_agent.change_position({'S1': new_S1, 'S2': new_S2})

        if flock_agent.best_cost < gbest['cost']:
            gbest['cost'] = flock_agent.best_cost
            gbest['points'] = flock_agent.best_position.copy()
# PSO Loop
    current_iteration = 0
    for i in range(0, iterations):
        current_iteration += 1
        for agent in flock:
            agent.calc_new_velocity(w, c1, c2, gbest)
            new_pos = {
                'S1': agent.position['S1'] + agent.velocity[0],
                'S2': agent.position['S2'] + agent.velocity[1]
            }
            agent.change_position(new_pos)

            if agent.best_cost < gbest['cost']:
                gbest['points'] = agent.best_position.copy()
                gbest['cost'] = agent.best_cost

    return gbest


if __name__ == '__main__':

    # Best
    # position
    # S1: [2.6924594632218293 3.587134506499059  0.7486731994209173]
    # Best
    # position
    # S2: [5.238872129380885  4.7903202507143945 1.8419299193456995]
    # Cost is: 11.662335956551718

    test = True
    if not test:
        best = PSO(iterations=1000000, flock_size= 200000)
        np.set_printoptions(precision=20)
        print("Best position S1: {}".format(best['points']['S1']))
        print("Best position S2: {}".format(best['points']['S2']))
        print("Cost is: {}".format(best['cost']))
    else:
        S1 = [2.6924594632218293, 3.587134506499059,  0.7486731994209173]
        S2 = [5.238872129380885,  4.7903202507143945, 1.8419299193456995]
        print(cost_function({'S1': S1, 'S2': S2}))