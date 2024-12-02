from utils import *
from aocd import get_data, submit


count = lambda arr, elt: len([i for i in arr if i == elt])

year, day = 2024, 1

dat = ints(get_data(year=year, day=day, block=True))

l1, l2 = dat[::2], dat[1::2]

ans = sum(l * count(l2, l) for l in l1)
print(ans)

submit(ans, part="b", day=day, year=year)
