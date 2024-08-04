from collections import *
grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

N = (len(grid))
print(N)

res = 0

rows = defaultdict(int)

for row in range(N):
    rows[tuple(grid[row])] += 1

for j in range(N):
    for i in range(N):
        column = tuple(grid[i][j])
        res += rows[column]
return res


