from utils import *
from aocd import get_data, submit

year, day = 2024, 16

dat = get_data(year=year, day=day, block=True)

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

class GridProblem(SearchProblem):
    """Problem for searching a grid from a start to a goal location.
    A state is just an (x, y) location in the grid."""

    def actions(self, loc):           return self.grid.neighbors(loc)

    def result(self, loc1, loc2):     return loc2

    def h(self, node):                return taxi_distance(node.state, self.goal)

    def action_cost(self, s, a, s1, direction):
        if self.grid[a] == '#':
            return np.inf

        if sub(s, a) != direction:
            return 1001
        return 1

def A_star_search(problem, h=None):
    """Search nodes with minimum f(n) = path_cost(n) + h(n) value first."""
    h = h or problem.h
    return best_first_search(problem, f=lambda n: n[0].path_cost + h(n[0]))

def best_first_search(problem, f) -> Tuple['Node', list['Node']]:
    "Search nodes with minimum f(node) value first."
    node, direction = Node(problem.initial), None

    frontier = PriorityQueue([(node, direction)], key=f)
    reached = {problem.initial: node}
    reached_prev = {problem.initial: (node, None)}
    while frontier:
        node, direction = frontier.pop()
        if problem.is_goal(node.state):
            curr_node = node.state
            final_path = [node]
            while reached_prev[curr_node][1] is not None:
                prev_node = reached_prev[curr_node][1]
                final_path.append(prev_node)
                curr_node = prev_node.state
            final_path = final_path[::-1]
            return node, final_path
        for child, dd in expand(problem, node, direction):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                reached_prev[s] = (child, node)
                direction = sub(node.state, child.state)
                frontier.add((child, direction))
    return search_failure

def expand(problem, node, direction):
    "Expand a node, generating the children nodes."
    s = node.state
    for action in problem.actions(s):
        s2 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s2, direction)
        yield Node(s2, node, action, cost), direction

dat = Grid(dat)
print(truncate(dat, 80))
print('=' * 80)

init = next(pos for pos, val in dat.items() if val == 'S')
end = next(pos for pos, val in dat.items() if val == 'E')

grid = Grid(dat, directions=directions4)
sp = GridProblem(grid=grid, initial=init, goal=end)
res = A_star_search(sp)
out = res[0].path_cost
print(out)

submit(out, part="a", day=day, year=year)
