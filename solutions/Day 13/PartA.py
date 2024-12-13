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
for machine in machines:
    (i1, i2), (j1, j2), (z1, z2) = parse(machine, ints)
    A = np.array([[i1, i2], [j1, j2]]).T
    a, b = np.linalg.inv(A) @ np.array([z1, z2])
    if np.isclose(np.round(b), b) and np.isclose(np.round(a), a) and a > 0 and b > 0 and a <= 100 and b <= 100:
        a, b = int(np.round(a)), int(np.round(b))
        out += ( a * 3 + b * 1 )

print(out)
submit(out, part="a", day=day, year=year)
