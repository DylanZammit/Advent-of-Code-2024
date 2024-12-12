from utils import *
from aocd import get_data, submit

year, day = 2024, 12

dat = get_data(year=year, day=day, block=True)

dat1 = '''RRRRIICCFF
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
    area = len(posns)
    perim = 0
    for pos in posns:
        d1 = North
        for i in range(4):
            d2 = make_turn(d1, 'R')
            if add2(pos, d1) not in posns and add2(pos, d2) not in posns:
                perim += 1
            if add2(pos, d1) in posns and add2(pos, d2) in posns and add2(pos, add2(d1, d2)) not in posns:
                perim += 1
            d1 = d2
    return area * perim


out = sum(get_cost(posns) for posns in gp_map.values())
print(out)
submit(out, part="b", day=day, year=year)
