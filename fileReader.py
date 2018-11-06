# project VRP
# class of problem file reader

from car import Car
from nodes import *
from routePlanner import *

class fileReader:

    def __init__(self):
        pass

    def readFile(self, filename, cars, cities, depots):
        testfile = open(filename, 'r')

        line_citynum = testfile.readline().rstrip()
        citynumInfo = line_citynum.split(' ',1)
        numCities = int(citynumInfo[1])

        line_depotnum = testfile.readline().rstrip()
        depotnumInfo = line_depotnum.split(' ', 1)
        numDepots = int(depotnumInfo[1])

        line_carnum = testfile.readline().rstrip()
        carnumInfo = line_carnum.split(' ', 1)
        numCars = int(carnumInfo[1])

        line_depotID = testfile.readline().rstrip()
        testfile.readline() # blank line

        line_carlist = testfile.readline().rstrip()
        if( line_carlist.split(':', 1)[0] == 'CAR_LIST' ):
            index = 0
            while(index < numCars):
                index += 1
                carInfo = testfile.readline().rstrip().split(' ')
                carId = carInfo[0]
                carCapacity = carInfo[1]
                carBase = carInfo[2]
                car = Car(carId, carBase, carCapacity)
                cars.append(car)

        testfile.readline() # blank line

        line_citylist = testfile.readline().rstrip()
        if( line_citylist.split(':', 1)[0] == 'NODE_LIST' ):
            index = 0
            while(index < numDepots):
                index += 1
                depotInfo = testfile.readline().rstrip().split(' ')
                depotId = depotInfo[0]
                depotX = depotInfo[1]
                depotY = depotInfo[2]
                #depotDemand = depotInfo[3]

                depot = Depository(depotId, depotX, depotY)
                depots.append(depot)

            while(index < numDepots+numCities):
                index += 1
                cityInfo = testfile.readline().rstrip().split(' ')
                cityId = cityInfo[0]
                cityX = cityInfo[1]
                cityY = cityInfo[2]
                demand = cityInfo[3]

                city = City(cityId, cityX, cityY, demand)
                cities.append(city)

        print('done reading file', filename)


