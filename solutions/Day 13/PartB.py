from functools import partial
from utils import *
from aocd import get_data, submit

year, day = 2024, 13

dat = get_data(year=year, day=day, block=True)

dat2 = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''

machines = dat.split('\n\n')
print(truncate(dat, 80))
out = 0
rtol, atol = 0, 0.001
isclose = partial(np.isclose, atol=atol, rtol=rtol)
for machine in machines:
    (i1, i2), (j1, j2), (z1, z2) = parse(machine, ints)
    z1, z2 = z1 + 10000000000000, z2 + 10000000000000
    A = np.array([[i1, i2], [j1, j2]]).T
    a, b = np.linalg.inv(A) @ np.array([z1, z2])


    if isclose(np.round(b), b) and isclose(np.round(a), a) and a > 0 and b > 0:
        a, b = int(np.round(a)), int(np.round(b))
        out += ( a * 3 + b * 1 )

print(out)
submit(out, part="b", day=day, year=year)
