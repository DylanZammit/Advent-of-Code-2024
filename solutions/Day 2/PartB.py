from copy import copy
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


def check_report(report, n=0):
    if n > 1:
        return False

    diff_report = np.diff(report)
    num_sd = quantify(np.abs(diff_report), lambda d: d < 1 or d > 3)
    num_asc = quantify(diff_report, lambda d: d >= 0)
    num_desc = quantify(diff_report, lambda d: d <= 0)

    if num_sd == 0 and (num_asc == 0 or num_desc == 0):
        return True
    elif num_sd <= 1 and (num_asc <= 1 or num_desc <= 1):
        for i in range(len(report)):
            sub_report = copy(report)
            del sub_report[i]
            if check_report(sub_report, n+1):
                return True
    return False


print(truncate(dat, 20))
dat = dat.split('\n')
ans = quantify(dat, lambda report: check_report(list(ints(report))))
print(ans)
submit(ans, part="b", day=day, year=year)
