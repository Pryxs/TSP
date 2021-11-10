from random import random
import init
import random
import population
import encoding
import jsonwriter
import json
import numpy

# création de n villes
cities = init.initCities(5)
# startCity = random.choice(cities)
startCity = cities[0]


# création de n chemins sur une ville de départ aléatoire
randomPaths = init.generateRandomPath(cities, 10, startCity)


for i in range (2):
    # ordonne les meilleurs chemins
    ordPaths = population.bestPath(randomPaths)
    jsonwriter.savePopulation(ordPaths)

    # regenere une nouvelle population
    newPaths = population.generateNewPopulation(ordPaths, startCity, cities)

    # converti au bon format objet
    finalPopulation = encoding.vectorToObject(newPaths, cities)
    randomPaths = finalPopulation


with open('results.json') as f:
    list = json.load(f)['list']
    count = 1
    counts = []
    values = []
    best = []
    for element in list:
        for v in element.values():
            # print(v[0][1])
            counts.append(count)
            count += 1
            best.append(round(float(v[0][1]), 2))

        for key in element.keys():
            values.append(round(float(key), 2))


    import matplotlib.pyplot as plt
    plt.plot(counts, best)
    plt.title("Occurence/meilleur chemin")
    plt.show()

    plt.plot(counts, values)
    plt.title("Occurence/moyenne")
    plt.show()


### DEBUG ###

# def printPath(path):
#     print("ville de départ : ", path.startCity.name)
#     print("ville d'arrivé : ", path.arrivalCity.name)
#     print("distance : ", path.distance)
#     print("code : ", path.code)
#     print("===========================")

# feedback des chemins
# for i in randomPaths:
#     print("\n\n")
#     for j in i:
#         printPath(j)


# feedback du poids des chemins
# print("\n\n")
# print(ordPaths)