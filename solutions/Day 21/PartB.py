from utils import *
from itertools import pairwise
from aocd import get_data, submit

year, day = 2024, 21

dat = get_data(year=year, day=day, block=True)

# 126384
dat2 = '''029A
980A
179A
456A
379A'''

codes = dat.split('\n')
truncate(dat, 80)

keypad = Grid({
    (0, 0): '7', (1, 0): '8', (2, 0): '9',
    (0, 1): '4', (1, 1): '5', (2, 1): '6',
    (0, 2): '1', (1, 2): '2', (2, 2): '3',
    (1, 3): '0', (2, 3): 'A',
}, directions=directions4)
key_pos = Grid({v: k for k, v in keypad.items()})


direction_pad = Grid({(1, 0): '^', (2, 0): 'A', (0, 1): '<', (1, 1): 'v', (2, 1): '>'}, directions=directions4)
dir_pos = Grid({arrow_direction[v] if v in arrow_direction else Zero: k for k, v in direction_pad.items()})


@cache
def get_best_path_horizontal_first(initial, goal, is_keypad = False):

    x0, y0 = initial
    x1, y1 = goal

    path = [initial]
    step = 1 if x0 < x1 else -1
    for xi in range(x0 + step, x1 + step, step):
        path.append((xi, y0))

    step = 1 if y0 < y1 else -1
    for yi in range(y0 + step, y1 + step, step):
        path.append((x1, yi))

    pad = keypad if is_keypad else direction_pad
    is_valid = next((False for p in path if p not in pad), True)
    if is_valid:
        return tuple(path), path[-1]

    path = [initial]
    step = 1 if y0 < y1 else -1
    for yi in range(y0 + step, y1 + step, step):
        path.append((x0, yi))

    step = 1 if x0 < x1 else -1
    for xi in range(x0 + step, x1 + step, step):
        path.append((xi, y1))

    return tuple(path), path[-1]


@cache
def get_best_path_vertical_first(initial, goal, is_keypad = False):

    x0, y0 = initial
    x1, y1 = goal

    path = [initial]
    step = 1 if y0 < y1 else -1
    for yi in range(y0 + step, y1 + step, step):
        path.append((x0, yi))

    step = 1 if x0 < x1 else -1
    for xi in range(x0 + step, x1 + step, step):
        path.append((xi, y1))

    pad = keypad if is_keypad else direction_pad
    is_valid = next((False for p in path if p not in pad), True)
    if is_valid:
        return tuple(path), path[-1]

    path = [initial]
    step = 1 if x0 < x1 else -1
    for xi in range(x0 + step, x1 + step, step):
        path.append((xi, y0))

    step = 1 if y0 < y1 else -1
    for yi in range(y0 + step, y1 + step, step):
        path.append((x1, yi))

    return tuple(path), path[-1]


@cache
def get_path(path_to_follow, robot=0) -> int:

    if robot == n_robots:
        return len(path_to_follow)

    out = 0
    initial = (2, 0)
    for p in path_to_follow:
        best_path_horiz, initial_horiz = get_best_path_horizontal_first(initial, p)
        best_dir_path_horiz = path_to_dirs(best_path_horiz)
        out_horiz = get_path(best_dir_path_horiz, robot=robot+1)

        best_path_vert, initial_vert = get_best_path_vertical_first(initial, p)
        best_dir_path_vert = path_to_dirs(best_path_vert)
        out_vert = get_path(best_dir_path_vert, robot=robot+1)

        if out_horiz < out_vert:
            out += out_horiz
            initial = initial_horiz
        else:
            out += out_vert
            initial = initial_vert

    return out


def path_to_dirs(path):
    return tuple([dir_pos[sub(e, s)] for s, e in pairwise(path)] + [(2, 0)])

all_paths = []
n_robots = 25
for code in codes:
    keypad_path = []

    initial = (2, 3)
    out = 0
    for c in code:
        goal = key_pos[c]
        best_keypad_path, _ = get_best_path_horizontal_first(initial, goal, is_keypad=True)
        best_dir_path = path_to_dirs(best_keypad_path)
        best_sub_path_horiz = get_path(best_dir_path)

        best_keypad_path, _ = get_best_path_vertical_first(initial, goal, is_keypad=True)
        best_dir_path = path_to_dirs(best_keypad_path)
        best_sub_path_vert = get_path(best_dir_path)

        best_sub_path = min([best_sub_path_vert, best_sub_path_horiz])

        out += best_sub_path
        initial = goal

    all_paths.append(out)

out = sum(x * int(code[:-1]) for x, code in zip(all_paths, codes))
print(out)
# 175396398527088 too low
# 325163194497028 too high
# 322223379778572 too high
submit(out, part="b", day=day, year=year)