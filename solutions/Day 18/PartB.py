from utils import *
from aocd import get_data, submit

year, day = 2024, 18

dat = get_data(year=year, day=day, block=True)

dat2 = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''

n = 71
k=  0
dat = parse(dat, ints)
print(len(dat))
grid = {}
for i in range(n):
    for j in range(n):
        grid[(i, j)] = '.' if (i, j) not in dat[:k] else '#'
grid = Grid(grid, directions=directions4, default='#')

print(truncate(dat, 200))
print(truncate(grid, 200))
grid.print()


class MyProblem(GridProblem):

    def action_cost(self, s, a, s1): return np.inf if self.grid[a] == '#' else 1


full_path = None
while True:
    print(k, dat[k])

    if full_path is None or dat[k] in full_path:
        sp = MyProblem(grid=grid, initial=(0, 0), goal=(n - 1, n - 1))
        node_path, _ = A_star_search(sp)
        full_path = set(path_states(node_path))
    k += 1
    grid[dat[k]] = '#'


# submit(out, part="b", day=day, year=year)
