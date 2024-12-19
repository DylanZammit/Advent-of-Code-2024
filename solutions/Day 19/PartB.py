from utils import *
from aocd import get_data, submit

year, day = 2024, 19

dat = get_data(year=year, day=day, block=True)

dat2 = '''r, wr, b, g, bwu, rb, gb, br

ubwu
brwrr
bggr
gbbr
rrbgbr
bwurrg
brgr
bbrgwb'''

pieces, towels = dat.split('\n\n')
pieces = set(pieces.replace(' ', '').split(','))
towels = towels.split('\n')
truncate(pieces, 80)
truncate(towels, 80)
print('=' * 80)

@cache
def get_combs(towel) -> int:
    if towel == '': return 1
    return sum(get_combs(towel[j+1:]) for j in range(len(towel)) if towel[:j+1] in pieces)

out = sum(get_combs(towel) for towel in towels)
print(out)
submit(out, part="b", day=day, year=year)
