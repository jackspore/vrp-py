from fileReader import fileReader
from car import Car
from nodes import City, Depository
from routePlanner import RoutePlanner

reader = fileReader()

listCars = []
listCities = []
listDepots = []

reader.readFile("10_2_3.txt", listCars, listCities, listDepots)

planner = RoutePlanner(listCars, listCities)
#planner.doJob()
planner.oneCarJob(listCars[0])

print('END')
