def crossesPopulation(population, maxPopulation):
    # on garde le meilleur
    crossesPopulation = []
    crossesPopulation.append(population[0])
    population.remove(population[0])

    # on croise le reste avec une proba de 0.5
    for i in range(len(population)):
        print("test")

    print(crossesPopulation)
    print(population)


def crossPaths(path1, path2):
    print("test")