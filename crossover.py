import random
import numpy as np

def crossesPopulation(population, maxPopulation):
    crossParents = []
    crossesPopulation = []
    probabilities = getProbabilities(population) # emet des probabilités selon le rang des individus
    population.sort(key = lambda x: x[1])

    # on garde le meilleur (convergence plus rapide)
    crossesPopulation.append(population[0][0])
    # population.remove(population[0])

    # on croise la population avec une proba de 0.7
    count = 0

    # on divise par 2 car on obtient 2 enfants
    for i in range(int(len(population) / 2)):
        if random.uniform(0, 1) < 0.7:
            count += 1
            parent1 = getIndividu(population, probabilities)
            parent2 = getIndividu(population, probabilities)
            # print("parent1 : ", parent1[0])
            # print("parent2 : ", parent2[0])

            # vérifie que les parents sont différent
            while(parent1 == parent2 or not crossoverCheck(crossParents, parent1, parent2)):
                # if parent1 == parent2:
                    # print("parents identique")
                parent2 = getIndividu(population, probabilities)
                # print("nouvel individu parent2 : ", parent2[0])


            # test = crossoverCheck(crossParents, parent1, parent2)
            # print(test)
            crossParents.append((parent1[0], parent2[0]))
            print("\n")
            print("parent choisi : " , parent1)
            print("parent choisi : " , parent2)

        
    print("\n sur ", len(population) , " : " , count , " croisements \n\n")

    
    print("\n LISTE DES CROISEMENTS")
    for i in crossParents:
        print(i)

    
    for couple in crossParents:
        indexCut = random.randint(int(len(couple[0]) / 4), (int(len(couple[0]) - int(len(couple[0]) / 4))) - 1)
        child1 = crossPaths(couple, indexCut)
        child2 = crossPaths(couple[::-1], indexCut)
        print("child1 : ",child1)
        print("child2 :" ,child2)
        crossesPopulation.append(child1)
        crossesPopulation.append(child2)

    if(len(crossesPopulation) < len(population)):
        print("on complète la population")
        crossesPopulation = fillPopulation(crossesPopulation, population)


    print("LONGUEUR POPULATION APRES CROISEMENT : " , len(crossesPopulation))
    print("+++++++++++++++++++++++++")
    print(crossesPopulation)
    return crossesPopulation


def crossPaths(couple, indexCut):
    child = couple[0].copy()
    print("\n on croise le couple", couple ,"sur la coupure : ", indexCut)
    
    firstPart1 = couple[0][:indexCut]
    secondPart1 = couple[0][-(len(couple[0]) - indexCut):]

    firstPart2 = couple[1][:indexCut]
    secondPart2 = couple[1][-(len(couple[1]) - indexCut):]

    print(firstPart1, secondPart1)
    print(firstPart2, secondPart2)

    for i in range(len(firstPart2)):
        changedCity = child[i]
        broughtCity = firstPart2[i]

        cityExistInSecondPart = elementInList(child, broughtCity)
        if cityExistInSecondPart:
            child[int(cityExistInSecondPart)] = changedCity

        child[i] = firstPart2[i]

    return child


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
    return adjustedProbabilities


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


def elementInList(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return str(i)

    return False


def fillPopulation(crossesPopulation, population):
    print(len(crossesPopulation), " : " , len(population))
    for i in range(int(len(population)) - int(len(crossesPopulation))):
        crossesPopulation.append(population[i + 1][0])


        
    return crossesPopulation


# def ordPorbabilities(probabilities):
#     ordPorbabilities = []
#     for x in range(len(probabilities) - 1, -1, -1):
#         ordPorbabilities.append(probabilities[x])

#     return ordPorbabilities
    

# import matplotlib.pyplot as plt
# plt.pie(test, normalize = True)
# plt.show()
