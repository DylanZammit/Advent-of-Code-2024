from utils import *
from aocd import get_data, submit

year, day = 2024, 7

dat = get_data(year=year, day=day, block=True)

dat2 = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

dat = parse(dat, ints)
print(truncate(dat, 30))

from itertools import product

tot = 0
for eqn in dat:

    lhs = eqn[0]
    rhs = eqn[1:]

    for op in product(['+', '*'], repeat=len(rhs) - 1):
        val = rhs[0]
        for i, r in enumerate(rhs[1:]):
            if op[i] == '+':
                val += r
            elif op[i] == '*':
                val *= r
        if val == lhs:
            tot += lhs
            break

print(tot)
submit(tot, part="a", day=day, year=year)
