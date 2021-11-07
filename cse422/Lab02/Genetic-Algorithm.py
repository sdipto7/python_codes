import numpy as np
import random

def fitness(population, n):
    # each row of population has 8 columns/indexes(0-7), each row represents a single board with 8 queens.
    # the index values of each row represents queens' position in that board.
    # total clash array for counting attacking pair for the whole population
    # total clash[0] = horizontal_clash(population[row0]) + diagonal_clash(population[row0])

    totalclash = np.zeros(len(population),dtype=int)
    for i, chromosome in enumerate(population):
        # chromosome = each row of the population, i = index of rows
        initial_population = list(chromosome)

        horizontal_clash = []
        for a in range(n):
            horizontal_clash.append(initial_population.count(initial_population[a]) - 1) #-1 is because not counting the number itself

        # horizontal clash pair
        totalclash[i] += sum(horizontal_clash) / 2

        diagonal_clash = 0
        for x in range(n):
            for y in range(n):
                if x != y:
                    x_change = abs(x-y) #for checking the x-axis change we use the indexes
                    y_change = abs(chromosome[x] - chromosome[y]) #for checking the y-axis change we use the values
                    if x_change == y_change:
                        diagonal_clash += 1

        #diagonal clash pair
        totalclash[i] += (diagonal_clash/2)

    # non_attacking_pair[0] = 28 - totalclash[0] -> like this, each index value of totalclash will be subtracted from 28
    # then will be stored indexwise in the non_attacking_pair array.

    non_attacking_pair = 28 - totalclash

    return non_attacking_pair


def select(population, fitness, mutation_threshold):
    # total is the sum of all fitness value/non-attacking pair value.
    total = sum(fitness)

    # probability of each board is dividing each fitness by total
    probability = fitness/total

    # if any fitness value probability is less than the mutation_threshold
    # remove the board from which that fitness value probability came
    # then in the removed row of population, duplicate any other row
    for i in range(len(probability)):
        if probability[i] < mutation_threshold:
            random_index = random.randint(0,len(population)-1)
            while random_index == i:
                random_index = random.randint(0, len(population)-1)
            population[i] = population[random_index]

    # now randomly choose any fitness value based on the probability
    random_select = np.random.choice(fitness,1,p=probability)

    # find out the index number of the chosen fitness value
    index = list(fitness).index(random_select)

    # return the randomly chosen fitness value's row.
    return population[index]


def crossover(x, y):
    # x and y are two selected rows/boards/parents from population both with same length
    length = len(x)

    # initializing a child list of same length as x and y. all indexes value is -1
    child = [-1] * length

    # randomly choosing a cross_point value to crossover. Want to crossover in a range of index 1 to 2nd last index
    cross_point = random.randint(1, (length - 2))

    # if generated crosspoint value = 4 then the child list will get the 0 to 3 index values from y.
    # and then the child list will get the 4 to last index values from x.
    for i in range(cross_point):
        child[i] = y[i]
    for i in range(cross_point, length):
        child[i] = x[i]

    return child


def mutate(child):
    # randomly choose an index between 0 to 7
    index_choose = random.randint(0, 7)

    #randomly choose a number between 1 to 8
    random_number = random.randint(1, 8)

    # mutate/change the randomly generated index value of child with randomly generated number
    child[index_choose] = random_number

    return child


def GA(population, n, mutation_threshold=0.3):

    # fitness_function is the total non-attacking pair of each board/row of the population
    fitness_function = fitness(population,n)

    # maximum 28 non-attacking pair can stay in a 8 queen board
    max_non_attacking_pair = 28

    # to count how many generations needed to get the solution
    generations = 0

    # checking if any of the row's/board's fitness function is 28 or not. if 28 is found then we got the goal state.
    while max_non_attacking_pair not in fitness_function:

        # next generation population is an array like population. (10rows * 8columns)
        next_generation_population = np.zeros((len(population),n),dtype=int)

        # This array will have the best crossovered,mutated,fit,selected children/boards.
        for i in range(len(population)):
            x = select(population,fitness_function,mutation_threshold)
            y = select(population,fitness_function,mutation_threshold)
            child = crossover(x, y)
            child = mutate(child)
            next_generation_population[i] = child

        # again calculate the fitness_function/non-attacking pair with the new generation population to iterate the loop.
        fitness_function = fitness(next_generation_population, n)

        # population/parents/boards are replaced with next generation population/children/boards.
        population = next_generation_population

        # one generation evolved per iteration
        generations += 1

    # the algorithm is here means 28 is found as a fitness_function of a board
    # goal_fitness is taking the maximum value from fitness_function which is 28
    goal_fitness = np.max(fitness_function)

    # then using goal_fitness, check in which index of the fitness function the value is 28
    index = list(fitness_function).index(goal_fitness)

    # store the maximum fitness value's row.
    # if maximum fitness value = 28 is found at index-0 in the fitness function then store the row-0/1st-board of the population
    board = population[index]
    # print(generations)

    return board, generations


#number of queens
n = 8

#number of boards
start_population = 10

mutation_threshold = 0.3

# population is a 10 * 8 array (10 rows, 8 column) (start_population = 10 * n = 8)
# each row of population has 8 columns/indexes(0-7), each row represents a single board with 8 queens.
# the index values of each row represents queens' position in that board.
population = np.random.randint(0, n, (start_population, n),dtype=int)

board, generations = GA(population, n, mutation_threshold)
print(f"After evolving {generations} generations we got the solution board: {board}")


