"""
AdventOfCode.com
Day 11: Corporate Policy
"""

import re

def isValidPass(password):
    # exactly 8 lowercase letters
    if len(password) != 8 or not password.islower():
        #print('INVALID LENGTH')
        return False
    
    # 1 increasing straight of 3+ letters
    containsStraight = False
    subs = [password[x:x+3] for x in range(6)]
    for s in subs:
        if ord(s[-1]) - ord(s[-2]) == 1 and ord(s[-2]) - ord(s[-3]) == 1:
            # straight found
            containsStraight = True
    if not containsStraight:
        #print('DOES NOT CONTAIN STRAIGHT')
        return False
            
    
    # does not contain letters 'i', 'o', or 'l'
    for c in 'iol':
        if c in password:
            #print('CONTAINS ILLEGAL CHARACTERS')
            return False
    
    # 2+ different non-overlapping pairs of letters
    pairs = re.findall('([a-z])\\1',password)
    if len(set(pairs)) < 2:
        #print('NOT ENOUGH PAIRS')
        return False

    return True

def generateNextPassword(currentPassword):
    curr = list(currentPassword)
    curr.reverse()

    while True:
        for i in range(8):
            curr[i] = chr((((ord(curr[i])-97)+1)%26)+97)
            if curr[i] != 'a':
                # no carry
                break

        candidate = curr
        candidate.reverse()
        newPass = ''.join(candidate)
        
        if isValidPass(newPass):
            return newPass

        curr = list(newPass)
        curr.reverse()
