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

print(fair_cost, i)

pos = initial
dist = 2
out = 0
for pos in visited_list:
    curr_cost = visited[pos]
    for d in directions4:
        cheat_pos = add2(pos, mul(d, 2))
        cheat_cost = visited.get(cheat_pos, -100)
        if cheat_cost - curr_cost - 2 >= 100:
            out += 1
print(out)
submit(out, part="a", day=day, year=year)
