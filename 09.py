with open('09.txt') as f:
    lines = f.read().strip().split('\n')

red = set()
rmax, cmax = 0, 0
s = []
for line in lines:
    c,r = map(int, line.split(','))
    red.add((c,r))
    rmax = max(rmax, r)
    cmax = max(cmax, c)
    s.append((c,r))

def pprint(red, green):
    image = '\n'
    for r in range(-2, rmax+2):
        for c in range(-1, cmax+2):
            if (c,r) in red:
                image += '#'
            elif (c,r) in green:
                image += 'X'
            else:
                image += '.'
        print(image)
        image = ''
    print(image)

def largest(tiles, part2=False, seen = set()):
    largest = 0
    for t1 in tiles:
        for t2 in tiles:
            if not part2:
                area = (abs(t1[0] - t2[0])+1) * (abs(t1[1] - t2[1])+1)
                largest = max(largest, area)
            if part2:
                cl, ch = min(t1[0], t2[0]), max(t1[0], t2[0])
                rl, rh = min(t1[1], t2[1]), max(t1[1], t2[1])

                rectangle = set([(c,r) for r in range(rl, rh+1) for c in range(cl, ch+1)])
                if rectangle.issubset(seen):
                    largest = max(largest, len(rectangle))
            
    return(largest)

print('Advent of code, day 9, part 1:', largest(red))
