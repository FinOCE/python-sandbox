# Number of dice
DICE = 4
# Number of rolls per group
ROLLS = 1000
# Number of groups
GROUPS = 1000
# Show stars to represent count
DISPLAY = False

from random import randint

def main():
    highest = {}
    minimum = DICE*1
    maximum = DICE*6
    for i in range(GROUPS):
        count = {}
        for ii in range(ROLLS):
            value = 0
            for i in range(DICE):
                value += randint(1, 6)
            if value not in count:
                count[value] = 1
            else:
                count[value] += 1
        if max(count, key=count.get) not in highest:
            highest[max(count, key=count.get)] = 1
        else:
            highest[max(count, key=count.get)] += 1
    for value in range(minimum, maximum+1):
        if value in highest:
            if DISPLAY:
                print(f"{value:2}: {highest[value] * '*'}")
            else:
                print(f"{value:2}: {highest[value]}")
        else:
            print(f"{value:2}: ")

main()