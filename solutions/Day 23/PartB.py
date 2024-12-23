from utils import *
from aocd import get_data, submit
from itertools import combinations

year, day = 2024, 23

dat = get_data(year=year, day=day, block=True)

# co,de,ka,ta
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
    g[c1].add(c2)
    g[c2].add(c1)

cliques = set()
def bron_kerbosch(P, R, X):
    if P == set() and X == set():
        cliques.add(','.join(sorted(tuple(R))))
        return R
    P_orig = P.copy()
    for v in P_orig:
        bron_kerbosch(P & g[v], R | {v}, X & g[v])
        P.remove(v)
        X = X | {v}

bron_kerbosch(set(g.keys()), set(), set())
out = max(cliques, key=lambda v: len(v))

print(out)
submit(out, part="b", day=day, year=year)

