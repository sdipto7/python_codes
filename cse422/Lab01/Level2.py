import numpy as np

# file read
file = open('level2.txt', 'r')
lines = file.readlines()

# first two values are number of nodes and edges
nodes = int(lines.pop(0).strip())
edges = int(lines.pop(0).strip())

# creating an array to store the edge connections
adj_matrix = np.zeros((nodes,nodes), dtype=int)
for i in range(edges):
    connection = (lines.pop(0).strip()).split(' ')
    adj_matrix[int(connection[0])][int(connection[1])] = 1
    adj_matrix[int(connection[1])][int(connection[0])] = 1 # as the graph is undirected

# the next three values are Lina's position/goal node, nora's position and lara's position respectively
lina_position = int(lines.pop(0).strip())
nora_position = int(lines.pop(0).strip())
lara_position = int(lines.pop(0).strip())

def BFS(adj_matrix, start_node, goal_node):

    distance = [-1] * nodes
    queue = []
    queue.append(start_node)
    distance[start_node] = 0

    while len(queue) > 0:
        x = queue.pop(0)
        for i in range(nodes):
            if adj_matrix[x][i] == 1: # checking if there is a connection
                if distance[i] == -1: # if distance of a node is -1, means it is not visited yet
                    queue.append(i)
                    distance[i] = distance[x] + 1
                    if i == goal_node: # if goal node reached then return
                        return distance

# run BFS twice, considering starting as nora's position first and then lara's position
p = BFS(adj_matrix, nora_position, lina_position)
q = BFS(adj_matrix, lara_position, lina_position)

# check who has less moves to reach Lina's position
if p[lina_position] < q[lina_position]:
    print('Nora')
else:
    print('Lara')