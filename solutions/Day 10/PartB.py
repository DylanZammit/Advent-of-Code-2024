from utils import *
from aocd import get_data, submit

year, day = 2024, 10

dat = get_data(year=year, day=day, block=True)

dat2 = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

dat = Grid(dat)
dat = {k: int(v) for k, v in dat.items()}
print(truncate(dat, 80))

def get_path_score(pos):
    h = dat[pos]
    if h == 9:
        return 1

    out = 0
    for d in directions4:
        next_pos = add2(pos, d)
        if next_pos in dat and dat[next_pos] == h + 1:
            out += get_path_score(next_pos)

    return out


out = sum(get_path_score(pos) for pos, h in dat.items() if h == 0)
print(out)
submit(out, part="b", day=day, year=year)
