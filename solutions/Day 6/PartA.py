from utils import *
from aocd import get_data, submit

year, day = 2024, 6

dat = get_data(year=year, day=day, block=True)

# 41
dat2 = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

dat = Grid(dat)
print(truncate(dat, 30))

pos, dir = next(pos for pos, val in dat.items() if val == '^'), North

tot = 0
visited = {pos}
visited_dir = {(pos, dir)}
while True:
    next_pos = add2(pos, dir)
    if next_pos not in dat:
        break
    if dat[next_pos] != '#':
        pos, dir = next_pos, dir
    else:
        next_dir = make_turn(dir, 'R')
        next_pos = add2(pos, next_dir)
        if next_pos in dat and dat[next_pos] != '#':
            pos, dir = next_pos, next_dir
    visited.add(pos)

tot = len(visited)
print(tot)
submit(tot, part="a", day=day, year=year)
