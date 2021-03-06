# project VRP
# class for route planner

from car import Car
from nodes import City, Depository

import math
import random

class RoutePlanner:
    totalLength = float('inf')
    maxCarLength = float('inf')
    minCarLength = 0.0
    listCar = []
    listCity = []

    def __init__(self, cars, cities):
        RoutePlanner.listCar = cars
        RoutePlanner.listCity = cities
        self.bSingleCarJob = False

    # randomly distribute cities to all cars
    def __distributeCities(self):
        randomcity = random.sample(RoutePlanner.listCity, len(RoutePlanner.listCity))
        idx = 0
        for city in randomcity:
            # first try to distribute cities equaly
            if RoutePlanner.listCar[idx].capacity >= city.demand:
                RoutePlanner.listCar[idx].routePlan.append(city)
                city.saved = True
                idx += 1
                idx %= len(RoutePlanner.listCar)
            else:
            # if not, give city to first able car found
                for car in RoutePlanner.listCar:
                    if car.capacity >= city.demand:
                        car.routePlan.append(city)
                        city.saved = True
                        break

    # distribute cities to nearby depot's car
    def __distributeCityToNearbyDepot(self):
        numDepot = len(Depository.listDepot)
        numCity = len(RoutePlanner.listCity)
        
        for depot in Depository.listDepot:
            depotCar = []
            for car in RoutePlanner.listCar:
                if (car.depot == depot.id):
                    depotCar.append(car)
            
            n = int(numCity / numDepot)
            i = 0
            while (i<=n):
                city = depot.listNearbyCity[i]
                r = random.randint(0, len(depotCar))
                if (depotCar[r].capacity >= city.demand):
                    depotCar[r].routePlan.append(city)
                    city.saved = True
                else:
                    assigned = False
                    for car in depotCar:
                        if (car.capacity >= city.demand):
                            car.routePlan.append(city)
                            city.saved = True
                            assigned = True
                            break
                    if not assigned:
                        for car in RoutePlanner.listCar:
                            if (car.capacity >= city.demand):
                                car.routeplan.append(city)
                                city.saved = True
                i += 1

            for city in RoutePlanner.listCity:
                if (not city.saved):
                    for car in RoutePlanner.listCar:
                        if (car.capacity >= city.demand):
                            car.routeplan.append(city)
                            city.saved = True
                            break

    # mutate a car's route plan by randomly swap its two cities
    def __mutateSingleCar(self, car):
        carPlan = car.routePlan
        a = random.randint(0, len(carPlan)-1)
        b = random.randint(0, len(carPlan)-1)
        tmp = carPlan[a]
        carPlan[a] = carPlan[b]
        carPlan[b] = tmp
        print('MUTATE SINGLE CAR: switch city', a, 'and', b)
        car.setRoutePlan(carPlan)

    # mutate between two cars, swap one city from each
    def __mutateBetweenCars(self, car1, car2):
        plan1 = car1.routePlan
        a = random.randint(0, len(plan1)-1)
        city1 = plan1[a]

        plan2 = car2.routePlan
        b = random.randint(0, len(plan2)-1)
        city2 = plan2[b]

        if( car1.capacity < city2.demand or car2.capacity < city1.demand):
            return # cannot swap cities, return

        plan1[a] = city2
        plan2[b] = city1

        car1.setRoutePlan(plan1)
        car2.setRoutePlan(plan2)

        print('MUTATE BETWEEN CAR', car1.id, 'CITY', city1.id, '&', car2.id, 'CITY', city2.id)

    # evaluate all cars' plans, update current total length if result is better
    # @updateAnyway: always update result when true
    def evaluateCarPlans(self, updateAnyway = False):
        __totalLength = 0.0
        __minCarLength = float('inf')
        __maxCarLength = 0.0
        
        for car in RoutePlanner.listCar:
            car.insertPlanWithReload()
            planLength = car.evaluatePlan()
            print("Car id:", car.id, "travels length:", planLength)
            #print("Route plan:", car.routePlan)

            __totalLength += planLength
            if(planLength < RoutePlanner.minCarLength):
                __minCarLength = planLength
            if(planLength > RoutePlanner.maxCarLength):
                __maxCarLength = planLength

        bBetter = __totalLength < RoutePlanner.totalLength
        if (bBetter or updateAnyway):
            print ('update route plan result')
            RoutePlanner.totalLength = __totalLength
            RoutePlanner.minCarLength = __minCarLength
            RoutePlanner.maxCarLength = __maxCarLength
        
        return bBetter

    def __hillClimb(self):
        if (self.bSingleCarJob):
            self.__mutateSingleCar(RoutePlanner.listCar[0])
        else:
            dice = random.randint(0, 100)
            if (dice % 2 == 0):
                c1 = random.randint(0, len(RoutePlanner.listCar)-1)
                c2 = random.randint(0, len(RoutePlanner.listCar)-1)
                self.__mutateBetweenCars(RoutePlanner.listCar[c1], RoutePlanner.listCar[c2])
            else:
                self.__mutateSingleCar(RoutePlanner.listCar[random.randint(0, len(RoutePlanner.listCar)-1)])

        return self.evaluateCarPlans()
    
    def oneCarJob(self, car):
        __tmpListCars = RoutePlanner.listCar
        RoutePlanner.listCar.clear()
        RoutePlanner.listCar.append(car)
        self.bSingleCarJob = True

        self.doJob()

        RoutePlanner.listCar = __tmpListCars
        self.bSingleCarJob = False

    def doJob(self):
        self.kickStart()
        self.printResult()

    def kickStart(self):
        __stepCount = 100
        __stopCount = 0

        self.__distributeCities()

        while(__stepCount > 0):
            __stepCount -= 1

            if (not self.__hillClimb()):
                __stopCount += 1
                if (__stopCount % 100 == 0 and not self.bSingleCarJob):
                    self.__distributeCities() # redistribute cities, jump out local optima

        return __stopCount

    def printResult(self):
        print('*********EVALUATION COMPLETE***********')
        print("Route plan total length:", RoutePlanner.totalLength)
        print("Maximum car length:", RoutePlanner.maxCarLength)
        print("Minimum car length:", RoutePlanner.minCarLength)

        print('Car routes:')
        for car in RoutePlanner.listCar:
            car.printFinalRoute()

    def seekSuitableCar(self, city):
        for car in self.listCar:
            if (car.capacity > city.demand):
                return car

    def isCarSuitable(self, car, city):
        return car.capacity > city.demand

    def findBiggestCar(self):
        cap = 0
        bigCar = Car(0,0,0)
        for car in self.listCar:
            if (car.capacity > cap):
                cap = car.capacity
                bigCar = car
        return bigCar



