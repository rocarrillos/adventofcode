from csvToList import readToNestedList
from day3puz1 import updateBoard, processWire
dataList = []
radius = 10000

dataList = []
readToNestedList('day3.csv', dataList)

mapArray = []
mapRow = ['.'] * 2 * radius
for i in range(2 * radius):
    mapArray.append(mapRow[:])

def checkIntersects(circuit, position, intersections, distance):
    if circuit[position[0]][position[1]] == 'X':
        intersections[position] += distance

for i in range(len(dataList)):
    processWire(mapArray, dataList[i], (radius, radius), str(i))

def findIntersections():
    intersections = []
    position = (radius, radius)
    for i in range(0, radius * 2):
        if i % (radius / 5) == 0:
            print('%s percent done building' %(i/(radius / 50)))
        for j in range(0, radius * 2):
            if mapArray[i][j] == 'X':
                intersections.append((i, j))
    return intersections

intersectionsList = findIntersections()
intersectionsDict = dict()
for item in intersectionsList:
    intersectionsDict[item] = 0

def followWire(circuit, wire, position, number):
    distance = [0]
    try:
        for segment in wire:
            if segment[0] == 'U':
                for i in range(int(segment[1:])):
                    position = (position[0], position[1] + 1)
                    distance[0] += 1
                    checkIntersects(circuit, position, intersectionsDict, distance[0])
            if segment[0] == 'D':
                for i in range(int(segment[1:])):
                    position = (position[0], position[1] - 1)
                    distance[0] += 1
                    checkIntersects(circuit, position, intersectionsDict, distance[0])
            if segment[0] == 'L':
                for i in range(int(segment[1:])):
                    position = (position[0] - 1, position[1])
                    distance[0] += 1
                    checkIntersects(circuit, position, intersectionsDict, distance[0])
            if segment[0] == 'R':
                for i in range(int(segment[1:])):
                    position = (position[0] + 1, position[1])
                    distance[0] += 1
                    checkIntersects(circuit, position, intersectionsDict, distance[0])
    except IndexError:
        print('IndexError')
        print(position)

def findDistances():
    for i in range(len(dataList)):
        print('following wire %s' %(i))
        followWire(mapArray, dataList[i], (radius, radius), str(i))

findDistances()
sorted_distances = sorted(intersectionsDict.items(), key=lambda kv: kv[1])
print(sorted_distances[0])