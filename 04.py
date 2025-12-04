import os, time

with open('04.txt') as f:
    image = f.read().strip().split('\n')

rolls = set()
for r,row in enumerate(image):
    for c,char in enumerate(row):
        if char == '@':
            rolls.add((r,c))

def pprint(rolls):
    os.system('cls' if os.name == 'nt' else 'clear')
    image = '\n'
    for r1 in range(r+1):
        for c1 in range(c+1):
            if (r1,c1) in rolls:
                image += '@'
            else:
                image += '.'
        image += '\n'
    print(image)
#    time.sleep(0.0001)

def nbs(rolls, pos):
    r,c = pos
    n = [(r1,c1) for r1 in [r-1, r, r+1] for c1 in [c-1, c, c+1] if (r1,c1) != (r,c) and (r1,c1) in rolls]
    return(len(n))

ans1 = sum(nbs(rolls, roll)<4 for roll in rolls)

print('Advent of Code, day 3, part 1:', ans1)

ans2 = 0
forklifted = True
while forklifted:
    forklifted = False
    for roll in list(rolls):
        if nbs(rolls, roll) < 4:
            rolls.remove(roll)
            forklifted = True
            ans2 += 1
            #pprint(rolls)

print('Advent of Code, day 3, part 2:', ans2)