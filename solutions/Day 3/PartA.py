from utils import *
from aocd import get_data, submit

year, day = 2024, 3

dat = get_data(year=year, day=day, block=True)

dat2 = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

print(truncate(dat, 30))

digs = ints('_'.join(re.findall(r'(mul\(\d+,\d+\))', dat)))
ans = sum([a * b for a, b in batched(digs, 2)])
print(ans)
submit(ans, part="a", day=day, year=year)
