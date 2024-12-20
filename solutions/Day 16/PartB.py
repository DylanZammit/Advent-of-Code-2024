from utils import *
from aocd import get_data, submit

year, day = 2024, 16

dat = get_data(year=year, day=day, block=True)

# 45
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

# 64
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

def A_star_search(problem, h=None):
    """Search nodes with minimum f(n) = path_cost(n) + h(n) value first."""
    h = h or problem.h
    return best_first_search(problem, f=lambda n: n.path_cost + h(n))


def get_path_so_far(reached_prev, node):
    curr_node = node.state
    final_path = [node]
    while reached_prev[curr_node][1] is not None:
        prev_node = reached_prev[curr_node][1]
        final_path.append(prev_node)
        curr_node = prev_node.state
    final_path = final_path[::-1]

    return set([f.state for f in final_path])


def best_first_search(problem, f) -> List['Node']:
    "Search nodes with minimum f(node) value first."
    best_cost = np.inf
    best_nodes = []
    node = Node(problem.initial)

    frontier = PriorityQueue([node], key=f)
    reached = {problem.initial: node}
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            if best_cost < node.path_cost:
                return best_nodes
            best_cost = node.path_cost
            best_nodes.append(node)

        for child in expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost <= reached[s].path_cost:
                reached[s] = child
                frontier.add(child)
    return best_nodes


class MyProblem(GridProblem):
    """Problem for searching a grid from a start to a goal location.
    A state is just an (x, y) location in the grid."""

    def is_goal(self, state):
        return state[0] == self.goal[0]

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

        return 1 if s[1] == a[1] else 1001


grid = Grid(dat, directions=directions4)
dat = {(p, d): val for d in directions4 for p, val in grid.items()}
init = next(pos for pos, val in dat.items() if val == 'S')
end = next(pos for pos, val in dat.items() if val == 'E')
print(truncate(dat, 80))
print('=' * 80)

sp = MyProblem(grid=dat, initial=(init[0] , East), goal=end)
res = A_star_search(sp)
tiles = set()
for path in res:
    print(path_states(path))
    tiles |= set([x[0] for x in path_states(path)])
out = len(tiles)
print(out)

submit(out, part="b", day=day, year=year)
