with open('11.txt') as f:
    data = f.read().strip().split('\n')

forward = {} # tabell för att gå framåt
for row in data:
    fr, to = row.split(':')
    to = to.strip().split()
    forward[fr] = to

ways = 0
def hittaut(path, goal):
    global ways
    this = path[-1]

    if this == goal: # Framme!
        ways += 1
        return()

    for n in forward[this]: #Testa vägar.
        if not(n in path):
            hittaut(path + [n], goal)

hittaut(['you'], 'out')
print('Advent of code, day 11, part 1:', ways)


mand = ['dac', 'fft']
lookup = {}

def hittaut2(this, goal, passed):

    if this == goal: # Done!
        if passed == 2: # Done and passed.
            return(1)
        return(0) # Done but not passed.

    if (this, passed) in lookup: # Check the memory.
        return(lookup[(this, passed)])

    if this in mand: # Passing a mandatory node.
        passed += 1
    
    lookup[(this, passed)] = 0 # Time for some memory
    for n in forward[this]:
        lookup[(this, passed)] += hittaut2(n, goal, passed)

    return(lookup[(this, passed)])

print('Advent of code, day 11, part 2:', hittaut2('svr', 'out', 0))
