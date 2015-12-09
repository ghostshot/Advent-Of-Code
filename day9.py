"""
AdventOfCode.com
Day 9: All in a Single Night
"""



from itertools import permutations

def build_graph(filename):
    inFile = open(filename,'r')

    verticies=set()
    edges={}

    for line in inFile:
        split_line = line.split()

        if split_line[0] not in verticies:
            verticies.add(split_line[0])
        if split_line[2] not in verticies:
            verticies.add(split_line[2])

        edge_tuples = []
        for i in permutations([split_line[0],split_line[2]]):
            edge_tuples.append(i)

        edges[edge_tuples[0]] = int(split_line[-1])
        edges[edge_tuples[1]] = int(split_line[-1])


    return verticies, edges


def shortest_path(verts, edges):
    shortest = -1
    for path in permutations(verts):
        nodes = len(path)
        distance = 0

        for x in range(nodes-1):
            edge = (path[x],path[x+1])
            distance += edges[edge]

        if shortest < 0:
            shortest = distance
        elif distance < shortest:
            shortest = distance

    return shortest

def longest_path(verts, edges):
    longest = -1
    for path in permutations(verts):
        nodes = len(path)
        distance = 0

        for x in range(nodes-1):
            edge = (path[x],path[x+1])
            distance += edges[edge]

        if distance > longest:
            longest = distance

    return longest
