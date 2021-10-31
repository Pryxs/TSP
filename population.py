import random
import crossover

def bestPath(paths):
    print("moyenne des chemins")
    ordPaths = []
    for path in paths:
        ordPaths.append(average(path))

    ordPaths.sort(key = lambda x: x[1])
    return ordPaths


def average(path):
    dist = 0
    code = []
    for i in path:
        dist += i.distance
        code.append(i.code[0])


    dist /= len(path)
    print("dist" ,dist)
    return (code, dist)


def generateNewPopulation(population):
    populationLength = len(population)
    selectedPath = []
    # récupère les 40% top solutions
    for i in range(int((len(population) / 100) * 40)):
        selectedPath.append(population[0])
        population.remove(population[0])


    # récupère les 20% de solutions aléatoirement dans le reste
    for i in range(int((len(population) / 100) * 20)):
        indexPath = random.randint(0, len(population))
        selectedPath.append(population[indexPath])
        population.remove(population[indexPath])
        

    crossedPopulation = crossover.crossesPopulation(selectedPath, populationLength)
