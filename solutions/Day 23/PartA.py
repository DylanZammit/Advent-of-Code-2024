from utils import *
from aocd import get_data, submit
from itertools import combinations

year, day = 2024, 23

dat = get_data(year=year, day=day, block=True)

dat2 = '''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''

dat = dat.split('\n')

g = defaultdict(set)

for conn in dat:
    c1, c2 = conn.split('-')
    g[c1] |= {c1, c2}
    g[c2] |= {c1, c2}

found = set()
for c3 in {k: v for k, v in g.items() if k.startswith('t')}:
    for c1, c2 in combinations(g[c3], 2):
        if c1 in g[c2] and c3 not in (c1, c2):
            found.add(tuple(sorted([c1, c2, c3])))

out = len(found)
print(out)
submit(out, part="a", day=day, year=year)
