"""
AdventOfCode.com
Day 3: Perfectly Spherical Houses in a Vacuum
"""

from multiprocessing import Process


def housesVisited(directions):
    currentHouse = startingHouse = (0,0)
    houses = {startingHouse:1}
    
    for instruction in directions:
        if instruction == '^':
            #Move north one house
            currentHouse = (currentHouse[0],currentHouse[1]+1)
            
            if currentHouse in houses:
                #House already visited
                houses[currentHouse] += 1
            else:
                #New House
                houses[currentHouse] = 1
                
        elif instruction == '>':
            #Move east one house
            currentHouse = (currentHouse[0]+1,currentHouse[1])

            if currentHouse in houses:
                #House already visited
                houses[currentHouse] += 1
            else:
                #New House
                houses[currentHouse] = 1

        elif instruction == 'v':
            #Move south one house
            currentHouse = (currentHouse[0],currentHouse[1]-1)

            if currentHouse in houses:
                #House already visited
                houses[currentHouse] += 1
            else:
                #New House
                houses[currentHouse] = 1

        elif instruction == '<':
            #Move west one house
            currentHouse = (currentHouse[0]-1,currentHouse[1])

            if currentHouse in houses:
                #House already visited
                houses[currentHouse] += 1
            else:
                #New House
                houses[currentHouse] = 1
                
    return houses


def divideAndDeliver(directions):

    #Split the work
    santasDirections, robosantasDirections = directions[::2], directions[1::2]

    santasHouses = housesVisited(santasDirections)
    robosantasHouses = housesVisited(robosantasDirections)

    # Merge results (may clobber some gift counts)
    houses = santasHouses.copy()
    houses.update(robosantasHouses)

    return houses
