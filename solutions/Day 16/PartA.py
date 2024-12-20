from utils import *
from aocd import get_data, submit

year, day = 2024, 16

dat = get_data(year=year, day=day, block=True)

# 7036
dat2 = '''###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############'''

# 11048
dat2 = '''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''

class MyProblem(GridProblem):
    """Problem for searching a grid from a start to a goal location.
    A state is just an (x, y) location in the grid."""

    def is_goal(self, state):        return state[0] == self.goal[0]

    def actions(self, state):
        loc, direction = state
        return [(add2(loc, d), d) for d in directions4]

    def result(self, loc1, loc2):
        return loc2

    def h(self, node):
        return taxi_distance(node.state[0], self.goal[0])

    def action_cost(self, s, a, s1):
        if self.grid[a] == '#':
            return np.inf

        if s[1] != a[1]:
            return 1001
        return 1


grid = Grid(dat, directions=directions4)
dat = {(p, d): val for d in directions4 for p, val in grid.items()}
init = next(pos for pos, val in dat.items() if val == 'S')
end = next(pos for pos, val in dat.items() if val == 'E')
print(truncate(dat, 80))
print('=' * 80)

sp = MyProblem(grid=dat, initial=(init[0] , East), goal=end)
res = A_star_search(sp)
out = res.path_cost
print(out)

submit(out, part="a", day=day, year=year)
