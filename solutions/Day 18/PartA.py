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
dat = parse(dat, ints)[:1024]
grid = {}
for i in range(n):
    for j in range(n):
        grid[(i, j)] = '.' if (i, j) not in dat else '#'
grid = Grid(grid, directions=directions4, default='#')

print(truncate(dat, 200))
print(truncate(grid, 200))
grid.print()
out = 0

class MyProblem(GridProblem):

    def action_cost(self, s, a, s1): return np.inf if self.grid[a] == '#' else 1

sp = MyProblem(grid=grid, initial=(0, 0), goal=(n - 1, n - 1))
out = A_star_search(sp)

print(out[0].path_cost)
submit(out, part="a", day=day, year=year)
