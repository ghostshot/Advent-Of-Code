"""
AdventOcCode.com
Day 13: Knights of the Dinner Table
"""

from itertools import permutations

def buildGraph(filename):
    fin = open(filename, 'r')

    attendees = {}
    
    for line in fin:
        lineList = line.strip()
        lineList = lineList.split()
        
        if attendees.get(lineList[0]) is None:
            attendees[lineList[0]] = {}
        if lineList[2] == 'gain':
            attendees[lineList[0]][lineList[-1][0:-1]] = int(lineList[3])
        else:
            attendees[lineList[0]][lineList[-1][0:-1]] = -int(lineList[3])

    return attendees

def addMyself(attendeeGraph):
    myHappinessScore = 0

    myRatings = {}
    for k,v in attendeeGraph.items():
        v['Me'] = 0
        myRatings[k] = 0

    attendeeGraph['Me'] = myRatings
        
    return attendeeGraph

def arrangeTable(filename, addMe=False):
    attendees = buildGraph(filename)

    if addMe:
        attendees = addMyself(attendees)

    bestTable = None
    bestHappiness = None

    for table in permutations(attendees.keys()):
        cTable = list(table)
        cTable.append(cTable[0])

        happiness = 0
        for person in range(len(cTable)-1):
            happiness += attendees[cTable[person]][cTable[person+1]]
        for person in range(1,len(cTable)):
            happiness += attendees[cTable[person]][cTable[person-1]]

        if bestHappiness == None:
            bestHappiness = happiness
            bestTable = cTable[0:4]
        elif happiness > bestHappiness:
            bestHappiness = happiness
            bestTable = cTable[0:4]

    return bestHappiness
