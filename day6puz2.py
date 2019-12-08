from csvtolist import csv_to_tuple_list
from day6puz1 import getPath, chartOrbits

def execute2():
    orbitsList = list()
    csv_to_tuple_list('day6.csv', orbitsList)
    knownMasses = set()
    orbitsDict = dict()

    chartOrbits(knownMasses, orbitsDict, orbitsList)

    santaPath = getPath('SAN', orbitsDict)
    youPath = getPath('YOU', orbitsDict)
    sharedDistance = 0
    for step in santaPath:
        if step in youPath:
            sharedDistance += 1
    print(len(santaPath) - 2 * sharedDistance + len(youPath))
