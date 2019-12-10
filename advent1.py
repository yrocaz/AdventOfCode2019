# Advent of Code day 2
# https://adventofcode.com/2019/day/1

import math

# wanted to test reading a file line by line. Will use urllib next.
advnt = open('/Users/Home/Documents/advent.txt', 'r')
masses = []

with advnt as m:                 # open the file of masses
    for line in m:
        line = line.rstrip('\n') # strip new line
        masses.append(int(line)) # make int

fuel = []
for i in masses:
    # divide by three, round down, and subtract 2.
    fuel.append(math.floor(i/3) - 2)

extra = [] # contianer for extra fuel needed for the fuel added

for i in fuel:
    xtra = math.floor(i/3) - 2                # same recipe for xtra fuel
    extra.append(xtra)
    while math.floor(xtra/3) - 2 > 0:
        extra.append(math.floor(xtra/3 - 2))  # continue adding fuel for the xtra fuel
        xtra = math.floor(xtra/3 - 2)         # added until what you would add < 0

print(f'The original fuel was {sum(fuel)} and the DiffEQ extra is {sum(extra)}\
    for a total of {sum(fuel) + sum(extra)}')