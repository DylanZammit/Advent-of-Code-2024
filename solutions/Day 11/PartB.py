from utils import *
from functools import partial
from aocd import get_data, submit

year, day = 2024, 11

dat = get_data(year=year, day=day, block=True)

dat2 = '''125 17'''

dat = list(parse(dat, ints)[0])
print(truncate(dat, 80))

@cache
def split_num(n, iter = 0, max_iter = 25):

    split_num_pre = partial(split_num, iter=iter + 1, max_iter=max_iter)
    if iter == max_iter:
        return 1
    if n == 0:
        return split_num_pre(1)
    elif (n_digits := int(log10(n)) + 1) % 2 == 0:
        n_new = n_digits // 2
        l, r = int(n // 10 ** n_new), int(n % 10 ** n_new)
        return split_num_pre(l) + split_num_pre(r)
    else:
        return split_num_pre(n * 2024)

n_blinks = 75

out = sum(split_num(n, max_iter=n_blinks) for n in dat)
print(out)
submit(out, part="b", day=day, year=year)
