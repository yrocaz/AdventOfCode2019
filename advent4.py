# Advent of Code day 4
# https://adventofcode.com/2019/day/4

# Part 1:
# How many different passwords within the range given in your puzzle input meet these criteria?

input = [271973, 785962] # 271973-785961(+1)

# conditions:
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

multis = []
def part1(input1, input2):
    pw_count1 = 0
    for attempt in range(input1, input2):
        pw = [int(x) for x in str(attempt)]
        if len(set(pw)) <= 5:                                      # @ least 1 doubled digit
            if any(sum(1 for _ in g) > 1 for _, g in groupby(pw)): # ensures it's adjacent
                if pw[0] <= pw[1]:                                 # equal and/or ascending
                    if pw[1] <= pw[2]:
                        if pw[2] <= pw[3]:
                            if pw[3] <= pw[4]:
                                if pw[4] <= pw[5]:
                                    pw_count1 += 1
                                    multis.append(pw)
    return pw_count1

part1(input[0], input[1])

### part 2
'''An Elf just remembered one more important detail: 
   the two adjacent matching digits are not part of 
   a larger group of matching digits.'''

def part2(multis):
    pw_count2 = 0
    for pw in multis:
        digits = set(pw)
        counts = [pw.count(i) for i in digits]
        if 2 in counts:
            pw_count2 += 1
    return pw_count2

part2(multis)
