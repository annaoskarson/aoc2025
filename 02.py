import re
with open('02.txt') as f:
    ranges = f.read().strip().split(',')

invalid1 = []
invalid2 = []
for r in ranges:
    start, stop = map(int, r.split('-'))
    for code in range(start, stop + 1):
        if re.search(r'^(\d+)\1{1,}$', str(code)):
            invalid2.append(code)
            if re.search(r'^(\d+)\1$', str(code)):
                invalid1.append(code)

print('Advent of Code, day 2, part 1:', sum(invalid1))
print('Advent of Code, day 2, part 2:', sum(invalid2))