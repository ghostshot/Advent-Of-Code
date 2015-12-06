"""
AdventOfCode.com
Day 5: Doesn't He Have Intern-Elves For This?
"""

import re

def isNiceOLD( inString ):
    #1. Contains 3+ vowels (aeiou)
    if re.search('([aeiou]).*[aeiou].*[aeiou]', inString) is None:
        return False

    #2. Contains 1+ letter twice in a row
    if re.search('(\\w)\\1+', inString) is None:
        return False
    
    #3. Does NOT contain substrings 'ab', 'cd', 'pq', or 'xy'
    if re.search('ab|cd|pq|xy', inString) is not None:
        return False

    return True

def isNice( inString ):
    #1. Contains a pair of any two letters appearing at least twice
    if re.search('(.{2}).*\\1', inString) is None:
        return False

    #2. Contains at least one letter which repeats with exactly one letter between them
    if re.search('(\w).\\1', inString) is None:
        return False

    return True


def checkList(filePath):
    inFile = open(filePath, 'r')
    
    niceCount=0
    for line in inFile:
        if isNice(line):
            niceCount += 1

    checkTwice=0
    inFile.seek(0)
    for line in inFile:
        if isNice(line):
            checkTwice += 1

    if niceCount == checkTwice:
        return niceCount
    else:
        return -1
