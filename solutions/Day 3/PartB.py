from utils import *
from aocd import get_data, submit

year, day = 2024, 3

dat = get_data(year=year, day=day, block=True) + 'do()'
# dat = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

print(truncate(dat, 30))

dat = re.sub(r'don\'t\(\).*?do\(\)', '', dat, flags=re.DOTALL)
digs = ints('_'.join(re.findall(r'(mul\(\d+,\d+\))', dat)))

ans = sum([a * b for a, b in batched(digs, 2)])

print(ans)
submit(ans, part="b", day=day, year=year)