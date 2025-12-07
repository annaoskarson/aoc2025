with open('07.txt') as f:
    lines = f.read().split('\n')

splitters = set() # The splitters.
for r,row in enumerate(lines):
    for c,ch in enumerate(row):
        if ch == '^':
            splitters.add((r,c))
        elif ch == 'S':
            s = (r,c)

def down(beams, rn, splitters):
    splits = 0 # Number of splits.
    newbeams = set() # Make a new set for the next row.
    for beam in beams:
        if (rn, beam) in splitters:
            splits += 1
            newbeams.add(beam-1)
            newbeams.add(beam+1)
        else:
            newbeams.add(beam)
    return(newbeams, splits)

splits = 0
beams = set()
beams.add(s[1]) # The beams om this row.

for r,line in enumerate(lines):
    if '^' in line: # Only here can splits occur.
        beams, newsplits = down(beams, r, splitters)
        splits += newsplits
    
print('Advent of code, day 7, part 1:', splits)

brainz = {} # We need a brainz dictionary remember things.
def trickle(p):
    r,c = p # This is where we are

    if r >= len(lines): # At the bottom
        return(1)

    if (r,c) in brainz: # Get from memory
        return(brainz[(r,c)])

    if (r,c) in splitters: # Split!
        brainz[(r,c)] = trickle((r+1, c-1)) + trickle((r+1, c+1))
    
    else: # No split, continue.
        brainz[(r,c)] = trickle((r+1, c))
    return(brainz[(r,c)])

ans2 = trickle(s)

print('Advent of code, day 7, part 2:', ans2)
