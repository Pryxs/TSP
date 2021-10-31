class Path:
    def __init__(self, startCity, arrivalCity):
        self.startCity = startCity
        self.arrivalCity = arrivalCity
        self.distance = startCity.distance(arrivalCity)
        self.code = [startCity.code, arrivalCity.code]
