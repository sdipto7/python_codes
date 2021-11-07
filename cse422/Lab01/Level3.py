import numpy as np

# file read
file = open('level3.txt', 'r')
lines = file.readlines()

# first two values are number of nodes and edges
nodes = int(lines.pop(0).strip())
edges = int(lines.pop(0).strip())

# creating an array to store the edge connections
adj_matrix = np.zeros((nodes,nodes), dtype=int)
# This is a directed graph and the direction of the graph is reversed
for i in range(edges):
    connection = (lines.pop(0).strip()).split(' ')
    # reversing the direction of the graph
    adj_matrix[int(connection[1])][int(connection[0])] = 1

# the next value is Lina's position
lina_position = int(lines.pop(0).strip())
# the next value is the count of participant
number_of_participant = int(lines.pop(0).strip())

# the next values are positions of the participants
participant = []
for i in range(number_of_participant):
    participant.append(int(lines.pop(0).strip()))

def BFS(adj_matrix, start_node):

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

    return distance

# run the BFS function once and store the distance list of the nodes
y = BFS(adj_matrix, lina_position)

# setting two large values to minimum distance and winning participant number
min_distance = 100
winner = 100
for i in range(len(participant)):
    # checking which participant requires less moves to reach to Lina's position
    if y[participant[i]] <= min_distance:
        winner = i
        min_distance = y[participant[i]]

print("Minimum moves require to kill the enemy is {}".format(min_distance))
print("Winner is the {}th participant who was in the {}th node initially and requires {} moves to kill the enemy".format((winner + 1), participant[winner], min_distance))