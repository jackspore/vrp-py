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
        # for city in self.listNearbyCity:
        #     city.dis = calcDistance(pos1=Pos2D(self.x, self.y), pos2=Pos2D(city.x, city.y))
        # self.listNearbyCity = sorted(self.listNearbyCity, key = lambda city: calcDistance(Pos2D(self.x, self.y), Pos2D(city.x, city.y)))

        self.listNearbyCity.sort(key = lambda city: calcDistance(Pos2D(self.x, self.y), Pos2D(city.x, city.y)))
        print('sorted cities by distance to depot', self.id)