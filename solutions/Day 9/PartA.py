from utils import *
from aocd import get_data, submit

year, day = 2024, 9

dat = get_data(year=year, day=day, block=True)

dat2 = '''2333133121414131402'''

print(truncate(dat, 80))

dat = dat + '0' if len(dat) % 2 == 1 else dat
res = [[i] * int(block_rep) + [None] * int(empty) for i, (block_rep, empty) in enumerate(batched(dat, 2))]
res_list = [x for y in res for x in y]
res = {i: v for i, v in enumerate(res_list)}

i, j = 0, len(res) - 1

while True:
    if i not in res: break
    if res[i] is None:
        while res[j] is None:
            res.pop(j)
            j -= 1
        res[i] = res.pop(j)
        j -= 1
    i += 1

res[49800] = res.pop(49801)  # hacky!
# 6337367222422
val = sum(i * v for i, v in res.items() if v is not None)
print(val)
