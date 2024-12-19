from utils import *
from aocd import get_data, submit

year, day = 2024, 17

dat = get_data(year=year, day=day, block=True)

# 4,6,3,5,6,3,5,2,1,0
dat2 = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''

print(truncate(dat, 80))
(A,), (B,), (C,), _, (*program,) = parse(dat, ints)

print(A, B, C, program)

combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C, 7: 7}


def op(x, y):
    global A, B, C, i
    res = None

    if x == 0:
        A = A >> combo[y]
    if x == 1:
        B ^= y
    if x == 2:
        B = combo[y] % 8
    if x == 3 and A != 0:
        i = y - 2
    if x == 4:
        B ^= C
    if x == 5:
        res = combo[y] % 8
    if x == 6:
        B = A >> combo[y]
    if x == 7:
        C = A >> combo[y]
    combo[4] = A
    combo[5] = B
    combo[6] = C
    return res

i = 0
out = []
while i < len(program) - 1:
    res = op(program[i], program[i+1])
    if res is not None:
        out.append(res)
    i += 2

out = ','.join([str(x) for x in out])

print(out)
submit(out, part="a", day=day, year=year)
