#import os, time

with open('05.txt') as f:
    data = f.read().strip().split('\n')

freshlist = []
ids = []
for d in data:
    if d == '':
        continue
    if '-' in d:
        first,last = map(int, d.split('-'))
        freshlist.append((first,last))
    else:
        ids.append(int(d))
fresh = 0
for i in ids:
    for fl in freshlist:
        if i in range(fl[0],fl[1]+1):
            fresh += 1
            break

print('Advent of Code, day 5, part 1:', fresh)

freshlist = sorted(freshlist)

newlist = []
def compress(freshlist):
    global newlist
    if len(freshlist) < 2:
        newlist.extend(freshlist)
        return()

    [first, second] = freshlist[:2]

    if second[0] <= first[1] <= second[1]:
        collapsed = (first[0], second[1])
        newlist.append(compress([collapsed] + freshlist[2:]))

    elif first[1] > second[1]:
        collapsed = (first[0], first[1])
        newlist.append(compress([collapsed] + freshlist[2:]))

    else:
        newlist.append(first)
        newlist.append(compress([second] + freshlist[2:]))

compress(freshlist)

# Get rid of some None in the list ...
howmany = sum((fl[1] - fl[0] +1) for fl in newlist if fl)

print('Advent of Code, day 5, part 2:', howmany)