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

def noRandomCity():
    cities.append(city.City(0, 0, names[0], 0))
    cities.append(city.City(20, 6, names[1], 1))
    cities.append(city.City(36, 3, names[2], 2))
    cities.append(city.City(42, 30, names[3], 3))
    cities.append(city.City(30, 24, names[4], 4))
    cities.append(city.City(16, 40, names[5], 5))
    cities.append(city.City(6, 34, names[6], 6))
    cities.append(city.City(22, 28, names[7], 7))
    cities.append(city.City(2, 26, names[8], 8))
    cities.append(city.City(18, 14, names[9], 9))

    # cities.append(city.City(12, 50, names[10], 10))
    # cities.append(city.City(50, 16, names[11], 11))
    # cities.append(city.City(25, 25, names[12], 12))
    return cities



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
