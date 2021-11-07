import numpy as np
import math

def minimax(node_index, depth, alpha, beta, maximizingPlayer):
    # prun count is the number of nodes pruned.
    # number_of_nodes_per_state is the branches or number of child's per node
    # leaf nodes_values is the array of random values from which we are finding a solution using this algorithm

    # global prun_count, number_of_nodes_per_state, leaf_nodes_values

    # if we want we can only mention prun_count as global inside the minimax function.
    # because only prun_count value is updated in this function. other global variable values are not being updated inside this function.
    # so, only just to use those global variables, we don't need to mention those as global inside this function.
    global prun_count

    if depth == 0:
        return leaf_nodes_values[node_index]

    if maximizingPlayer:
        maxEval = -math.inf
        for c in range(number_of_nodes_per_state):
            eval = minimax((node_index * number_of_nodes_per_state + c), (depth-1), alpha, beta, False)
            maxEval = max(maxEval,eval)
            alpha = max(alpha,eval)
            if alpha >= beta:
                prun_count += (number_of_nodes_per_state - (c + 1))
                break
        return maxEval

    else:
        minEval = math.inf
        for c in range(number_of_nodes_per_state):
            eval = minimax((node_index * number_of_nodes_per_state + c), (depth-1), alpha, beta,True)
            minEval = min(minEval,eval)
            beta = min(beta, eval)
            if alpha >= beta:
                prun_count += (number_of_nodes_per_state - (c + 1))
                break
        return minEval


## prun_count,number_of_nodes_per_state,leaf_nodes_values --> these three are used here as global variable
## because we will use these three variable in the function with a fixed value.
## Also because, we don't want to send these three as parameter of the function.

global prun_count, number_of_nodes_per_state, leaf_nodes_values

# number of turns in the game for each player
each_player_turn = int(input('Enter the number of turns of RIYAD'))

# Branches/number of childs per node
number_of_nodes_per_state = int(input('Enter the number of choices for each turn'))

lowest_range = int(input('Enter the minimum possible value of leaf nodes'))
highest_range = int(input('Enter the maximum possible value of leaf nodes'))

# number of nodes pruned
prun_count = 0
depth = 2 * each_player_turn
number_of_leaf_nodes = pow(number_of_nodes_per_state,depth)

# random leaf node values with the lowest and highest range
leaf_nodes_values = np.random.randint(lowest_range,highest_range,number_of_leaf_nodes)

maximum_amount = minimax(0, depth, -math.inf, math.inf, True)

print(f"Depth: {depth}")
print(f"Branch: {number_of_nodes_per_state}")
print(f"Terminal States (Leaf Nodes): {number_of_leaf_nodes}")
print(f"Maximum amount: {maximum_amount}")
print(f"Comparisons: {number_of_leaf_nodes}")
print(f"Comparisons: {number_of_leaf_nodes - prun_count}")
