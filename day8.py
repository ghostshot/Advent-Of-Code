"""
AdventOfCode.com
Day 8: Matchsticks
"""

import codecs

def getLiteralSize(filename):
    # Return number of characters in string literal
    
    inFile = codecs.open(filename)

    sizeStringCode = []
    for line in inFile:
        sizeStringCode.append( len(line.strip()) )

    inFile.close()

    return sum(sizeStringCode)

def getMemSize(filename):
    # Return number of characters in memory
    
    inFile = codecs.open(filename, encoding='utf-8')

    sizeInMem = []
    for line in inFile:
        sizeInMem.append(len(eval(str(line.strip()))))

    inFile.close()

    return sum(sizeInMem)

def getEncodedSize(filename):
    # Return number of characters in encoded literal string
    
    inFile = open(filename,'r')

    sizeEncoded = []
    encode_dict = {'"': '\\"',
                   '\\': '\\\\'}

    for line in inFile:
        chars = []
        chars.extend(line.strip())

        for i, char in enumerate(chars):
            if encode_dict.get(char) is not None:
                chars[i]=encode_dict[char]

        encodedStr = ''.join(chars)
        encodedStr = '"{}"'.format(encodedStr)
        sizeEncoded.append(len(encodedStr))

    inFile.close()

    return sum(sizeEncoded)


def getSpace(filename='day8input.txt', encodeInput=False):
    if encodeInput == False:
        return getLiteralSize(filename) - getMemSize(filename)
    else:
        return getEncodedSize(filename) - getLiteralSize(filename)
