import csv

orbitsList = list()
with open('day6.csv') as file:
    dataReader = csv.reader(file, delimiter=',')
    for row in dataReader:
        orbitsList.append((row[0], row[1]))

def getPath(item, obj):
    # returns the path if it exists, otherwise None
    if item in obj.keys():
        return [item]
    else:
        for key in obj.keys():
            path = getPath(item, obj[key])
            if path is not None:
                return [key] + path

knownMasses = set()
orbitsDict = dict()
def chartOrbits():
    for orbit in orbitsList:
        knownMasses.add(orbit[0])
        knownMasses.add(orbit[1])
        path1 = getPath(orbit[0], orbitsDict)
        path2 = getPath(orbit[1], orbitsDict)
        if path1 is None and path2 is None:
            orbitsDict[orbit[0]] = dict()
            orbitsDict[orbit[0]][orbit[1]] = dict()
        elif path1 is None and path2 is not None:
            orbitsDict[orbit[0]] = dict()
            orbitsDict[orbit[0]][orbit[1]] = orbitsDict[orbit[1]]
            del(orbitsDict[orbit[1]])
        elif path1 is not None and path2 is None:
            pathEnd = orbitsDict
            for step in path1:
                pathEnd = pathEnd[step]
            pathEnd[orbit[1]] = dict()
        elif path1 is not None and path2 is not None:
            pathEnd = orbitsDict
            for step in path1:
                pathEnd = pathEnd[step]
            pathEnd[orbit[1]] = dict()
            pathEnd[orbit[1]] = orbitsDict[orbit[1]]
            del(orbitsDict[orbit[1]])

chartOrbits()

santaPath = getPath('SAN', orbitsDict)
youPath = getPath('YOU', orbitsDict)
sharedDistance = 0
for step in santaPath:
    if step in youPath:
        sharedDistance += 1

print(len(santaPath) - 2 * sharedDistance + len(youPath))
