import math

class City:
    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y

    # retourne la distance euclidienne entre 2 villes (valeur absolue)
    def distance(self, city):
        return math.sqrt((abs(self.x - city.x) ** 2) +  (abs(self.y - city.y) ** 2))
