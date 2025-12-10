import time, os
import itertools

with open('10.txt') as f:
    data = f.read().strip().split('\n')

machines = []
for row in data:
    leds , buttons, jolt = row.split()[0], row.split()[1:-1], row.split()[-1]
    leds = [l == '#' for l in leds[1:-1]]
    buttons = [tuple(map(int, x[1:-1].split(','))) for x in buttons]
    machines.append((leds, buttons, jolt))

def pprint(LEDS, upper = []):
    upper = ''.join(['#' if LED else '.' for LED in upper])
    row = ''.join(['#' if LED else '.' for LED in LEDS])
    os.system('cls' if os.name == 'nt' else 'clear')
    print(upper)
    print(row)
    time.sleep(0.2)

def toggle(state, button):
    newstate = [s for s in state]
    for toggle in button: # toggle according to the button
        newstate[toggle] = not(state[toggle])
    return(newstate)

fewest = []
for i,m in enumerate(machines):
    goal, buttons, _ = m
    done = False
    # Fixa alla kombinationer av knappar, alla längder.
    num = 1
    while not done:
        trythis = itertools.combinations(buttons, num)
        # Testa alla av längd num tills en funkar.
        for run in list(trythis):
            state = [False] * len(goal)
            for b in run:
                state = toggle(state, b)
            if state == goal: # Klart!
                fewest.append(num)
                done = True
                break
        num += 1

print('Advent of code, day 10, part 1:', sum(fewest))
