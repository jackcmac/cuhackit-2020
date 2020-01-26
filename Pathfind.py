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

edges = {}
for i in range(len(graph)):
    for j in range(3,len(graph[i])):
        if graph[i][j]+graph[i][0] not in edges:
            edges[graph[i][0]+graph[i][j]] = abs((graph[i][1] - graphDict[graph[i][j]][0]) + (graph[i][2] - graphDict[graph[i][j]][1]))

dgraph = Graph()
for key,value in edges.items():
    dgraph.add_edge(key[0],key[1],value)


path_info = find_path(dgraph,'A','G')

shortestpath = path_info.nodes

for key, value in edges.items():
    print(key, ':', value)

for nodes in shortestpath:
    print(*nodes)


