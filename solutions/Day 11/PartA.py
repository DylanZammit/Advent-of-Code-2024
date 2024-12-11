from utils import *
from aocd import get_data, submit

year, day = 2024, 11

dat = get_data(year=year, day=day, block=True)

dat2 = '''125 17'''

dat = list(parse(dat, ints)[0])
print(truncate(dat, 80))

def split_num(n):
    n_digits = int(1+log10(n)) / 2
    return int(n // 10 ** n_digits), int(n % 10 ** n_digits)

n_blinks = 25
for blink in range(n_blinks):
    i = 0
    while True:
        stone = dat[i]
        if stone == 0:
            dat[i] = 1
        elif (n_digits := int(log10(stone)) + 1) % 2 == 0:
            s1, s2 = split_num(stone)
            dat.insert(i, s1)
            dat.insert(i+1, s2)
            del dat[i + 2]
            i += 1
        else:
            dat[i] *= 2024
        i += 1
        if i == len(dat):
            break

out = len(dat)
print(out)
submit(out, part="a", day=day, year=year)
