with open('03.txt') as f:
    banks = f.read().strip().split('\n')

def largest(digits, length):
    h = max([int(d) for d in digits[:len(digits)-(length-1)]]) # Find the highest number in the allowed range.
    i = digits.index(str(h)) # Place of the leftmost of the highest number in the allowed range.
    return(str(h),digits[i+1:]) # Return the next battery and rest of the bank.

def jolting(banks, length = 2):
    joltages = []
    for bank in banks:
        jolts = ''
        left = length
        while left > 0: # Process the whole bank
            h, bank = largest(bank,left)
            jolts += h
            left -= 1
        joltages.append(int(jolts))
    return(sum(joltages))

print('Advent of Code, day 3, part 1:', jolting(banks))
print('Advent of Code, day 3, part 2:', jolting(banks, 12))