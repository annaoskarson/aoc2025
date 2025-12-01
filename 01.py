data = [r.strip() for r in open('01.txt')]
dial = 50

p1 = 0
for r in data:
    d, a = r[0], int(r[1:]) * (-1 if r[0] == 'L' else 1)
    dial = (dial + a) % 100
    if dial == 0: p1 += 1
print('Advent of code 2025, day 1, part 1:', p1)

dial = 50
p2 = 0
for r in data:
    d, a = r[0], int(r[1:]) * (-1 if r[0] == 'L' else 1)
    for _ in range(abs(a)):
        dial = (dial + (-1 if a<0 else 1)) % 100
        if dial == 0: p2 += 1
print('Advent of code 2025, day 1, part 2:', p2)
