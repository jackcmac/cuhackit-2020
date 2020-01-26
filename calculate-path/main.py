from dijkstar import Graph, find_path
import pyproj

def calculate(request):
    request_json = request.get_json()
    inputlist = []
    filepath = 'map.txt'
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
        for j in range(3, len(graph[i])):
            geod = pyproj.Geod(ellps='WGS84')

            lat0, lon0 = graph[i][1], graph[i][2]
            lat1, lon1 = graphDict[graph[i][j]][0], graphDict[graph[i][j]][1]

            azimuth1, azimuth2, distance = geod.inv(lon0, lat0, lon1, lat1)
            edges[graph[i][0]+graph[i][j]] = distance * 3.28084

    dgraph = Graph()
    for key, value in edges.items():
        dgraph.add_edge(key[0],key[1],value)


    path_info = find_path(dgraph,request_json["startWaypoint"],request_json["destinationWaypoint"])

    shortestpath = path_info.nodes

    turnList = []
    turnfilepath = 'turnDictionary.txt'
    with open(turnfilepath, 'r') as input:
        turnList = input.readlines()

    fileEntries = []
    for turns in turnList:
        turns = turns.rstrip("\n")
        fileEntries.append(turns.split(','))

    turnDict = {}
    for entry in fileEntries:
        turnDict[entry[0]] = int(entry[1])

    distances = []

    for node in range(len(shortestpath) - 1):
        distances.append(edges[shortestpath[node] + shortestpath[node + 1]])

    turns = [0]
    for i in range(1, len(shortestpath) - 1):

        turnTriple = shortestpath[i-1] + shortestpath[i] + shortestpath[i + 1]
        if turnTriple in turnDict.keys():
            turns.append(turnDict[turnTriple])
        else:
            turns.append(0)

    i = 1
    while i < len(turns) - 1:
        if turns[i] == 0:
            turns.pop(i)
            distances[i - 1] += distances[i]
            distances.pop(i)
            shortestpath.pop(i)
            i -= 1
        i += 1

    instructions = ""
    for node in range(len(shortestpath) - 1):
        turnString = "then "
        if node < len(shortestpath) - 2:
            if turns[node+1] < 0:
                turnString += "turn left"
            elif turns[node+1] == 0:
                turnString += "continue straight"
            else:
                turnString += "turn right"
        else:
            turnString = "to your destination"
        instructions += "Go forward " + str(round(distances[node] / float(request_json["feetPerStep"]))) + " steps " + turnString + ". "

    return instructions
