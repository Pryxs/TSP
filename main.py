from random import random
import init
import random
import stats

cities = init.initCities(5)
randomWays = init.generateRandomWay(cities, 2, random.choice(cities))

# feedback pour debug
for i in randomWays:
    print("=======")
    for j in i:
        print(j['label'])


print("=======")
stats.bestWay(randomWays)