# project VRP
# class of cars

from nodes import City
from nodes import Depository

import math

# member data:
#  id: car ID
#  base: the starting node of the car
#  capacity: car capacit
#  loads: current load
#  routePlan: car route plan, without reloading at deposit nodes
#  __reloadPlan: final route plan [private]
#  numCars: number of all cars
class Car:
    numCars = 0

    def __init__(self, id, base, capacity):
        self.id = id
        self.base = base
        self.capacity = int(capacity)
        self.loads = int(capacity)
        self.routePlan = []
        self.__reloadPlan = []
        Car.numCars += 1
    
    def setBase(self, newBase):
        self.base = newBase

    def setRoutePlan(self, plan):
        self.routePlan = plan

    def evaluatePlan(self):
        length = 0.0
        curPos = self.__reloadPlan[0]
        for node in self.__reloadPlan:
            length += self.__calcDistance(curPos, node)
        return length

    def insertPlanWithReload(self):
        self.__reloadPlan.clear() #reset current reload plan
        
        for depot in Depository.listDepot:
            if( depot.id == self.base ):
                self.__reloadPlan.append(depot)

        for city in self.routePlan:
            lastCity = city
            if(city.demand >= self.loads):
                self.__visitCity(city)
                self.__reloadPlan.append(lastCity)
            else:
                depot = self.__seekDepository(lastCity)
                self.__reloadPlan.append(depot)
                self.__reload()

        return self.__reloadPlan

    def __visitCity(self, city):
        self.loads -= city.demand
        city.saved = True

    def __reload(self):
        self.loads = self.capacity

    def __calcDistance(self, pos1, pos2):
        x2 = math.fabs(pos1.x - pos2.x) * math.fabs(pos1.x - pos2.x)
        y2 = math.fabs(pos1.y - pos2.y) * math.fabs(pos1.y - pos2.y)
        return math.sqrt(x2 + y2)

    def __seekDepository(self, curCity):
        __shortest = 9999999.9

        for depot in Depository.listDepot:
            length = self.__calcDistance(curCity, depot)
            if(length < __shortest):
                __shortest = length
                __depot = depot

        print("Reload at depot: %s, position: %f, %f" % depot.id, depot.x, depot.y)
        return depot

    def printFinalRoute(self):
        print("Car id:", self.id, "final route plan:\n", self.__reloadPlan)


    
