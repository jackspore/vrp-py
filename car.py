# project VRP
# class of cars

from nodes import City
from nodes import Depository
from common import *

# import math

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
        self.planLength = 0.0
        Car.numCars += 1
    
    def setBase(self, newBase):
        self.base = newBase

    def setRoutePlan(self, plan):
        self.routePlan = plan

    def evaluatePlan(self):
        self.planLength = 0.0
        curPos = self.__reloadPlan[0]
        for node in self.__reloadPlan:
            self.planLength += calcDistance(pos1=Pos2D(curPos.x, curPos.y), pos2=Pos2D(node.x, node.y))
        return self.planLength

    def insertPlanWithReload(self):
        self.__reloadPlan.clear() #reset current reload plan
        self.loads = self.capacity
        
        for depot in Depository.listDepot:
            if( depot.id == self.base ):
                self.__reloadPlan.append(depot)

        for city in self.routePlan:
            if(city.demand > self.loads):
                print('Car', self.id, 'needs reload for city', city.id)
                depot = self.__seekDepository(city)
                self.__reloadPlan.append(depot)
                self.__reload()
            self.__visitCity(city)
            self.__reloadPlan.append(city)

        return self.__reloadPlan

    def __visitCity(self, city):
        print('Car', self.id, 'visit city', city.id, 'with goods', self.loads)
        self.loads -= city.demand
        city.saved = True

    def __reload(self):
        self.loads = self.capacity

    def __seekDepository(self, curCity):
        __shortest = float('inf')

        for depot in Depository.listDepot:
            length = calcDistance(pos1=Pos2D(curCity.x, curCity.y), pos2=Pos2D(depot.x, depot.y))
            if(length < __shortest):
                __shortest = length
                __depot = depot

        print("Reload at depot:", depot.id, "position:", depot.x, depot.y)
        return depot

    def printFinalRoute(self):
        print("Car id:", self.id, "\nfinal route plan length:", self.planLength)
        for node in self.__reloadPlan:
            if(type(node) == City):
                print(node.id, end=' ')
            else:
                print('(%s)' % node.id, end=' ')
        print('\n**********************')


    
