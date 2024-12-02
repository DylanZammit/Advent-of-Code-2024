from utils import *
from aocd import get_data, submit

year, day = 2024, 1

dat = ints(get_data(year=year, day=day, block=True))

l1, l2 = np.sort(dat[::2]), np.sort(dat[1::2])
ans = sum(abs(l1 - l2))
print(ans)

submit(ans, part="a", day=day, year=year)
