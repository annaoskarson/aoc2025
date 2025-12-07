with open('07.txt') as f:
    lines = f.read().split('\n')

splitters = set() # The splitters.
for r,row in enumerate(lines):
    for c,ch in enumerate(row):
        if ch == '^':
            splitters.add((r,c))
        elif ch == 'S':
            s = (r,c)

splits = 0
brainz = {} # We need a brainz dictionary remember things.
def trickle(p):
    global splits
    r,c = p # This is where we are

    if r >= len(lines): # At the bottom
        return(1)

    if (r,c) in brainz: # Get from memory
        return(brainz[(r,c)])

    if (r,c) in splitters: # Split! And we only need to check every other row. :-)
        brainz[(r,c)] = trickle((r+2, c-1)) + trickle((r+2, c+1))
        splits += 1
    
    else: # No split, continue. And we only need to check every other row. :-)
        brainz[(r,c)] = trickle((r+2, c))
    return(brainz[(r,c)])

ans2 = trickle(s)
print('Advent of code, day 7, part 1:', splits)
print('Advent of code, day 7, part 2:', ans2)
