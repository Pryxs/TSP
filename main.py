from random import random
import init
import random
import population
import encoding
import jsonwriter
import json
import numpy
import os

### DEBUG ###

def printPath(path):
    print("ville de départ : ", path.startCity.name)
    print("ville d'arrivé : ", path.arrivalCity.name)
    print("distance : ", path.distance)
    print("code : ", path.code)
    print("===========================")

# # feedback des chemins
def showPath(path):
    for i in randomPaths:
        print("\n\n")
        for j in i:
            printPath(j)



os.remove("results.json")
with open('results.json', 'w') as f: 
    json.dump({"list" : []}, f)
    pass

# création de n villes
# cities = init.initCities(12)
# startCity = random.choice(cities)
cities = init.noRandomCity()
startCity = cities[0]

# création de n chemins sur une ville de départ aléatoire
randomPaths = init.generateRandomPath(cities, 35, startCity)
showPath(randomPaths)


for i in range (150):
    # ordonne les meilleurs chemins
    ordPaths = population.bestPath(randomPaths)
    print("\n\n Fitness : ", ordPaths)
    jsonwriter.savePopulation(ordPaths)

    # regenere une nouvelle population
    newPaths = population.generateNewPopulation(ordPaths, startCity, cities)

    # converti au bon format objet
    finalPopulation = encoding.vectorToObject(newPaths, cities)
    randomPaths = finalPopulation


### VISUALISATION ###

### nécessite matplotlib ! ###

# with open('results.json') as f:
#     list = json.load(f)['list']
#     count = 1
#     counts = []
#     values = []
#     best = []
#     for element in list:
#         for v in element.values():
#             # print(v[0][1])
#             counts.append(count)
#             count += 1
#             best.append(round(float(v[0][1]), 2))

#         for key in element.keys():
#             values.append(round(float(key), 2))


#     import matplotlib.pyplot as plt
#     plt.plot(counts, best)
#     plt.title("Occurence/meilleur chemin")
#     plt.show()

#     plt.plot(counts, values)
#     plt.title("Occurence/moyenne")
#     plt.show()
