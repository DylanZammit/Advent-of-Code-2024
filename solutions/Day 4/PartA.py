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


dat = Grid(dat)
x, y = dat.width, dat.height
print(truncate(dat, 30))


tot = 0
for pos, v in dat.items():
    if v != 'X':
        continue
    for dir in directions8:
        if 0 <= X_(add2(pos, mul(dir, 3))) <= x-1 and 0 <= Y_(add2(pos, mul(dir, 3))) <= y-1:
            if dat[add2(pos, dir)] == 'M' and dat[add2(pos, mul(dir, 2))] == 'A' and dat[add2(pos, mul(dir, 3))] == 'S':
                tot += 1

print(tot)
submit(tot, part="a", day=day, year=year)
