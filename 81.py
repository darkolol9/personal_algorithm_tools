from functools import cache
limit = 80


def is_valid_coord(x, y):
	
	res = x in range(limit) and y in range(limit)
	return res

with open('./0083_matrix.txt', 'r') as f:
	matrix = [[0] * limit] * limit
	lines = f.readlines()

	for i, line in enumerate(lines):
		matrix[i] = [int(x) for x in line.split(',')]


@cache
def solve(i, j):
	if (i, j) == (79,79):
		print('met the end')
		return matrix[-1][-1]

	curr = matrix[i][j]
	down = 1e6
	right = 1e6
	left = 1e6
	up = 1e6

	if is_valid_coord(i+1, j):
		down = solve(i + 1, j)

	if is_valid_coord(i, j + 1):
		right = solve(i, j + 1)

	return curr + min(down, right, up, left)

print(solve(0, 0))
