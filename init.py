import random

import city

names = ["Pékin", "Paris", "Londres", "Kaboul", "Berlin", "Camberra"]
cities = []

def initCities(nb):
    for x in range(nb):
        cityInstance = city.City(random.randint(0, 10), random.randint(0, 10), names[x])
        cities.append(cityInstance)

    
    return cities


def generateRandomWay(cities, nb, startCity):
    randomWays = []
    for x in range(nb):

        tempCities = cities.copy()
        for city in cities:
            if city.name == startCity.name:
                tempCities.remove(city)
                break

        randomWay = []
        print("Ville départ : " , startCity.name)
        
        for x in range(len(tempCities)):
            if 'b' in locals():
                a = b
            elif len(randomWay) == 0:
                a = startCity
            else:
                print("error, generateRandomWay")
                exit()

            b = random.choice(tempCities)
            tempCities.remove(b)
            randomWay.append({"label" : str(a.name) + " => " +  str(b.name) +  " : d = " + str(a.distance(b)), "distance" : a.distance(b)})

            if len(tempCities) == 0:
                randomWay.append({"label" : str(b.name) + " => " +  str(startCity.name) +  " : d = " + str(b.distance(startCity)), "distance" : b.distance(startCity)})
                del b


        randomWays.append(randomWay)


    return randomWays
