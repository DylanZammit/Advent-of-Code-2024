from utils import *
from aocd import get_data, submit

year, day = 2024, 14

dat = get_data(year=year, day=day, block=True)

dat2 = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''

dat = parse(dat, ints)
print(truncate(dat, 80))

out = 0
n = 100
w, h = 101, 103
quads = [0, 0, 0, 0]
for px, py, vx, vy in dat:
    px2, py2 = ( px + vx * n ) % w, ( py + vy * n ) % h
    quads[int(px2 < w // 2) + 2 * int(py2 < h // 2)] += 1

out = prod(quads)
print(out)
submit(out, part="a", day=day, year=year)
