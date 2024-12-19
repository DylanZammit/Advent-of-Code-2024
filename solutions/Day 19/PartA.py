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

def get_combs(towel):
    if towel == '': return True
    for j in range(len(towel)):
        if towel[:j+1] in pieces and get_combs(towel[j+1:]):
            return True
    return False

out = sum(int(get_combs(towel) > 0) for towel in towels)
print(out)
submit(out, part="a", day=day, year=year)
