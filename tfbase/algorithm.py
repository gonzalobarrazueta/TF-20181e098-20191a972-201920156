import json
import visualizations 

def graph():
    Loc = visualizations.coordinates
    G = visualizations.graph

    response = {"loc": Loc, "g": G}

    return json.dumps(response)

def paths():
    bestpath = [-1, 0, 1, 0]
    path1 = [-1, 0, 1, 0]
    path2 = [-1, 0, 1, 0]

    response = {"bestpath": bestpath, "path1": path1, "path2": path2}

    return json.dumps(response)

