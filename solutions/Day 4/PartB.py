from utils import *
from aocd import get_data, submit

year, day = 2024, 4

dat = get_data(year=year, day=day, block=True)

dat2 = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

datspl = dat.split('\n')
x, y = len(datspl[0]), len(datspl)

dat = Grid(dat)
print(truncate(dat, 30))


def is_valid(pos, dir):
    return 0 <= X_(add2(pos, dir)) <= x-1 and 0 <= Y_(add2(pos, dir)) <= y-1


tot = 0
for pos, v in dat.items():
    if v != 'A':
        continue
    if is_valid(pos, NE) and is_valid(pos, SE) and is_valid(pos, SW) and is_valid(pos, NW):
        if {dat[add2(pos, NE)], dat[add2(pos, SW)]} == {'M', 'S'} and {dat[add2(pos, NW)], dat[add2(pos, SE)]} == {'M', 'S'}:
            tot += 1

print(tot)
submit(tot, part="b", day=day, year=year)
