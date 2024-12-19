from itertools import count

from utils import *
from aocd import get_data, submit

year, day = 2024, 8

dat = get_data(year=year, day=day, block=True)

dat2 = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

dat = Grid(dat)
print(truncate(dat, 80))

tot = 0
antennas = set(dat.values())
antennas_pos = defaultdict(list)
for pos, ant in dat.items():
    if ant == '.':
        continue
    antennas_pos[ant].append(pos)


antis = set()
for ant, positions in antennas_pos.items():
    for ant1, ant2 in combinations(positions, 2):
        diff = sub(ant1, ant2)

        def add_antis(ant, diff):
            for i in count(0):
                apos = add2(ant, mul(diff, i))
                if apos not in dat:
                    break
                antis.add(apos)

        for d in [diff, mul(diff, -1)]:
            add_antis(ant1, d)


tot = len(antis)
print(tot)
submit(tot, part="b", day=day, year=year)
