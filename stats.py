def bestWay(ways):
    print("moyenne des chemins")
    for way in ways:
        print(average(way))



def average(way):
    dist = 0
    for i in way:
        dist += i["distance"]

    dist /= len(way)
    return dist;
