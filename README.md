# Advent of Code 2024

Attempts for the [Advent of Code](https://adventofcode.com/) 2024.

![Calendar](https://github.com/DylanZammit/Advent-Of-Code-2023/blob/master/img/calendar.png?raw=true)

**WARNING: SPOILERS AHEAD**

## [Problem 1](https://adventofcode.com/2024/day/1)
### Part 1
For Part 1 we can sort both lists and then sum the absolute difference between them to give the solution.

```python
l1, l2 = np.sort(dat[::2]), np.sort(dat[1::2])
ans = sum(abs(l1 - l2))
```

### Part 2
For Part 1, we can use a lambda function to count the number of times an element occurs in an array. We then iterate
the first list and count the number of times each element appears in the second list.
```python
count = lambda arr, elt: len([i for i in arr if i == elt])
```
## [Problem 2](https://adventofcode.com/2024/day/2)
### Part 1
By taking the sequential differences of a report we can find out two things.
* If all differences are of the same sign, then the original sequence _must_ be strictly increase or decreasing.
* If the absolute value of each elements difference is between 1 and 3 (included), then the other condition is satisfied.
```python
num_sd = quantify(np.abs(np.diff(report)), lambda d: d < 1 or d > 3)
num_asc = quantify(np.diff(report), lambda d: d >= 0)
num_desc = quantify(np.diff(report), lambda d: d <= 0)
```
With the above counts calculated for a specific `report`  then all we have to check is `num_sd == 0 and (num_asc == 0 or num_desc == 0)`.
### Part 2
For the second part we take a brute force approach and follow these steps.
* Check if report is valid
* If not, check by how many elements it is invalid
* If by more than 1 element, skip the report.
* If by at most 1 element, iterate through each element, remove the item, and check if it is valid.
* Stop until either a sub-report is valid, or all sub-reports are invalid.
## [Problem 3](https://adventofcode.com/2024/day/3)
### Part 1
Using regex we can capture all instances of multiplications such as `mul(x,y)` using
```pythonregexp
(mul\(\d+,\d+\))
```
### Part 2
We first remove all characters encapsulated by the "don't" and "do"s using the below regex, and then repeat Part 1.
```pythonregexp
don\'t\(\).*?do\(\)
```
## [Problem 4](https://adventofcode.com/2024/day/4)
### Part 1
A brute force approach was taken.
* Iterate all `X` elements in the matrix.
* For each such instance iterate all 8 possible directions (N, NE, E, etc.).
* For each direction check if the successive values in that direction from the `X` positions are `M`, `A` and `S`.
### Part 2
Similar to Part 1 but for each `A` position, check that both diagonals are equal to the set `{M, S}`.
## [Problem 5](https://adventofcode.com/2024/day/5)
### Part 1
For each page, get all rules in which it is contained in the second part (i.e. the followed-by part).
Then for each such rule check if all the preceeded-by pages exist before the current page.

Eg. Say the report is `3,95,45,75,34` and we are on page `75`. Extracting the valid rules and checking each one we get:
```
3|75  -> 3 is indeed before 75
45|75  -> 45 is indeed before 75
34|75  -> 34 is _not_ before 75 ==> BAD REPORT
```
### Part 2
We notice that for a report to be fully validated, all adjacent pages _must_ be a rule. Otherwise the ordering might be ambiguous.
Thus for each page we can count the number of rules for which it is on the right-end of the rule, giving us its correct position.
## [Problem 6](https://adventofcode.com/2024/day/6)
A brute force approach was taken, where at each step we walk in the same direction if there is no obstacle. Otherwise,
we take a turn to the right. Each position is stored in a set (to avoid duplicates) and counted as soon as the guard
leaves the area.
### Part 1
```python
visited = {pos}
while (next_pos := add2(pos, dir)) in dat:
    pos, dir = (pos, make_turn(dir, 'R')) if dat[next_pos] == '#' else (next_pos, dir)
    visited.add(pos)
```
### Part 2
Another brute force approach with some smart pruning. The same strategy as above was taken.
The only difference is that we apply an extra step if the guard is allowed to move forward because there is no obstacle.
In this case, assume that the guard is faced with an obstacle and has to turn right. Repeat the procedure of Part 1 with
this extra obstacle in place. As soon as the guard steps on a tile facing a direction that was already taken, then it is a loop!
## [Problem 7](https://adventofcode.com/2024/day/7)
### Part 1
We take a brute force approach, where for each sequence of elements, we iterate through all possible operators.
If we find one that matches the left-hand-side, we can break out of the loop.
### Part 2
The exact same approach is taken as Part 1 with the additional concat operator.
Note that instead of casting to a string, concatenating and converting back to an int, we use a more optimal approach.
* We first count the number of digits of the right-operand. 
* Pad the left-operand by this number of zeros.
* Add this new multiplied value with the right-operand.
```python
cat = lambda x, y: x * 10 ** (int(log10(y)) + 1) + y
```
## [Problem 8](https://adventofcode.com/2024/day/8)
### Part 1
Another brute force solution. 
* We first create a dictionary mapping each type of antenna-frequencies to their positions.
* For each frequency we take the pairwise combinations of positions 
* Take the difference between them.
* Then we check if `antenna_position_1 + diff` and `antenna_position_2 - diff` are within bounds
* If so, we add them to a set.
* We count the length of the set

### Part 2
Same strategy is applied here, but instead of checking `antenna_position_1 + diff` and `antenna_position_2 - diff`, we repeat for
* `antenna_position_1 + 0 * diff`
* `antenna_position_1 + 1 * diff`
* `antenna_position_1 + 2 * diff`
* and so on until out of bounds....

And also for 
* `antenna_position_1 - 0 * diff`
* `antenna_position_1 - 1 * diff`
* `antenna_position_1 - 2 * diff`
* and so on until out of bounds....
## [Problem 9](https://adventofcode.com/2024/day/9)
### Part 1
Use a left and right pointer. Move the left one until we reach a non-digit. At that point move the right pointer to the left
until we reach a digit. Pop the digit from the right to the left pointer position, and repeat.
### Part 2
Not good code, slow, but it works...avoid my solution like the plague.
## [Problem 10](https://adventofcode.com/2024/day/10)
### Part 1
A recursive solution, were we start at every position with height 0 and call method A. 
We then turn 90 degrees in all direction, and at each turn call method A again only if the new height position is exactly
one more than the current one. So in the first iteration, we can only move to `1` heights. If the height is `9`, return the position as a set, otherwise check the 4 directions again, this time checking for height `2`.
Finally take the distinct count of all trail end-positions to get the answer.
### Part 2
Only minor adjustments needed from the above. Instead of returning the position of the end of the trail, increment a counter by 1. This way,
we might have multiple trails that end at the same position, but no two trails will be the same.
## [Problem 11](https://adventofcode.com/2024/day/11)
### Part 1
For the first solution we take a breadth first approach, where we iterate the list of stones, and follow the rules for each one.
Once finished, repeat the process for 25 times.
### Part 2
The brute force solution of part 1 takes too long. So instead, we take a depth-first approach.
For each stone we iterate, we apply the rules, and recursively re-apply these rules for the next 25 times.
Notice that the most important part is caching the recursive function.
```python
@cache
def split_num(n, iter = 0, max_iter = 25):
    split_num_pre = partial(split_num, iter=iter + 1, max_iter=max_iter)
    if iter == max_iter:
        return 1
    if n == 0:
        return split_num_pre(1)
    elif (n_digits := int(log10(n)) + 1) % 2 == 0:
        n_new = n_digits // 2
        l, r = int(n // 10 ** n_new), int(n % 10 ** n_new)
        return split_num_pre(l) + split_num_pre(r)
    else:
        return split_num_pre(n * 2024)
```
## [Problem 12](https://adventofcode.com/2024/day/12)
### Part 1
For each tile add it to a set `visited` and a list `L`, and check if any of the four adjacent tiles are of the same type. 
Add each adjacent tile to `L` and recurse the previous step for each adjacent tile that is not already visited.
Once finished we would have a set of lists, each with contiguous tile positions.

The area of each contiguous area is simply the length of each `L`.
To obtain the perimeter, we iterate each tile of `L`, and look in all 4 directions (NSEW).
If the tile next to the current one in the current direction is *not* in `L`, then it is a side.
### Part 2
We notice that the number of "contiguous" sides is equal to the number of inner/outer corners. See the below diagram as 
an example, where the number of sides is equal to the acute/obtuse right-angled corners.
![Day 12](https://github.com/DylanZammit/Advent-Of-Code-2024/blob/master/img/aocd12.png?raw=true)
## [Problem 13](https://adventofcode.com/2024/day/13)
### Part 1
Let `a` and `b` be the number of times we need to press the `A` and `B` buttons respectively.
Let $`i = (i_1, i_2)`$ be the vector which the claw is moved when the `A` button is pressed.
Similarly $`j = (j_1, j_2)`$ for the `B` button.
Finally, let $`z = (z_1, z_2)`$ be the position of the prize.
We would essentially like to solve the systems of equations given by
```math
\begin{align}
a i_1 + b j_1 &= z_1 \\
a i_2 + b j_2 &= z_2
\end{align}
```
If we let $`A = 
  \begin{bmatrix}
    i_1 & j_1 \\
    i_2 & j_2 
  \end{bmatrix}`$, then our problem becomes
```math
\begin{align}
A \begin{bmatrix}
   a\\
   b 
  \end{bmatrix}&=z\\
\implies\begin{bmatrix}
   a\\
   b 
  \end{bmatrix} &= A^{-1}z
\end{align}
```
After solving for `a` and `b` we just need to check that
* they are both positive
* they are both close to integers (eg. `np.isclose(a, round(a))`)
* both `a` and `b` are not more than 100.
### Part 2
For part 2, the third of the conditions above is dropped, but the rest of the solution remains the same.
## [Problem 14](https://adventofcode.com/2024/day/14)
### Part 1
Modulo arithmetic does the trick. If we start at positions $`(p_x^0, p_y^0)`$ with velocity $`(v_x, v_y)`$.
After $`n`$ second, the $`x`$ value would be $`p_x^1 = p_x^0 + n v_x`$. Since the map wraps, we would need to take the modulo
of size $`w`$, the width of the map. 
```math
\begin{align}
p_x^1 &= p_x^0 + nv_x \text{ (mod w)} \\
p_y^1 &= p_y^0 + nv_y \text{ (mod h)}  
\end{align}
```
A similar task is done for the vertical position.
### Part 2
Sorted all possible maps under 10,000 by number of distinct overlaps descending. One of the top positions gives the tree.
## [Problem 15](https://adventofcode.com/2024/day/15)
### Part 1
Each iteration is a move in the current direction, where you skip a turn if faced with a barrier `#`.
If a box `O` is encountered, we check the first non-box tile in the same direction. If this tile is a `#`, do nothing.
Otherwise shift all these boxes by 1.
### Part 2
Same procedure as above with one major adjustment: when meeting a box vertically.
Upon reaching a box, a recursive procedure starts.
* Start with the position of the box you collided with $`p_1`$.
* Without loss of generality, assume that $`p_1`$ is a `[` and $`p_2`$ is a `]` (or swap otherwise).
* Check the tile in front of $`p_i`$ in the same direction and call it $`q_i`$ for $`i\in\{1,2\}`$.
* If any of $`q_1, q_2`$ are `#`, then no box can be moved. 
* If they are both `.`, then these boxes can be safely shifted.
* Otherwise, recurse from step 1, this time for $`q_1`$ if it is part of a box, and similarly for $`q_2`$.
## [Problem 16](https://adventofcode.com/2024/day/16)
### Part 1
An implementation of A* algorithm with a 3-dimensional grid, with the third dimension being the direction.
```python
def action_cost(self, s, a, s1):
    if self.grid[a] == '#': return np.inf
    return 1 if s[1] == a[1] else 1001
```
### Part 2
Once A* finds the optimal path, we continue searching paths attaining the same cost as the first one.
These are then expanded, and the total unique number of tiles are counted.
## [Problem 17](https://adventofcode.com/2024/day/17)
### Part 1
A straightforward implementation by following the rules. Note that "dividing `x` by 2 power `z` and taking the floor" is
equivalent to shifting the bits by `z` spaces. In python this is denoted by `x >> z`.
### Part 2
## [Problem 18](https://adventofcode.com/2024/day/18)
### Part 1
A straightforward implementation of A* algorithm, where create the map by filling the grid with `#`, and the cost of an action is defined as
```python
def action_cost(self, s, a, s1): return np.inf if self.grid[a] == '#' else 1
```
### Part 2
We iterate from `k=1024` onwards (since we know there is a path up until then), and store the shortest path in memory (not just the cost).
At every iteration we place a `#` at the new location and check if it lands on the current shortest path.
If not, the shortest path is untouched, and the same path remains. Otherwise it needs to be recalculated.
If the script hangs, we have found our answer!

Two potential improvements are:
* exit strategy for when a path is not found instead of hanging.
* when a path is hit by a `#`, recalculate A* only from that point onward.

Even without these two improvements, the script finishes in less than a second on my machine.
## [Problem 19](https://adventofcode.com/2024/day/19)
### Part 1
We employ a recursive solution to both parts, with the first technically being a subset of the second.
We iterate through the towel starting from the first part (letter), and checking if it exists in the list of pieces.
If it exists we have two options:
* recurse with the rest of the towel.
* increase the part of the towel by 1, and check if this 2-part towel exists in the list of pieces.
Then repeat until the recursed towel is of 0 length, which means that all pieces of the towel have been found successfully.
There is no need to continue searching, and we can return true. If this condition is never reached, we return false.
### Part 2
This part is similar, but instead of stopping at the first `return True` condition, we instead `return 1`, and proceed the search.
The method should output the number of ways to make the towel.
Caching the recursive function is a must.
```python
@cache
def get_combs(towel) -> int:
    if towel == '': return 1
    return sum(get_combs(towel[j+1:]) for j in range(len(towel)) if towel[:j+1] in pieces)
```
*NOTE*: Actually trying to display the combinations that make up the towel is a challenge as it might take up too much memory and slow the script down considerably, making it infeasible.
## [Problem 20](https://adventofcode.com/2024/day/20)
### Part 1
### Part 2
## [Problem 21](https://adventofcode.com/2024/day/21)
### Part 1
### Part 2
## [Problem 22](https://adventofcode.com/2024/day/22)
### Part 1
Simply following instructions. These can be summarised by the following method.
```python
def gen_secret(secret):
    secret = (secret ^ (secret << 6)) % (2 ** 24)
    secret = (secret ^ (secret >> 5)) % (2 ** 24)
    secret = (secret ^ (secret << 11)) % (2 ** 24)
    return secret
```
### Part 2
At each secret generation we keep track of the last 4 changes and store these changes as a key, and the price as a dictionary value.
We ignore any repeated diffs for the same merchant. But if we encounter the sequence again for a different merchant, we add
the price to the already-existing value.

Finally we can find the maximum value of the dictionary.
## [Problem 23](https://adventofcode.com/2024/day/23)
### Part 1
* Create a dictionary representing an undirected graph, where each vertex is a key, whose corresponding values are the node's neighbours.
* For each key in the dictionary starting with `t`, call it `c3`:
  * Take every pair of possible neighbours, `c1` and `c2`.
  * Check if `c2` and `c3` are neighbours. If they are, add (`c1`, `c2`, `c3`) to a set `K`.
* Count the number of elements of `K`
### Part 2
This is a concept of a [clique](https://en.wikipedia.org/wiki/Clique_(graph_theory)) in graph theory.
A clique is a fully connected subgraph of a graph. Picture a social network graph, where any two friends are connected.
A clique is essentially a group of friends, where every two persons are friends.

What we want is a maximal clique.

> A maximal clique is a clique that cannot be extended by including one more adjacent vertex, that is, a clique which does not exist exclusively within the vertex set of a larger clique.

Finding all cliques, or the maximal clique is an NP-complete problem. The [Bron–Kerbosch algorithm](https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm) is a polynomial-time algorithm for finding the maximal clique in a graph.
We implement this algorithm for the solution of part 2.

```python
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
```
## [Problem 24](https://adventofcode.com/2024/day/24)
### Part 1
For part 1 we should iterate all commands, and apply the operation only if the two operands are defined.
We iterate until all commands have been run, and return the last value of `z`. To calculate the decimal value of `z` from
a list of binary digits $`z_{(2)} = [z_n, z_{n-1}, \cdots, z_1]`$ we compute
```math
z_{(10)} = \sum_{i=0}^n z_i \cdot 2^i.
```
### Part 2
We calculate the correct value of `x + y = z` and convert to binary, and compare that value to the binary representation of `z` by running part 1.

58367545758258 = 1101010001010111000000110101001101001000**1**10010  <-- incorrect

58367528979026 = 1101010001010110111111110101001100101001**0**10010  <-- correct

Most bits seem to be in order, with the first incorrect one occurring at the 6th bit highlighted in **bold**.
This would be a good starting point to look into.
We also notice that a pattern emerges if we draw the logic gates of the first couple of iterations as seen below.
![Day 24](https://github.com/DylanZammit/Advent-Of-Code-2024/blob/master/img/aocd24.png?raw=true)
This is essentially a [full adder](https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder).
Thus our strategy is a semi-programmatic one, where we write down the expected steps in code, and the program should fail if the actual output does not match.
At this point I check the command outputting the correct output, and swap with the wrong one. That would give me the first pair.
I repeat this procedure 3 more times and sort the 8 outputs.

In fact, the first time the script paused in my case, was on the 6th digit as expected. This is only the case for my input.

**NOTE**: This strategy is a bit of a 'pen-and-paper' strategy and is not generalisable. It was only possible because there were only a low number of swaps required.
## [Problem 25](https://adventofcode.com/2024/day/25)
No need to differentiate between keys and locks really using this method. We take a brute force approach and iterate every two pairs of schematics `L` and `K`.
We put the coordinates of `#` in a set for both `L` and `K`, and then check if their intersection is empty.
If it is, we can increment by 1 as there is no overlap.
```python
valid = sum(1 for s1, s2 in combinations(schematics_sets, 2) if len(s1 & s2) == 0)
```