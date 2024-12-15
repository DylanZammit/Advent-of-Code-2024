from utils import *
from aocd import get_data, submit

year, day = 2024, 15

dat = get_data(year=year, day=day, block=True)


# 9021
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

dat2 = '''#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^'''

dat = dat.replace('#', '##')
dat = dat.replace('O', '[]')
dat = dat.replace('.', '..')
dat = dat.replace('@', '@.')

dat, dirs = dat.split('\n\n')
grid = Grid(dat, default = '#')
dirs = [(d, arrow_direction[d]) for d in dirs.replace('\n', '')]

print(truncate(dat, 80))
print(truncate(grid, 80))
print(truncate(dirs, 80))
grid.print()
print('=' * 80)

def pushable_boxes(p1, dir):

    p2 = add2(p1, West) if grid[p1] == ']' else add2(p1, East)

    if grid[p1] == ']':
        p1, p2 = p2, p1

    boxes = {p1, p2}

    p1n, p2n = add2(p1, dir), add2(p2, dir)
    v1n, v2n = grid[p1n], grid[p2n]

    if v1n == '#' or v2n == '#':
        return set()

    if v1n == '.' and v2n == '.':
        return boxes

    b1, b2 = set(), set()

    if v1n in '[]' and not (b1 := pushable_boxes(p1n, dir)):
        return set()

    if v2n in '[]' and not (b2 := pushable_boxes(p2n, dir)):
        return set()

    return boxes | b1 | b2

curr_pos = next(k for k, v in grid.items() if v == '@')
out = 0
side_pos = None
for arr, d in dirs:
    grid[curr_pos] = arr
    next_pos = add2(curr_pos, d)
    if grid[next_pos] == '#':
        continue

    if grid[next_pos] == '.':
        grid[curr_pos] = '.'
        grid[next_pos] = '@'
        curr_pos = next_pos
        continue

    if d in {West, East}:
        n = 1
        while grid[add2(curr_pos, mul(d, n))] in '[]':
            n += 1

        if grid[add2(curr_pos, mul(d, n))] == '#':
            continue

        for nn in range(n, 0, -1):
            p1 = add2(curr_pos, mul(d, nn))
            p2 = add2(curr_pos, mul(d, nn - 1))
            grid[p1] = grid[p2]
    else:
        boxes = pushable_boxes(next_pos, d)
        if not boxes:
            continue

        grid_tmp = grid.copy()
        for box_pos in boxes:
            grid_tmp[box_pos] = '.'

        for box_pos in boxes:
            next_box_pos = add2(box_pos, d)
            grid_tmp[next_box_pos] = grid[box_pos]
        grid = grid_tmp

    grid[curr_pos] = '.'
    grid[next_pos] = '@'
    curr_pos = next_pos

grid.print()
out = sum(X_(pos) + 100 * Y_(pos) for pos, v in grid.items() if v == '[')
print(out)

submit(out, part="b", day=day, year=year)
