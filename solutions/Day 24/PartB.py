from utils import *
from aocd import get_data, submit

year, day = 2024, 24

dat = get_data(year=year, day=day, block=True)

dat = ''''''
# bpf,z05,hcc,z11,hqc,qcw,fdw,z35

starts, cmds = dat.split('\n\n')


wires = {k: int(v) for k, v in [x.split(': ') for x in starts.split('\n')]}

all_cmds_raw = cmds.split('\n')
all_cmds_raw = [x.split(' ') for x in all_cmds_raw]

all_cmds = []
for cmd in all_cmds_raw:
    a, op, b, _, z = cmd
    cmd_new = (b, op, a, z) if a > b else (a, op, b, z)
    all_cmds.append(cmd_new)

s1_hist = []
s2_hist = []
s3_hist = []
carry_hist = []
z_hist = []

i = 1
carry = 'mkf'
while True:

    x = 'x{}'.format(str(i).zfill(2))
    y = 'y{}'.format(str(i).zfill(2))
    print(x, y)
    z_next = 'z{}'.format(str(i).zfill(2))
    s1a = next((cmd[-1] for cmd in all_cmds if cmd[0] == x and cmd[1] == 'XOR' and cmd[2] == y), None)
    s1b = next((cmd[-1] for cmd in all_cmds if cmd[0] == y and cmd[1] == 'XOR' and cmd[2] == x), None)
    s1 = s1a or s1b
    s1_hist.append(s1)

    s2a = next((cmd[-1] for cmd in all_cmds if cmd[0] == s1 and cmd[1] == 'AND' and cmd[2] == carry), None)
    s2b = next((cmd[-1] for cmd in all_cmds if cmd[0] == carry and cmd[1] == 'AND' and cmd[2] == s1), None)
    s2 = s2a or s2b
    s2_hist.append(s2)

    za = next((cmd[-1] for cmd in all_cmds if cmd[0] == s1 and cmd[1] == 'XOR' and cmd[2] == carry), None)
    zb = next((cmd[-1] for cmd in all_cmds if cmd[0] == carry and cmd[1] == 'XOR' and cmd[2] == s1), None)
    z = za or zb
    assert z == z_next, f'z != z_correct....{z} != {z_next}'
    z_hist.append(z)

    s3a = next((cmd[-1] for cmd in all_cmds if cmd[0] == x and cmd[1] == 'AND' and cmd[2] == y), None)
    s3b = next((cmd[-1] for cmd in all_cmds if cmd[0] == y and cmd[1] == 'AND' and cmd[2] == x), None)
    s3 = s3a or s3b
    s3_hist.append(s3)

    carrya = next((cmd[-1] for cmd in all_cmds if cmd[0] == s3 and cmd[1] == 'OR' and cmd[2] == s2), None)
    carryb = next((cmd[-1] for cmd in all_cmds if cmd[0] == s2 and cmd[1] == 'OR' and cmd[2] == s3), None)
    carry = carrya or carryb
    carry_hist.append(carry)

    if not s1 or not s2 or not z or not s3 or not carry:
        print(x, y, s1, s2, z, s3, carry)
        pass

    i += 1
