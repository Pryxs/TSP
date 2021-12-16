import random
import numpy as np

# cross pop, get 1 child
def crossesPopulation2(population):
    crossParents = []
    crossesPopulation = []
    probabilities = getProbabilities(population) # emet des probabilités selon le rang des individus
    population.sort(key = lambda x: x[1])

    # on garde le meilleur (convergence plus rapide)
    crossesPopulation.append(population[0][0])

    for i in range(int(len(population)/100 * 70) - 1):
        parent1 = getIndividu(population, probabilities)
        parent2 = getIndividu(population, probabilities)

        while(parent1 == parent2 or not crossoverCheck(crossParents, parent1, parent2)):
            parent2 = getIndividu(population, probabilities)


        crossParents.append((parent1[0], parent2[0]))

    for couple in crossParents:
        indexCut = random.randint(int(len(couple[0]) / 4), (int(len(couple[0]) - int(len(couple[0]) / 4))) - 1)
        child = crossPaths(couple, indexCut)
        crossesPopulation.append(child)

    
    return crossesPopulation


def crossesPopulation(population):
    print("\n\n Population sélectionné : " , population)
    crossParents = []
    crossesPopulation = []
    probabilities = getProbabilities(population) # emet des probabilités selon le rang des individus
    population.sort(key = lambda x: x[1])

    # on garde le meilleur (convergence plus rapide)
    crossesPopulation.append(population[0][0])

    # on croise la population avec une proba de 0.7
    count = 0

    # on divise par 2 car on obtient 2 enfants
    for i in range(int(len(population) / 2)):
        if random.uniform(0, 1) < 0.7:
            count += 1

            # on selectionne 2 individus
            parent1 = getIndividu(population, probabilities)
            parent2 = getIndividu(population, probabilities)

            # vérifie que les parents sont différents
            while(parent1 == parent2 or not crossoverCheck(crossParents, parent1, parent2)):
                parent2 = getIndividu(population, probabilities)

            crossParents.append((parent1[0], parent2[0]))

    print("\n\n Couple de parents : " , crossParents)
    # on croise nos couples d'individus
    for couple in crossParents:
        indexCut = random.randint(int(len(couple[0]) / 4), (int(len(couple[0]) - int(len(couple[0]) / 4))) - 1)
        child1 = crossPaths(couple, indexCut)
        child2 = crossPaths(couple[::-1], indexCut) # inverse l'ordre du tuple
        crossesPopulation.append(child1)
        crossesPopulation.append(child2)


    print("\n\n Population croisée : " ,crossesPopulation)
    if(len(crossesPopulation) < len(population)):
        # on complete la population
        crossesPopulation = fillPopulation(crossesPopulation, population)

    print("\n\n Population rempli avec les meilleurs parents : " ,crossesPopulation)
    return crossesPopulation


# croise un couple de parent
def crossPaths(couple, indexCut):
    # enfant est une copie du premier parent
    child = couple[0].copy()
    firstPart2 = couple[1][:indexCut]

    # pour chaque element dans le 2e parent (avant césure)
    for i in range(len(firstPart2)):
        changedCity = child[i] # ville changé
        broughtCity = firstPart2[i] # ville apporté

        # on check si la ville qu'on va rapporté existe dans la 2 partie de l'enfant (copie parent1)
        cityExistInSecondPart = elementInList(child, broughtCity)

        # si c'est le cas on remplace cette ville par la ville changé
        if cityExistInSecondPart:
            child[int(cityExistInSecondPart)] = changedCity

        # puis on remplace la ville changé par la ville apporté
        child[i] = firstPart2[i]

    # taux de mutation
    if random.uniform(0, 1) < 0.01:
        child = mutation(child)


    return child


# éffectue une mutation sur un individu
def mutation(child):
    rand = random.randint(1, int(len(child)) - 1)
    rand2 = random.randint(1, int(len(child)) - 1)

    switch = child[rand]
    switch2 = child[rand2]

    child[rand] = switch2
    child[rand2] = switch
    
    return child


# ajoute des probabilités aux individus de la population
def getProbabilities(population):
    population.reverse()
    probabilities = np.geomspace(1,30,num=len(population))

    j = 0
    for i in probabilities : 
        j += i

    probabilities /= j
    probabilities = probabilities.tolist()
    adjustedProbabilities = [1]

    index = 0
    for i in range(len(probabilities) - 1, -1, -1):
        adjustedProbabilities.append(adjustedProbabilities[index] - probabilities[i])
        index += 1

    adjustedProbabilities.remove(adjustedProbabilities[len(adjustedProbabilities) - 1])
    adjustedProbabilities.remove(1)
    adjustedProbabilities.append(0)
    print("\n\n Probabilités ajustées : " , adjustedProbabilities)
    return adjustedProbabilities


# sélectione un individu selon ses probabilités
def getIndividu(population, probabilities):
    rand = random.uniform(0, 1)
    for x in probabilities:
        if rand > x:
            return population[probabilities.index(x)]


# vérifie que les parents n'ont pas été deja croisé ensemble
def crossoverCheck(crossParents, parent1, parent2):
    if len(crossParents) > 0:
        for parent in crossParents:
            if (parent[0] == parent1[0]  and parent[1] == parent2[0]) or (parent[1] == parent1[0] and parent[0] == parent2[0]):
                return False
            else:
                return True
    else:
        return True


# vérifie si un élément existe dans la liste
def elementInList(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return str(i)

    return False


def fillPopulation(crossesPopulation, population):
    for i in range(int(len(population)) - int(len(crossesPopulation))):
        crossesPopulation.append(population[i + 1][0])


    return crossesPopulation
