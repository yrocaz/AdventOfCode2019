# Advent of Code Day 5
# https://adventofcode.com/2019/day/5

# Part 1: After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program produce? 
# Part 2: What is the diagnostic code for system ID 5?

diagnostic_ = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,45,16,225,2,65,191,224,1001,224,-3172,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,1102,90,55,225,101,77,143,224,101,-127,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1102,52,6,225,1101,65,90,225,1102,75,58,225,1102,53,17,224,1001,224,-901,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1002,69,79,224,1001,224,-5135,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,102,48,40,224,1001,224,-2640,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1101,50,22,225,1001,218,29,224,101,-119,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1101,48,19,224,1001,224,-67,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1101,61,77,225,1,13,74,224,1001,224,-103,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,28,90,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,8,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,389,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,434,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,449,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,464,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,479,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,539,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,554,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,569,1001,223,1,223,107,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,1107,677,677,224,102,2,223,223,1005,224,644,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226"
diagnostic = [int(x) for x in diagnostic_.split(',')]

# Instruction class for counts
class Instruction(object):
    def __init__(self):
        count = 0

# instruction = 0 # container for instruction increases
def OpcodeMode(opcode, opcodes, mode1=None, mode2=None, mode3=None):
    # paramter modes
    if mode1 == None or mode1 == 0:     
        param1 = diagnostic[opcodes + 1]    # position mode - value @ the position referenced
    else:
        param1 = opcodes + 1                # immediate mode - value @ that position
    if mode2 == None or mode2 == 0:
        param2 = diagnostic[opcodes + 2]
    else:
        param2 = opcodes + 2
    try:
        if mode3 == None or mode3 == 0:
            param3 = diagnostic[opcodes + 3]
        else:
            param3 = opcodes + 3
    except:
        pass

    # opcodes
    if opcode == 1: # adds together numbers read from two positions and stores the result in a third position. 
        diagnostic[param3] = diagnostic[param1] + diagnostic[param2]
        Instruction.count += 4
    elif opcode == 2: # works exactly like opcode 1, except it multiplies the two inputs instead of adding them
        diagnostic[param3] = diagnostic[param1] * diagnostic[param2]
        Instruction.count += 4
    elif opcode == 3: # takes a single integer as input and saves it to the position given by its only parameter
        diagnostic[param1] = int(input(">>>\ngive us the ID of the system to test \n>>> "))
        Instruction.count += 2
    elif opcode == 4: # outputs the value of its only parameter
        print(diagnostic[param1])
        Instruction.count += 2
    elif opcode == 5:
        if diagnostic[param1] != 0:                 # jump-if-true: if the first parameter is non-zero, 
            Instruction.count = diagnostic[param2]  # it sets the instruction pointer to the value from the second parameter.
        else:
            Instruction.count += 3                  # Otherwise, it does nothing
    elif opcode == 6:
        if diagnostic[param1] == 0:                 # jump-if-false: if the first parameter is zero, 
            Instruction.count = diagnostic[param2]  # it sets the instruction pointer to the value from the second parameter.
        else:
            Instruction.count += 3                  # Otherwise, it does nothing
    elif opcode == 7: 
        if diagnostic[param1] < diagnostic[param2]: # less than: if the first parameter is less than the second parameter,
            diagnostic[param3] = 1                  # it stores 1 in the position given by the third parameter.
        else:
            diagnostic[param3] = 0                  # Otherwise, it stores 0.
        Instruction.count += 4
    elif opcode == 8:
        if diagnostic[param1] == diagnostic[param2]: # equals: if the first parameter is equal to the second parameter, 
            diagnostic[param3] = 1                   # it stores 1 in the position given by the third parameter.
        else:
            diagnostic[param3] = 0                   # Otherwise, it stores 0.
        Instruction.count += 4

def Intcode():
    Instruction.count = 0
    for _ in range(0, len(diagnostic)):
        opcodes = Instruction.count
        opcode = diagnostic[opcodes]
        if opcode == 99: # ends program
            break
        else:
            modes = [int(x) for x in str(opcode)[-3::-1]]
            opcode = int(str(opcode)[-2:])
            try:
                mode1 = modes[0]
            except:
                mode1 = 0
            try:
                mode2 = modes[1]
            except:
                mode2 = 0
            try:
                mode3 = modes[2]
            except:
                mode3 = 0
            print(f'opcode: {diagnostic[opcodes]} / {opcode}, instruction: {Instruction.count}, modes: {mode1}, {mode2}, {mode3}')
            OpcodeMode(opcode, opcodes, mode1, mode2, mode3)
            

Intcode()
# Part 1 - input 1
# Part 2 - input 5
