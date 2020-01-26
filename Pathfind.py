from dijkstar import Graph, find_path

inputlist = []
filepath = 'sampleinput.txt'
with open(filepath,'r') as input:
    inputlist = input.readlines()

graph = []
for points in inputlist:
    points = points.rstrip("\n")
    graph.append(points.split(','))

for i in range(len(graph)):
    graph[i][1] = float(graph[i][1])
    graph[i][2] = float(graph[i][2])

graphDict = {}
for i in range(len(graph)):
    graphDict[graph[i][0]] = graph[i][1:]

#for points in graphDict.values():
#    print(*points)

edges = {}
for i in range(len(graph)):
    for j in range(3,len(graph[i])):
        if graph[i][j]+graph[i][0] not in edges:
            edges[graph[i][0]+graph[i][j]] = abs((graph[i][1] - graphDict[graph[i][j]][0]) + (graph[i][2] - graphDict[graph[i][j]][1]))



# class Graph:
#   def __init__(self):
#     self.nodes = set()
#     self.edges = defaultdict(list)
#     self.distances = {}

#   def add_node(self, value):
#     self.nodes.add(value)

#   def add_edge(self, from_node, to_node, distance):
#     self.edges[from_node].append(to_node)
#     self.edges[to_node].append(from_node)
#     self.distances[(from_node, to_node)] = distance


# def dijsktra(graph, initial):
#   visited = {initial: 0}
#   path = {}

#   nodes = set(graph.nodes)

#   while nodes: 
#     min_node = None
#     for node in nodes:
#       if node in visited:
#         if min_node is None:
#           min_node = node
#         elif visited[node] < visited[min_node]:
#           min_node = node

#     if min_node is None:
#       break

#     nodes.remove(min_node)
#     current_weight = visited[min_node]

#     for edge in graph.edges[min_node]:
#       weight = current_weight + graph.distance[(min_node, edge)]
#       if edge not in visited or weight < visited[edge]:
#         visited[edge] = weight
#         path[edge] = min_node

#   return visited, path




dgraph = Graph()
for key,value in edges.items():
    dgraph.add_edge(key[0],key[1],value)


path_info = find_path(dgraph,'A','G')

shortestpath = path_info.nodes
#for items in graph:
#    print(*items)

for key, value in edges.items():
    print(key, ':', value)

for nodes in shortestpath:
    print(*nodes)


