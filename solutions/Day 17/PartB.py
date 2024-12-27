import sys

from utils import *
from aocd import get_data, submit

year, day = 2024, 17

dat = get_data(year=year, day=day, block=True)

# 117440
dat2 = '''Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0'''

print(truncate(dat, 80))
(A,), (B,), (C,), _, (*program,) = parse(dat, ints)

print(A, B, C, program)


@cache
def part_prog(A):
    B = A % 8
    B = B ^ 5
    C = A >> B
    B = B ^ C
    B = B ^ 6
    return B % 8

@cache
def compute(A):
    out = []
    while A != 0:
        out.append(part_prog(A))
        A = A >> 3
    return out

n = len(program)
min_A = 105690555219968 #2 ** (3 * (n - 1))
max_A = 105759274696704
# 105982440168042  # too high


A_bounds = [(min_A, 105982440168042)]
M = 12

for m in range(M, -1, -1):
    valid = False
    new_A_bounds = []
    for min_A, max_A in A_bounds:
        A = min_A
        while A < max_A:
            res = compute(A)
            valid_idx = m + 1
            if not valid and program[valid_idx] == res[valid_idx]:
                new_min_A = A
                valid = True

            if valid and program[valid_idx] != res[valid_idx]:  # might not be closeD
                new_A_bounds.append((new_min_A, A))
                valid = False

            if program == res:
                print('FOUND <', '-' * 30)
                print(A)
                sys.exit(0)
                break
            A += (8 ** m)
    if valid:
        new_A_bounds.append((new_min_A, A))
        valid = False

    A_bounds = new_A_bounds
    print(A, res, program, m)
