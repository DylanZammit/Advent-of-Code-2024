from utils import *
from itertools import product, pairwise
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
        return tuple(path)

    path = [initial]
    step = 1 if y0 < y1 else -1
    for yi in range(y0 + step, y1 + step, step):
        path.append((x0, yi))

    step = 1 if x0 < x1 else -1
    for xi in range(x0 + step, x1 + step, step):
        path.append((xi, y1))

    return tuple(path)


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
        return tuple(path)

    path = [initial]
    step = 1 if x0 < x1 else -1
    for xi in range(x0 + step, x1 + step, step):
        path.append((xi, y0))

    step = 1 if y0 < y1 else -1
    for yi in range(y0 + step, y1 + step, step):
        path.append((x1, yi))

    return tuple(path)


def get_path(path_to_follow, robot=0):

    if robot == n_robots:
        return tuple(path_to_follow)

    out = []
    initial = (2, 0)
    for p in path_to_follow:
        best_path = get_best_path_horizontal_first(initial, p)
        best_dir_path = path_to_dirs(best_path)
        best_sub_path = get_path(best_dir_path, robot=robot+1)
        initial = best_path[-1]
        out = out + list(best_sub_path)

    return tuple(out)


def path_to_dirs(path):
    return tuple([dir_pos[sub(e, s)] for s, e in pairwise(path)] + [(2, 0)])

def path_to_arrow(path):
    return tuple([direction_pad[p] for p in path])


all_paths = []
n_robots = 2
for code in codes:
    keypad_path = []

    initial = (2, 3)
    out = []
    for c in code:
        goal = key_pos[c]
        best_keypad_path = get_best_path_horizontal_first(initial, goal, is_keypad=True)
        best_dir_path = path_to_dirs(best_keypad_path)
        best_sub_path_horiz = get_path(best_dir_path)


        best_keypad_path = get_best_path_vertical_first(initial, goal, is_keypad=True)
        best_dir_path = path_to_dirs(best_keypad_path)
        best_sub_path_vert = get_path(best_dir_path)

        best_sub_path = min([best_sub_path_vert, best_sub_path_horiz], key=lambda x: len(x))

        out = out + list(best_sub_path)
        print(path_to_arrow(out))
        initial = goal

    all_paths.append(''.join(path_to_arrow(out)))

for x in all_paths:
    print(x, len(x))
out = sum(len(x) * int(code[:-1]) for x, code in zip(all_paths, codes))
print(out)
submit(out, part="a", day=day, year=year)
