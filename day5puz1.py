from csvtolist import csv_to_list

dataList = []
csv_to_list('day5.csv', dataList)

def handleOpcode(opCode, input1, input2, output, program): 
    if opCode == '1' or opCode == '01':
        program[output] = str(int(program[input1]) + int(program[input2]))
        return 4
    if opCode == '2' or opCode == '02':
        program[output] = str(int(program[input1]) * int(program[input2]))
        return 4
    if opCode == '3' or opCode == '03':
        # special case
        program[input1] = '1'
        return 2
    if opCode == '4' or opCode == '04':
        print(program[input1])
        return 2
    if opCode == '99':
        print('Done')
        return 0
    else:
        print('something went wrong')
        return 0

def parseIndex(idx, program):
    opCode = program[idx]
    if len(opCode) == 1: 
        inputLocation1 = int(program[idx + 1])
        inputLocation2 = int(program[idx + 2])
        outputLocation = int(program[idx + 3])
        return handleOpcode(opCode, inputLocation1, inputLocation2, outputLocation, program)
    else:
        while len(opCode) < 5:
            opCode = ''.join(['0', opCode])
        operation = opCode[3:]
        mode3 = opCode[2]
        mode2 = opCode[1]
        mode1 = opCode[0]
        inputLocation1 = int(program[idx + 1]) if mode3 == '0' else idx + 1
        inputLocation2 = int(program[idx + 2]) if mode2 == '0' else idx + 2
        outputLocation = int(program[idx + 3]) if mode1 == '0' else idx + 3
        return handleOpcode(operation, inputLocation1, inputLocation2, outputLocation, program)

def execute1():
    i = 0
    while i < len(dataList):
        delta = parseIndex(i, dataList)
        if delta == 0:
            break
        i += delta
