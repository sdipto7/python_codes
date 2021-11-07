import numpy as np

# file read
file = open('level1.txt', 'r')
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

# the next value is Lina's position/goal node
lina_position = int(lines.pop(0))

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

y = BFS(adj_matrix, 0, lina_position) #start node is 0 according to the question
print(y[lina_position])