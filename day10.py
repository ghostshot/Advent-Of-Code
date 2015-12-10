"""
AdventOfCode.com
Day 10: Elves Look, Elves Say
"""

def look_and_say(inStr):

    group = 0
    counts = []
    digits = []
    currentDigit = None

    for n in inStr:
        if currentDigit is None:
            currentDigit = n
            digits.append(n)
        if n == currentDigit:
            group += 1
        else:
            #finish counting previous digit
            counts.append(str(group))

            #start counting next digit
            digits.append(n)
            group = 1
            currentDigit = n

    counts.append(str(group))

    #create next iteration
    nextList = list(zip(counts, digits))
    
    return ''.join(t[0]+t[1] for t in nextList)


def iterate(inStr='1', iterations=40):

    nextStr = inStr
    while iterations:
        nextStr = look_and_say(nextStr)
        iterations -= 1

    return nextStr
