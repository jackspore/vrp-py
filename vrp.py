from fileReader import fileReader
from car import Car
from nodes import City, Depository
from routePlanner import RoutePlanner

reader = fileReader()

listCars = []
listCities = []
listDepots = []

fileToRead = input('input filename to read:')
reader.readFile(fileToRead, listCars, listCities, listDepots)

# for each depot, make a sorted list of cities by distance to it
for depot in listDepots:
    depot.sortNearbyCity()

planner = RoutePlanner(listCars, listCities)
planner.doJob()
#planner.oneCarJob(listCars[0])

print('END')
