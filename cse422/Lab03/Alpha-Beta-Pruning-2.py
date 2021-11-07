import random

def minimax(values, height, choices, node, a, b, maximizingPlayer, prun):
    if height == 0:
        return values[node], prun

    if maximizingPlayer:
        max_val = -999999
        for k in range(choices):
            child_node = (node * choices + k)
            next_level = height - 1
            val,prun = minimax(values, next_level, choices, child_node, a, b, False, prun)
            max_val = max(max_val,val)
            a = max(a,val)
            if b <= a:
                prun += (choices - (k + 1))
                break
        return max_val, prun

    else:
        min_val = 999999
        for k in range(choices):
            child_node = (node * choices + k)
            next_level = height - 1
            val,prun = minimax(values, next_level, choices, child_node, a, b, True, prun)
            min_val = min(min_val,val)
            b = min(b, val)
            if b <= a:
                prun += (choices - (k + 1))
                break
        return min_val, prun

total_turns = int(input("please give input of total number of turns for each player"))
choices = int(input('please give input of number of choices'))
down_range = int(input('Enter lowest value of the leaf nodes'))
upper_range = int(input('Enter highest value of the leaf nodes'))

height = total_turns * 2
terminal_nodes = pow(choices, height)
print("Depth:", height)
print("Branch:", choices)
print("Terminal States (Leaf Nodes):", terminal_nodes)

terminal_nodes_values = []
for k in range(terminal_nodes):
    terminal_nodes_values.append(random.randint(down_range, upper_range))

prun = 0
output, pruned = minimax(terminal_nodes_values, height, choices, 0, -999999, 999999, True, prun)

print("Maximum amount:", output)
print("Comparisons:", terminal_nodes)
print("Comparisons:", (terminal_nodes - pruned))
