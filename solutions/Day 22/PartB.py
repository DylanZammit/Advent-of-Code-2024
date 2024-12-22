from utils import *
from aocd import get_data, submit

year, day = 2024, 22

dat = get_data(year=year, day=day, block=True)

dat1 = '''1
2
3
2024'''

dat = dat.split('\n')
dat = [int(x) for x in dat]
truncate(dat, 80)


def gen_secret(secret):
    secret = (secret ^ (secret << 6)) % (2 ** 24)
    secret = (secret ^ (secret >> 5)) % (2 ** 24)
    secret = (secret ^ (secret << 11)) % (2 ** 24)
    return secret

n_iter = 2000
out = 0
cons_prices = defaultdict(int)
for secret in dat:
    cons_prices_found = set()
    p0 = secret % 10
    diffs = []
    best_so_far = 0
    for i in range(n_iter):
        secret = gen_secret(secret)
        p1 = secret % 10
        diffs.append(p1 - p0)

        last_4_diffs = tuple(diffs[-4:])
        if len(diffs) >= 4 and last_4_diffs not in cons_prices_found:
            cons_prices_found.add(last_4_diffs)
            cons_prices[last_4_diffs] += p1
        p0 = p1

best_diff = max(cons_prices, key=lambda key: cons_prices[key])
out = cons_prices[best_diff]

print(out)
submit(out, part="b", day=day, year=year)
