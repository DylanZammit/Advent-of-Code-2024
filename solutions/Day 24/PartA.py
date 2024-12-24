from utils import *
from aocd import get_data, submit

year, day = 2024, 24

dat = get_data(year=year, day=day, block=True)

dat2 = '''x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02'''


dat2 = '''x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj'''

starts, cmds = dat.split('\n\n')

wires = {k: int(v) for k, v in [x.split(': ') for x in starts.split('\n')]}
wires_z = {}

complete = 0
all_cmds = cmds.split('\n')
all_cmds = [tuple(x.split()) for x in all_cmds]
n_cmd = len(all_cmds)

ops = {'AND': lambda x, y: x & y, 'OR': lambda x, y: x | y, 'XOR': lambda x, y: x ^ y, }
i = -1
complete = set()
while len(complete) < n_cmd:
    i += 1
    cmd = all_cmds[i % n_cmd]
    a, op, b, _, z = cmd
    if a not in wires or b not in wires:
        continue
    wires[z] = ops[op](wires[a], wires[b])
    if z.startswith('z'):
        wires_z[z] = ops[op](wires[a], wires[b])

    complete.add(i % n_cmd)


def bin_to_dec(d):
    return sum(d[k] * 2 ** i for i, k in enumerate(sorted(d)))

z = bin_to_dec(wires_z)

print(wires_z)
print(z)
submit(z, part="a", day=day, year=year)
