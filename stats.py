def bestPath(paths):
    print("moyenne des chemins")
    ordPaths = []
    for path in paths:
        ordPaths.append(average(path))

    ordPaths.sort(key = lambda x: x[1])
    return ordPaths

def average(path):
    dist = 0
    code = ""
    for i in path:
        dist += i.distance
        code += i.code

    dist /= len(path)
    print(dist)
    return (code, dist)
