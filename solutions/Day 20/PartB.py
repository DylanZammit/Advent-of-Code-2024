from utils import *
from aocd import get_data, submit

year, day = 2024, 20

dat = get_data(year=year, day=day, block=True)
dat2 = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''

truncate(dat, 80)

grid = Grid(dat, directions=directions4)
initial = next(k for k, v in grid.items() if v == 'S')
goal = next(k for k, v in grid.items() if v == 'E')

visited = {}
visited_list = []
pos = initial
i = 0
while grid[pos] != 'E':
    visited[pos] = i
    visited_list.append(pos)
    pos = next(neighbour for neighbour in grid.neighbors(pos) if neighbour not in visited and grid[neighbour] != '#')
    i += 1

visited[goal] = i
visited_list.append(goal)
fair_cost = len(visited) - 1


pos = initial
dist = 20
out = 0
min_improvement = 100
n = len(visited_list)
for i, pos in enumerate(visited_list):
    curr_cost = visited[pos]
    for cheat_pos, val in grid.items():
        if val in '#S' or (d := taxi_distance(pos, cheat_pos)) > dist:
            continue

        cheat_cost = visited[cheat_pos]
        if cheat_cost - curr_cost - d >= min_improvement:
            out += 1

print(out)
submit(out, part="b", day=day, year=year)
