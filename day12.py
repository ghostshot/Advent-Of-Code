"""
AdventOfCode.com
Day 12: JSAbacusFramework.io
"""

import re
import json

def sumNums(filename):
    fi = open(filename,'r')

    sum = 0
    line = fi.readline()

    nums = re.findall('-?[0-9]+',line)

    for n in nums:
        sum += int(n)


def correctedSum(structure):
    inType = type(structure)
    if inType == int:
        # Base case
        return structure
    elif inType == str:
        return 0
    elif inType == list:
        listSum = 0
        for n in structure:
            listSum += correctedSum(n)
        return listSum
    elif inType == dict:
        if 'red' in structure.values():
            return 0
        dictSum = 0
        for key, val in structure.items():
                dictSum += correctedSum(val)
        return dictSum

def sumJsonFile(filename):
    fi = open(filename,'r')

    doc = json.load(fi)

    return correctedSum(doc)
