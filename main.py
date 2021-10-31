from random import random
import init
import random
import population
import crossover

# création de n villes
cities = init.initCities(12)

# création de n chemins sur une ville de départ aléatoire
randomPaths = init.generateRandomPath(cities, 9, random.choice(cities))

# ordonne les meilleurs chemins
ordPaths = population.bestPath(randomPaths)

# regenere une nouvelle population
newPaths = population.generateNewPopulation(ordPaths)

### DEBUG ###

def printPath(path):
    print("ville de départ : ", path.startCity.name)
    print("ville d'arrivé : ", path.arrivalCity.name)
    print("distance : ", path.distance)
    print("code : ", path.code)
    print("===========================")

# feedback des chemins
# for i in randomPaths:
#     print("\n\n")
#     for j in i:
#         printPath(j)


# feedback du poids des chemins
print("\n\n")
# print(ordPaths)
