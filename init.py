import random
import json
import city, path, encoding

with open('cities.json') as f:
    names = json.load(f)['names']

cities = []


# créations des villes
def initCities(nb):
    for x in range(nb):
        cityInstance = city.City(random.randint(0, 100), random.randint(0, 100), names[x], x)
        cities.append(cityInstance)

    return cities

# def noRadomCity():
#     cities.append(city.City(0, , names[x], x)


# génération de chemins aléatoire
def generateRandomPath(cities, nb, startCity):
    print("Ville départ : " , startCity.name)
    randomPaths = []

    for x in range(nb):
        tempCities = cities.copy()
        for city in cities:
            if city.name == startCity.name:
                tempCities.remove(city)
                break

        randomPath = []
        

        for x in range(len(tempCities)):
            if 'b' in locals():
                a = b
            elif len(randomPath) == 0:
                a = startCity
            else:
                print("error, generateRandomPath")
                exit()

            b = random.choice(tempCities)
            tempCities.remove(b)
            randomPath.append(path.Path(a, b))

            if len(tempCities) == 0:
                randomPath.append(path.Path(b, startCity))
                del b


        randomPaths.append(randomPath)


    return randomPaths
