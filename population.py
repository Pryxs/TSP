import random
import crossover
import init

def bestPath(paths):
    # print("moyenne des chemins")
    ordPaths = []
    for path in paths:
        ordPaths.append(average(path))

    ordPaths.sort(key = lambda x: x[1])
    # for i in ordPaths:
        # print(i)
    return ordPaths


def average(path):
    dist = 0
    code = []
    for i in path:
        dist += i.distance
        code.append(i.code[0])


    # dist /= len(path)
    # print("dist" ,dist)
    return (code, dist)


def generateNewPopulation(population, startCity, cities):
    populationLength = len(population)
    selectedPath = []
    # récupère les 60% top solutions
    for i in range(int((populationLength / 100) * 60)):
        selectedPath.append(population[0])
        population.remove(population[0])


    # récupère les 20% de solutions aléatoirement dans le reste
    for i in range(int((populationLength / 100) * 20)):
        indexPath = random.randint(0, len(population) - 1)
        selectedPath.append(population[indexPath])
        population.remove(population[indexPath])
        
    
    crossedPopulation = crossover.crossesPopulation(selectedPath)
    # print("on complete avec ", populationLength - int(len(crossedPopulation)) , " random path")
    fillPopulationWithRandom = bestPath(init.generateRandomPath(cities, populationLength - int(len(crossedPopulation)), startCity))

    for path in fillPopulationWithRandom:
        crossedPopulation.append(path[0])


    return crossedPopulation
