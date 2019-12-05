import csv

dataList = []
with open('day5.csv') as file:
    dataReader = csv.reader(file, delimiter=',')
    for row in dataReader:
        for item in row:
            dataList.append(item)

def handleOpcode(pointer, opCode, input1, input2, output, program): 
    if opCode == '1' or opCode == '01':
        program[output] = str(int(program[input1]) + int(program[input2]))
        return pointer + 4
    if opCode == '2' or opCode == '02':
        program[output] = str(int(program[input1]) * int(program[input2]))
        return pointer + 4
    if opCode == '3' or opCode == '03':
        # special case
        program[input1] = '5'
        return pointer + 2
    if opCode == '4' or opCode == '04':
        print('output')
        print(program[input1])
        return pointer + 2
    if opCode == '5' or opCode == '05':
        return int(program[input2]) if int(program[input1]) != 0 else pointer + 3
    if opCode == '6' or opCode == '06':
        return int(program[input2]) if int(program[input1]) == 0 else pointer + 3
    if opCode == '7' or opCode == '07':
        if int(program[input1]) < int(program[input2]):
            program[output] = '1'
        else: 
            program[output] = '0'
        return pointer + 4
    if opCode == '8' or opCode == '08':
        if int(program[input1]) == int(program[input2]):
            program[output] = '1'
        else: 
            program[output] = '0'
        return pointer + 4
    if opCode == '99':
        print('Done')
        return -1
    else:
        print('something went wrong')
        print(pointer, program[pointer])
        return -1

def parseIndex(pointer, program):
    opCode = program[pointer]
    if len(opCode) == 1: 
        inputLocation1 = int(program[pointer + 1])
        inputLocation2 = int(program[pointer + 2])
        outputLocation = int(program[pointer + 3])
        return handleOpcode(pointer, opCode, inputLocation1, inputLocation2, outputLocation, program)
    else:
        while len(opCode) < 5:
            opCode = ''.join(['0', opCode])
        operation = opCode[3:]
        mode3 = opCode[2]
        mode2 = opCode[1]
        mode1 = opCode[0]
        inputLocation1 = int(program[pointer + 1]) if mode3 == '0' else pointer + 1
        inputLocation2 = int(program[pointer + 2]) if mode2 == '0' else pointer + 2
        outputLocation = int(program[pointer + 3]) if mode1 == '0' else pointer + 3
        return handleOpcode(pointer, operation, inputLocation1, inputLocation2, outputLocation, program)

def execute():
    pointer = 0
    while pointer < len(dataList):
        try:
            pointer = parseIndex(pointer, dataList)
            if pointer == -1:
                break
        except IndexError:
            break

execute()