from utils import *
from itertools import product
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

tot = 0
for lhs, *rhs in dat:

    for ops in product(['+', '*', '||'], repeat=len(rhs) - 1):
        val = rhs[0]
        for op, r in zip(ops, rhs[1:]):
            if op == '+':
                val += r
            elif op == '*':
                val *= r
            elif op == '||':
                val = val * 10 ** (int(log10(r)) + 1) + r
        if val == lhs:
            tot += lhs
            break

print(tot)
submit(tot, part="b", day=day, year=year)
