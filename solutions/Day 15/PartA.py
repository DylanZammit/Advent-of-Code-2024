from utils import *
from aocd import get_data, submit

year, day = 2024, 15

dat = get_data(year=year, day=day, block=True)


# 10092
dat2 = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''


# 2028
dat2 = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<'''

dat, dirs = dat.split('\n\n')
grid = Grid(dat)
dirs = [arrow_direction[d] for d in dirs.replace('\n', '')]

print(truncate(dat, 80))
print(truncate(grid, 80))
print(truncate(dirs, 80))
print('=' * 80)

curr_pos = next(k for k, v in grid.items() if v == '@')
out = 0

for d in dirs:

    next_pos = add2(curr_pos, d)
    if grid[next_pos] == '#':
        continue

    if grid[next_pos] == '.':
        grid[curr_pos] = '.'
        grid[next_pos] = '@'
        curr_pos = next_pos
        continue

    n = 1
    while grid[add2(curr_pos, mul(d, n))] == 'O':
        n += 1

    if grid[(non_box := add2(curr_pos, mul(d, n)))] == '#':
        continue

    grid[non_box] = grid[next_pos]

    grid[curr_pos] = '.'
    grid[next_pos] = '@'
    curr_pos = next_pos

grid.print()
out = sum(X_(pos) + 100 * Y_(pos) for pos, v in grid.items() if v == 'O')
print(out)

submit(out, part="a", day=day, year=year)
