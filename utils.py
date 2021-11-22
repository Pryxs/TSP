import numpy as np
import init

def getDistanceMatrix(cities):
    rowTab = []
    for i in range(len(cities)):
        row = []
        print(cities[i].name)
        # row.append(cities[i].name)
        for city in cities:
            row.append(round(cities[i].distance(city), 2))

        rowTab.append(row)

    dMatrix = np.array([rowTab[0], rowTab[1], rowTab[2], rowTab[3], rowTab[4], rowTab[5], rowTab[6],rowTab[7],rowTab[8],rowTab[9],])
    return dMatrix
            


cities = init.noRandomCity()
print(cities)
dMatrix = getDistanceMatrix(cities)
print(dMatrix)
