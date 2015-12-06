"""
AdventOfCode.com
Day 6: Probably a Fire Hazard
"""

import numpy as np

def followInstruction(lights, ins):
    ins = ins.split()
    start = ins[-3].split(',')
    end = ins[-1].split(',')

    x1,y1 = int(start[0]), int(start[1])
    x2,y2 = int(end[0])+1, int(end[1])+1

    if ins[0] == 'toggle':
        #Toggle lights
        #lights[x1:x2,y1:y2] ^= 1
        #increase brightness by 2
        lights[x1:x2,y1:y2] += 2
    elif ins[1] == 'on':
        #Turn lights on
        #lights[x1:x2,y1:y2] = 1
        #increase brightness by 1
        lights[x1:x2,y1:y2] += 1
    elif ins[1] == 'off':
        #turn lights off
        #lights[x1:x2,y1:y2] = 0
        #decrease brightness by one
        lights[x1:x2,y1:y2] -= 1

        #constrain to range [0,1024]
        np.clip(lights, 0, 1024, out=lights)

def installLights(filename):
    inFile = open(filename, 'r')

    lights = np.ndarray((1000,1000), np.int16)
    lights.fill(0)

    for instruction in inFile:
        followInstruction(lights, instruction)
    return lights.sum()
