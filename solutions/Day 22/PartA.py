from utils import *
from aocd import get_data, submit

year, day = 2024, 22

dat = get_data(year=year, day=day, block=True)

# Single day
# 1: 8685429
# 10: 4700978
# 100: 15273692
# 2024: 8667524
# 2000 days
# 37327623
dat2 = '''1
10
100
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
for secret in dat:
    for i in range(n_iter):
        secret = gen_secret(secret)
    out += secret

print(out)
submit(out, part="a", day=day, year=year)
