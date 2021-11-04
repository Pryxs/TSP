import random
import numpy as np

def crossesPopulation(population, maxPopulation):
    crossParents = []
    crossesPopulation = []
    probabilities = getProbabilities(population) # emet des probabilités selon le rang des individus
    population.sort(key = lambda x: x[1])

    # on garde le meilleur (convergence plus rapide)
    crossesPopulation.append(population[0])
    # population.remove(population[0])

    # on croise la population avec une proba de 0.7
    for i in range(len(population)):
        if random.uniform(0, 1) < 0.7:
            parent1 = getIndividu(population, probabilities)
            parent2 = getIndividu(population, probabilities)
            print("parent1 : ", parent1[0])
            print("parent2 : ", parent2[0])

            # vérifie que les parents sont différent
            while(parent1 == parent2 or not crossoverCheck(crossParents, parent1, parent2)):
                if parent1 == parent2:
                    print("parents identique")
                parent2 = getIndividu(population, probabilities)
                print("nouvel individu parent2 : ", parent2[0])


            # test = crossoverCheck(crossParents, parent1, parent2)
            # print(test)
            crossParents.append((parent1[0], parent2[0]))
            print("parent choisi : " , parent1)
            print("parent choisi : " , parent2)
            print("========== \n")

    
    print("\n\n LISTE DES CROISEMENTS")
    for i in crossParents:
        print(i)

    
    for couple in crossParents:
        crossPaths(couple)


def crossPaths(couple):
    child1 = couple[0]
    child2 = []
    indexCut = random.randint(int(len(couple[0]) / 4), (int(len(couple[0]) - int(len(couple[0]) / 4))) - 1)
    print("on croise le couple", couple ,"sur la coupure : ", indexCut)
    
    firstPart = couple[0][:indexCut]
    secondPart = couple[1][-(len(couple[1]) - indexCut):]

    print(firstPart)
    for i in range(len(firstPart)):
        print(firstPart[i])

    # child1.append(couple[0][:indexCut] + couple[1][-(len(couple[1]) - indexCut):])
    print(child1)



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


# def ordPorbabilities(probabilities):
#     ordPorbabilities = []
#     for x in range(len(probabilities) - 1, -1, -1):
#         ordPorbabilities.append(probabilities[x])

#     return ordPorbabilities
    

# import matplotlib.pyplot as plt
# plt.pie(test, normalize = True)
# plt.show()
