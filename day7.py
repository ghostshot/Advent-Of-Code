"""
AdventOfCode.com
Day 7: Some Assembly Required
"""

import functools

wires = {}

@functools.lru_cache()
def wireSignal( wire ):
    #Base Case - Signal Found
    if wire.isdigit():
        return int(wire)

    op = wires[wire].split()
    if 'AND' in op:       # AND Gate
        return wireSignal(op[0]) & wireSignal(op[2])
    elif 'OR' in op:      # OR Gate
        return wireSignal(op[0]) | wireSignal(op[2])
    elif 'LSHIFT' in op:  # LEFT SHIFT
        return wireSignal(op[0]) << wireSignal(op[2])
    elif 'RSHIFT' in op:  # RIGHT SHIFT
        return wireSignal(op[0]) >> wireSignal(op[2])
    elif 'NOT' in op:     #NOT Gate
        return ~wireSignal(op[1])
    else:                 # No operation
        # Recieves signal directly from another wire
        return wireSignal(op[0])

        
def followCircuit(filename, returnWire='a', override=False, overrideWire=('b',46065)):
    inFile = open(filename, 'r')
    
    for line in inFile:
        op, dest = line.split(' -> ')
        wires[dest.strip()] = op

    if override:
        wires[overrideWire[0]] = str(overrideWire[1])
        wireSignal.cache_clear() 
        
    return wireSignal( returnWire )
