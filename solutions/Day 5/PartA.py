from utils import *
from aocd import get_data, submit

year, day = 2024, 5

dat = get_data(year=year, day=day, block=True)

dat2 = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

pub, order = dat.split('\n\n')
pub = parse(pub, ints)
ordering = parse(order, ints)
print(truncate(pub, 30))
print(truncate(order, 30))


is_valid = None
tot = 0
for order in ordering:
    mid = order[len(order) // 2]
    for i, page in enumerate(order):
        rules = [p for p in pub if p[1] == page and p[0] in order]
        is_valid = all(r[0] in set(order[:i]) for r in rules) if i > 0 else len(rules) == 0
        if not is_valid:
            mid = 0
            break
    tot += mid

print(tot)
submit(tot, part="a", day=day, year=year)