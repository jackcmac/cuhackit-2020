def write_directions(path,turns,distances):
    directions = []
    for nodes in path:
        instruction = "Go forward " + distances[nodes] " [units] " + " then face " + turns[nodes]
        directions.append(instruction)
    return directions

def create_distance_dict(path,edges):
    distances = []
    for nodes in range(len(path)-1):
        distances.append(edges[path[nodes]+path[nodes+1]]
    return distances

def create_turn_dict(path):
    turns = []
    for nodes in range(len(path)-2):
        turns.append(getTurns(path[nodes],path[nodes+1],path[nodes+2]))
    return turns



