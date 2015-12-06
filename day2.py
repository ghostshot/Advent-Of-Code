"""
AdventOfCode.com
Day2: I Was Told There Would Be No Math
"""

from numpy import loadtxt

def surfaceAreaAndSlack(l, w, h):
    A = (l*w)
    B = (w*h)
    C = (l*h)

    return 2*A + 2*B + 2*C, min(A,B,C)

def paperNeeded(inFile='day2input.txt' ):
    presents = loadtxt(inFile, int, delimiter='x')

    sqFeet = 0

    for present in presents:
        sqFeet += sum(surfaceAreaAndSlack(present[0],present[1], present[2]))

    return sqFeet

def ribbonNeeded(inFile='day2input.txt'):
    presents = loadtxt(inFile, int, delimiter='x')

    feetOfRibbon = 0

    for present in presents:
        minDims = present.argsort()[:2]
        wrappingLength = (2* present[minDims[0]]) + (2*present[minDims[1]])
        bowLength = present.prod()
        feetOfRibbon += (wrappingLength + bowLength)

    return feetOfRibbon
        
