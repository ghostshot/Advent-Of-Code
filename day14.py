"""
AdventOfCode.com
Day 14: Reindeer Olympics
"""

def distanceFlown(speed, sprint, rest, time):
    completed_sprints = time // (sprint + rest)
    current_interval = time % (sprint + rest)
    current_sprint = 0
    
    if current_interval >= sprint:
        completed_sprints += 1
    else:
        current_sprint = speed * current_interval

    distance = (completed_sprints * sprint * speed) + current_sprint
    return distance
    
    
def winnerDist(filename, seconds):
    fin = open(filename, 'r')

    racers = {}

    for line in fin:
        line = line.split()

        speed, sprint, rest = int(line[3]), int(line[6]), int(line[-2])

        racers[line[0]] = distanceFlown(speed, sprint, rest, seconds)

    winner = max(racers, key=racers.get)
    return winner, racers[winner]

def winnerPts(filename, seconds):
    fin = open(filename, 'r')

    racers = {}
    for line in fin:
        line = line.split()
        racers[line[0]] = int(line[3]), int(line[6]), int(line[-2])

    positions = {}
    points = {}
    for reindeer in racers.keys():
        points[reindeer] = 0

    for t in range(1,seconds+1):
        for reindeer, stats in racers.items():
            positions[reindeer] = distanceFlown(stats[0],stats[1],stats[2], t)

        leaderDist = positions[max(positions, key=positions.get)]
        for reindeer, distance in positions.items():
            if distance == leaderDist:
                points[reindeer] += 1
            
    winner = max(points, key=points.get)
    return winner, points[winner]
        
