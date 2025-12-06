with open('06.txt') as f:
    lines = f.read().split('\n')

lines = lines[:-1] # Get rid of a blank line

digits = [ list(map(int, line.split())) for line in lines[:-1] ]
digits = list(map(list, zip(*digits)))

operators = lines[-1].split()

def grandtotal(digits, operators):
    grand = 0
    for i,m in enumerate(operators):
        #print(i, m, digits[i])
        if m == '+':
            this = sum(digits[i])
            grand += this
        elif m == '*':
            this = 1
            for d in digits[i]:
                this = this * d
            grand += this
    return(grand)

print('Advent of code, day 6, part 1:', grandtotal(digits, operators))

# Nu kommer nåt riktigt fult som borde gå att göra betydligt snyggare.
transposed = [ ''.join([line[i] for line in lines[:-1]  if line[i] != ' ']) for i in range(len(lines[0])) ]

digits = []
row = []
for t in transposed:
#    print('t', t)
    if len(t) < 1:
        digits.append(row)
        row = []
    else:
        row.append(int(t))

digits.append(row)

print('Advent of code, day 6, part 2:', grandtotal(digits, operators))