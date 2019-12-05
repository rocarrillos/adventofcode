dataList = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]

def processOpcode(position, valueArray):
    inputLocation1 = valueArray[position + 1]
    inputLocation2 = valueArray[position + 2]
    outputLocation = valueArray[position + 3]
    if valueArray[position] == 1:
        valueArray[outputLocation] = valueArray[inputLocation1] + valueArray[inputLocation2]
        return True
    elif valueArray[position] == 2:
        valueArray[outputLocation] = valueArray[inputLocation1] * valueArray[inputLocation2]
        return True
    elif valueArray[position] == 99:
        return False
    else:
        print('something went wrong')
        return False

def execute(valueArray):
    position = 0
    while position < len(valueArray) and processOpcode(position, valueArray):
        position += 4
    return valueArray[0]

def findMoonLanding():
    for i in range(100):
        for j in range(100):
            dataArray = dataList[:]
            dataArray[1] = i
            dataArray[2] = j
            if execute(dataArray) == 19690720:
                print(i)
                print(j)
    print('completed')


findMoonLanding()