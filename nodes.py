# project VRP
# class of city
# class of depository point

class City:
    numCity = 0
    listCity = []

    def __init__(self, id, x, y, demand):
        self.id = id
        self.x = float(x)
        self.y = float(y)
        self.demand = int(demand)
        self.saved = False
        City.numCity += 1
        City.listCity.append(self)

class Depository:
    numDepot = 0
    listDepot = []

    def __init__(self, id, x, y):
        self.id = id
        self.x = float(x)
        self.y = float(y)
        Depository.numDepot += 1
        Depository.listDepot.append(self)
