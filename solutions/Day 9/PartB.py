from utils import *
from aocd import get_data, submit

year, day = 2024, 9

dat = get_data(year=year, day=day, block=True)

# 2858
dat2 = '''2333133121414131402'''

print(truncate(dat, 80))

dat = dat + '0' if len(dat) % 2 == 1 else dat
res = []
for i, (block_rep, empty) in enumerate(batched(dat, 2)):
    res.append([i] * int(block_rep))
    res.append([None] * int(empty))

res_final = res.copy()


def is_empty(file):
    return all([x is None for x in file])

k = len(res) - 1
for file in res[::-1]:
    if is_empty(file):
        continue
    k = next(i for i, v in enumerate(res_final) if tuple(v) == tuple(file))
    file_size = len(file)
    for j in range(len(res_final)):
        curr_space = res_final[j]
        curr_space_size = len(curr_space)
        if tuple(file) == tuple(curr_space):
            break
        if curr_space_size >= file_size and is_empty(curr_space):
            res_final.insert(k, [None] * len(res_final[k]))
            del res_final[k+1]
            if k < len(res_final) and is_empty(res_final[k]) and is_empty(res_final[k - 1]):
                res_final.insert(k - 1, [None] * (len(res_final[k]) + len(res_final[k - 1])))
                del res_final[k]
                del res_final[k]

            res_final.insert(j, [None] * (curr_space_size - file_size))
            res_final.insert(j, file)
            del res_final[j + 2]
            break


res_list = [x for y in res_final for x in y]
res = {i: v for i, v in enumerate(res_list)}

val = sum(i * v for i, v in res.items() if v is not None)

print(val)
