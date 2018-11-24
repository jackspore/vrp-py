# project VRP
# class of city
# class of depository point

from common import *

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
    listNearbyCity = []

    def __init__(self, id, x, y):
        self.id = id
        self.x = float(x)
        self.y = float(y)
        Depository.numDepot += 1
        Depository.listDepot.append(self)

    def sortNearbyCity(self):
        self.listNearbyCity = City.listCity
        for city in self.listNearbyCity:
            city.dis = calcDistance(self, city)
        
        self.listNearbyCity.sort(key = lambda dist:city.dis)
        print('1')