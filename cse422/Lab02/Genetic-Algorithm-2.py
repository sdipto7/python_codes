import numpy as np
import random

def fitness(population):
    safe_pair = np.full(len(population), 28)
    for i, cr in enumerate(population):
        board = list(cr)
        diagonal_clash = 0
        row_clash = []

        for k in range(len(board)):
            row_clash.append(board.count(board[k]) - 1)

        for x_0 in range(len(board)):
            for x_1 in range(len(board)):
                if x_0 != x_1:
                    if abs(x_0 - x_1) == abs(cr[x_0] - cr[x_1]):
                        diagonal_clash += 1

        safe_pair[i] -= ((sum(row_clash) / 2) + (diagonal_clash / 2))

    return safe_pair

def select(population, fit, mutation_threshold):

    pr = fit/sum(fit)
    for i in range(len(pr)):
        if pr[i] < mutation_threshold:
            random_i = i
            while random_i == i:
                random_i = random.randint(0, len(population)-1)
            population[i] = population[random_i]

    parent_index = list(fit).index(np.random.choice(fit,1,p=pr))

    return population[parent_index]

def crossover(x, y):
    cross_board = [-1] * len(x)
    divide_index = random.randint(0, (len(x) - 1))

    for k in range(len(x)):
        if k < divide_index:
            cross_board[k] = x[k]
        else:
            cross_board[k] = y[k]

    return cross_board

def mutate(child):
    random_num = random.randint(1, 8)
    random_i = random.randint(0, 7)
    child[random_i] = random_num

    return child

def GA(population, n, mutation_threshold=0.3):
    safe_pair = fitness(population)
    goal = 28
    gen = 0
    while goal not in safe_pair:
        gen += 1
        new_population = np.zeros((len(population),n))
        for k in range(len(population)):
            x = select(population,safe_pair,mutation_threshold)
            y = select(population,safe_pair,mutation_threshold)
            new_board = mutate(crossover(x, y))
            new_population[k] = new_board
        population = new_population
        safe_pair = fitness(population)

    best_fitness_index = list(safe_pair).index(np.max(safe_pair))
    row = population[best_fitness_index]
    print(gen)
    print(row)

'''for 8 queen problem, n = 8'''
n = 8

#number of boards
start_population = 10

mutation_threshold = 0.3

# population is a 10 * 8 array (10 rows, 8 column) (start_population = 10 * n = 8)
# each row of population has 8 columns/indexes(0-7), each row represents a single board with 8 queens.
# the index values of each row represents queens' position in that board.
population = np.random.randint(0, n, (start_population, n))

GA(population, n, mutation_threshold)
