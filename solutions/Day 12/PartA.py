from utils import *
from aocd import get_data, submit

year, day = 2024, 12

dat = get_data(year=year, day=day, block=True)

dat2 = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

dat = Grid(dat)
print(truncate(dat, 80))
gp_map = defaultdict(set)
visited = set()

def get_contig(pos, gp):
    visited.add(pos)
    gp_map[gp].add(pos)
    for dir in directions4:
        next_pos = add2(pos, dir)
        if next_pos in dat and next_pos not in visited and dat[next_pos] == dat[pos]:
            get_contig(next_pos, gp)


gp = 0
for pos in dat:
    if pos not in visited:
        get_contig(pos, gp)
        gp += 1

def get_cost(posns):
    perim = sum(1 for pos in posns for d in directions4 if add2(pos, d) not in dat or dat[add2(pos, d)] != dat[pos])
    return len(posns) * perim


out = sum(get_cost(posns) for posns in gp_map.values())
print(out)
submit(out, part="a", day=day, year=year)
