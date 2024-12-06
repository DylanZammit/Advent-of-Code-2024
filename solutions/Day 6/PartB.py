from utils import *
from aocd import get_data, submit

year, day = 2024, 6

# 1972
puzzle = get_data(year=year, day=day, block=True)

# 6
# {(3, 8), (7, 7), (1, 8), (7, 9), (6, 7), (3, 6)}
puzzle2 = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''


def is_loop(pos, dir, visited_dir: set = None):
    visited_dir = visited_dir or set()
    dat_loop = dict(dat)
    next_pos = add2(pos, dir)

    dat_loop[next_pos] = '#'
    for p, _ in visited_dir:
        dat_loop[p] = '.'  # not sure why needed....probably deepcopy stuff? deepcopy too slow!

    while (next_pos := add2(pos, dir)) in dat_loop:
        pos, dir = (pos, make_turn(dir, 'R')) if dat_loop[next_pos] == '#' else (next_pos, dir)
        if (pos, dir) in visited_dir:
            return True
        visited_dir.add((pos, dir))

    return False


def get_route(pos, dir):
    visited = {pos}
    visited_dir = {(pos, dir)}
    obstacles = set()
    while (next_pos := add2(pos, dir)) in dat:
        if dat[next_pos] != '#':
            if next_pos not in obstacles and is_loop(pos, dir, visited_dir.copy()):
                obstacles.add(next_pos)

        pos, dir = (pos, make_turn(dir, 'R')) if dat[next_pos] == '#' else (next_pos, dir)

        visited.add(pos)
        visited_dir.add((pos, dir))
    print(f'Visited {len(visited)}')
    return obstacles


dat = Grid(puzzle)
print(truncate(dat, 30))

obstacles = get_route(next(pos for pos, val in dat.items() if val == '^'), North)
tot = len(obstacles)
print(tot)
submit(tot, part="b", day=day, year=year)
