from csvtolist import csv_to_list

class IntcodeComputer:
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.program = []
        self.currentInput = 0
        self.pointer = 0

    def set_inputs_and_program(self, inputs, program):
        """
        Set program inputs and the program to run. 
        Parameters:
            inputs (list(str)): inputs in the order they will be used
            program (list(str)): program to execute
        """
        self.inputs = inputs[:]
        self.program = program[:]

    def handle_opcode(self, opcode, input1, input2, output):
        """
        Internal function. 
        Perform the action specified by opcode with given input and output locations.
        
        Parameters:
        opcode (string): opcode to execute
        input1 (int): index of first input
        input2 (int): index of second input
        output (int): index to place output
        """
        if opcode == '1' or opcode == '01':
            self.program[output] = str(int(self.program[input1]) + int(self.program[input2]))
            self.pointer += 4
        elif opcode == '2' or opcode == '02':
            self.program[output] = str(int(self.program[input1]) * int(self.program[input2]))
            self.pointer += 4
        elif opcode == '3' or opcode == '03':
            self.program[input1] = self.inputs[self.currentInput]
            self.currentInput += 1
            self.pointer += 2
        elif opcode == '4' or opcode == '04':
            print('Output:', self.program[input1])
            self.pointer = -1
        elif opcode == '5' or opcode == '05':
            self.pointer = int(self.program[input2]) if int(self.program[input1]) != 0 else self.pointer + 3
        elif opcode == '6' or opcode == '06':
            self.pointer = int(self.program[input2]) if int(self.program[input1]) == 0 else self.pointer + 3
        elif opcode == '7' or opcode == '07':
            if int(self.program[input1]) < int(self.program[input2]):
                self.program[output] = '1'
            else: 
                self.program[output] = '0'
            self.pointer += 4
        elif opcode == '8' or opcode == '08':
            if int(self.program[input1]) == int(self.program[input2]):
                self.program[output] = '1'
            else: 
                self.program[output] = '0'
            self.pointer += 4
        elif opcode == '99':
            print('Done')
            self.pointer = -1
        else:
            print('Error: invalid opcode', opcode, 'encountered')
            self.pointer = -1

    def exe_instruction(self):
        """
        Internal function. Execute the instruction at the instruction pointer.
        """
        opcode = self.program[self.pointer]
        if len(opcode) == 1: 
            input1 = int(self.program[self.pointer + 1])
            input2 = int(self.program[self.pointer + 2])
            output = int(self.program[self.pointer + 3])
            return self.handle_opcode(opcode, input1, input2, output)
        else:
            while len(opcode) < 5:
                opcode = ''.join(['0', opcode])
            operation = opcode[3:]
            mode3 = opcode[2]
            mode2 = opcode[1]
            mode1 = opcode[0]
            input1 = int(self.program[self.pointer + 1]) if mode3 == '0' else self.pointer + 1
            input2 = int(self.program[self.pointer + 2]) if mode2 == '0' else self.pointer + 2
            output = int(self.program[self.pointer + 3]) if mode1 == '0' else self.pointer + 3
            return self.handle_opcode(operation, input1, input2, output)

    def run_program(self):
        """
        Run the given program with the given inputs.
        """
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
    csv_to_list('day5.csv', dataList)
    intcodeComputer.set_inputs_and_program(['5'], dataList)
    intcodeComputer.run_program()
