import csv

orbitsList = list()
with open('day6.csv') as file:
    dataReader = csv.reader(file, delimiter=',')
    for row in dataReader:
        orbitsList.append((row[0], row[1]))

testMasses = ['orbit1', 'orbit2', 'orbit3', 'orbit4', 'orbit5', 'orbit6']
test = {
    'orbit1': {
        'orbit2': {
            'orbit5': {}
        },
        'orbit3': {}
    }, 
    'orbit4': {
        'orbit6': {}
    }
}

def getPath(item, obj):
    # returns the path of it exists, otherwise None
    if item in obj.keys():
        return [item]
    else:
        for key in obj.keys():
            path = getPath(item, obj[key])
            if path is not None:
                return [key] + path


def prettyPrint(obj, numTabs):
    # for visualization purposes
    if len(obj.keys()) == 0:
        print('..' * numTabs + '{}')
    else:
        for key in obj.keys():
            print('..' * numTabs + '%s : {' %key)
            prettyPrint(obj[key], numTabs + 1)
            print('..' * numTabs + '}')

knownMasses = set()
orbitsDict = dict()
def chartOrbits():
    for orbit in orbitsList:
        knownMasses.add(orbit[0])
        knownMasses.add(orbit[1])
        path = getPath(orbit[0], orbitsDict)
        path2 = getPath(orbit[1], orbitsDict)
        if path is None and path2 is None:
            orbitsDict[orbit[0]] = dict()
            orbitsDict[orbit[0]][orbit[1]] = dict()
        elif path is None and path2 is not None:
            orbitsDict[orbit[0]] = dict()
            orbitsDict[orbit[0]][orbit[1]] = orbitsDict[orbit[1]]
            del(orbitsDict[orbit[1]])
        elif path is not None and path2 is None:
            pathEnd = orbitsDict
            for step in path:
                pathEnd = pathEnd[step]
            pathEnd[orbit[1]] = dict()
        elif path is not None and path2 is not None:
            pathEnd = orbitsDict
            for step in path:
                pathEnd = pathEnd[step]
            pathEnd[orbit[1]] = dict()
            pathEnd[orbit[1]] = orbitsDict[orbit[1]]
            del(orbitsDict[orbit[1]])

    

chartOrbits()
prettyPrint(orbitsDict['COM'], 0)
print(sum([len(getPath(mass, orbitsDict)) - 1 for mass in knownMasses]))
