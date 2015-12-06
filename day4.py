"""
AdventOfCode.com
Day 4: The Ideal Stocking Stuffer
"""

from hashlib import md5

def getHash(key, number):
    key += str(number)
    return md5(key.encode('ascii')).hexdigest()

def mineAdventCoin(key, numLeadingZeroes=5):
    currentNumber=0
    hashString=''
    targetStr = '0' * numLeadingZeroes
    
    while hashString[:numLeadingZeroes] != targetStr:
        currentNumber += 1
        hashString = getHash(key, currentNumber)

    return currentNumber, hashString
