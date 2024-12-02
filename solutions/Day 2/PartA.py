from utils import *
from aocd import get_data, submit

year, day = 2024, 2

dat = get_data(year=year, day=day, block=True)

dat2 = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''


def check_valid(a, b, is_asc):
    if abs(a - b) < 1 or abs(a - b) > 3:
        return False

    if (is_asc and a >= b) or (not is_asc and a <= b):
        return False
    return True


print(truncate(dat, 20))
dat = dat.split('\n')

n_safe = 0
for report in dat:
    probs = 0
    report = ints(report)
    safe = True

    num_sd = quantify(np.abs(np.diff(report)), lambda d: d < 1 or d > 3)
    num_asc = quantify(np.diff(report), lambda d: d >= 0)
    num_desc = quantify(np.diff(report), lambda d: d <= 0)

    if num_sd == 0 and (num_asc == 0 or num_desc == 0):
        n_safe += 1


ans = n_safe
print(ans)
submit(ans, part="a", day=day, year=year)
