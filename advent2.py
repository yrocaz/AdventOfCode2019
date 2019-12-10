# Advent of Code day 2
# https://adventofcode.com/2019/day/2

# import requests
# from bs4 import BeautifulSoup
# JK - "Puzzle inputs differ by user.  Please log in to get your puzzle input."
# response = requests.get("https://adventofcode.com/2019/day/2/input") #inputs
# html_soup = BeautifulSoup(response.text, 'html.parser')

inputs_ = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,9,23,1,23,9,27,1,10,27,31,1,13,31,35,1,35,10,39,2,39,9,43,1,43,13,47,1,5,47,51,1,6,51,55,1,13,55,59,1,59,6,63,1,63,10,67,2,67,6,71,1,71,5,75,2,75,10,79,1,79,6,83,1,83,5,87,1,87,6,91,1,91,13,95,1,95,6,99,2,99,10,103,1,103,6,107,2,6,107,111,1,13,111,115,2,115,10,119,1,119,5,123,2,10,123,127,2,127,9,131,1,5,131,135,2,10,135,139,2,139,9,143,1,143,2,147,1,5,147,0,99,2,0,14,0"
# test
# inputs_ = "1,0,0,0,99"
inputs = [int(x) for x in inputs_.split(',')]

def Intcode(p1, p2):
    inputs[1] = p1
    inputs[2] = p2
    instruction = 4
    for opcode in range(0, len(inputs), instruction):
        if inputs[opcode] == 99: # ends program
            break
        else: 
            param1 = inputs[opcode + 1]
            param2 = inputs[opcode + 2]
            param3 = inputs[opcode + 3]
            if inputs[opcode] == 1: # adds together numbers read from two positions and stores the result in a third position. 
                inputs[param3] = inputs[param1] + inputs[param2]
            elif inputs[opcode] == 2: # works exactly like opcode 1, except it multiplies the two inputs instead of adding them
                inputs[param3] = inputs[param1] * inputs[param2]
    return inputs[0]

# to get part1 solution:
# replace position 1 with the value 12 and replace position 2 with the value 2
# Intcode(12, 2)
# print(inputs[0])

def GravityAssist(noun, verb):
    inputs = [int(x) for x in inputs_.split(',')]
    Intcode(noun, verb)


combos = [(noun, verb) for noun in range(100) for verb in range(100)]
count = 0
output = 19690720
for noun, verb in combos:
    GravityAssist(noun, verb)
    if inputs[0] == output:
        print(f'FOUND IT: {noun} and {verb}!\n{100 * noun + verb}')
        break
    else:
        count += 1
        print(f'Attempt {count} of {len(combos)}')
        inputs = [int(x) for x in inputs_.split(',')]


# part1 notes ###
# first attempt : it's not 1
# forgot inputs[oppcode], just had "if oppcose ==..."
# second attempt: it's not 1 again...
# fixed range() to start @ 0
# still getting 1...
# tested using problem example: inputs[oppcode + 3] = ... was giving me that value, 
# but not replacing that vale with the operation, so I had to wrap it inside another
# inputs to replace that value as index
# eg: inputs[oppcode + 3] = inputs[oppcode + 1] + inputs[oppcode + 2]
#              3          =         1           +       2
# insetad I want:
# inputs[inputs[oppcode + 3]] = inputs[oppcode + 1] + inputs[oppcode + 2]
#       inputs[3]         =         1           +       2
## FML its not 152.
# ok - had to break out if oppcode == 99 before trying anythign else.
# renamed oppcodes not to have to keep repeating them.

