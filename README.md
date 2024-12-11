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
