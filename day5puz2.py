from csvToList import readToList

class IntcodeComputer:
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.program = []
        self.currentInput = 0
        self.pointer = 0

    def set_inputs_and_program(self, inputs, program):
        """Set program inputs and the program to run. 
        
        Parameters:
        inputs (list(str)): inputs in the order they will be used
        program (list(str)): program to execute
        """
        self.inputs = inputs[:]
        self.program = program[:]

    def handle_opcode(self, opCode, input1, input2, output):
        """
        Internal function. 
        Perform the action specified by opCode with given input and output locations.
        
        Parameters:
        opCode (string): opcode to execute
        input1 (int): index of first input
        input2 (int): index of second input
        output (int): index to place output
        """
        if opCode == '1' or opCode == '01':
            self.program[output] = str(int(self.program[input1]) + int(self.program[input2]))
            self.pointer += 4
        elif opCode == '2' or opCode == '02':
            self.program[output] = str(int(self.program[input1]) * int(self.program[input2]))
            self.pointer += 4
        elif opCode == '3' or opCode == '03':
            self.program[input1] = self.inputs[self.currentInput]
            self.currentInput += 1
            self.pointer += 2
        elif opCode == '4' or opCode == '04':
            print('Output:', self.program[input1])
            self.pointer = -1
        elif opCode == '5' or opCode == '05':
            self.pointer = int(self.program[input2]) if int(self.program[input1]) != 0 else self.pointer + 3
        elif opCode == '6' or opCode == '06':
            self.pointer = int(self.program[input2]) if int(self.program[input1]) == 0 else self.pointer + 3
        elif opCode == '7' or opCode == '07':
            if int(self.program[input1]) < int(self.program[input2]):
                self.program[output] = '1'
            else: 
                self.program[output] = '0'
            self.pointer += 4
        elif opCode == '8' or opCode == '08':
            if int(self.program[input1]) == int(self.program[input2]):
                self.program[output] = '1'
            else: 
                self.program[output] = '0'
            self.pointer += 4
        elif opCode == '99':
            print('Done')
            self.pointer = -1
        else:
            print('Error: invalid opcode', opCode, 'encountered')
            self.pointer = -1

    def exe_instruction(self):
        opCode = self.program[self.pointer]
        if len(opCode) == 1: 
            inputLocation1 = int(self.program[self.pointer + 1])
            inputLocation2 = int(self.program[self.pointer + 2])
            outputLocation = int(self.program[self.pointer + 3])
            return self.handle_opcode(opCode, inputLocation1, inputLocation2, outputLocation)
        else:
            while len(opCode) < 5:
                opCode = ''.join(['0', opCode])
            operation = opCode[3:]
            mode3 = opCode[2]
            mode2 = opCode[1]
            mode1 = opCode[0]
            inputLocation1 = int(self.program[self.pointer + 1]) if mode3 == '0' else self.pointer + 1
            inputLocation2 = int(self.program[self.pointer + 2]) if mode2 == '0' else self.pointer + 2
            outputLocation = int(self.program[self.pointer + 3]) if mode1 == '0' else self.pointer + 3
            return self.handle_opcode(operation, inputLocation1, inputLocation2, outputLocation)

    def run_program(self):
        if len(self.program) == 0:
            print('Program is empty!')
        else:
            while self.pointer < len(self.program):
                self.exe_instruction()
                if self.pointer == -1:
                    break

def execute2():
    intcodeComputer = IntcodeComputer()
    dataList = []
    readToList('day5.csv', dataList)
    intcodeComputer.set_inputs_and_program(['5'], dataList)
    intcodeComputer.run_program()
