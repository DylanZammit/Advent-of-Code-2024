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
while (next_pos := add2(pos, dir)) in dat:
    pos, dir = (pos, make_turn(dir, 'R')) if dat[next_pos] == '#' else (next_pos, dir)
    visited.add(pos)

tot = len(visited)
print(tot)
submit(tot, part="a", day=day, year=year)
