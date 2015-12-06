"""
AdventOfCode.com
Day1: Not Quite Lisp
"""

def whatFloor(inputStr, initialFloor=0):
    currentFloor = initialFloor
    for char in inputStr:
        if char == '(':
            #Go up one floor
            currentFloor += 1
        elif char == ')':
            #Go down one floor
            currentFloor -= 1
    return currentFloor


            
def floorPosition(inputStr, targetFloor=-1, initialFloor=0):
    currentFloor = initialFloor
    position = 0
    while currentFloor != targetFloor:
        currentFloor = whatFloor(inputStr[position], currentFloor)
        position += 1
    return position
