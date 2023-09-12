# 9oormthon Challenge Week 4 - Day 3
# Intersection Point

N, M = map(int, input().split())
matrix = [[[0, 0] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    y, x, command = input().split()
    x, y = int(y) - 1, int(x) - 1

    if command == "U":
        for i in range(x + 1):
            matrix[i][y][0] += 1
    elif command == "D":
        for i in range(x, N):
            matrix[i][y][0] += 1
    elif command == "L":
        for j in range(y + 1):
            matrix[x][j][1] += 1
    elif command == "R":
        for j in range(y, N):
            matrix[x][j][1] += 1

result = 0

for i in range(N):
    for j in range(N):
        result += matrix[i][j][0] * matrix[i][j][1]

print(result)


################# My Solution #################
# def search(x, y, command, line):
# 	directions = {
# 		"U": (-1, 0),
# 		"R": (0, 1),
# 		"D": (1, 0),
# 		"L": (0, -1)
# 	}

# 	x_current = x
# 	y_current = y

# 	for _ in range(1, N + 1):
# 		if 1 <= x_current < N + 1 and 1 <= y_current < N + 1:
# 			line[x_current][y_current] += 1
# 			x_current += directions[command][0]
# 			y_current += directions[command][1]

# N, M = map(int, input().split())
# matrix = []

# for _ in range(M):
# 	y, x, command = input().split()
# 	matrix.append(((int(y), int(x)), command))

# # print(matrix)

# result = 0

# horizontal = [[0] * (N + 1) for _ in range(N + 1)]
# vertical = [[0] * (N + 1) for _ in range(N + 1)]

# for (x, y), command in matrix:
# 	if command == "U" or command == "D":
# 		search(x, y, command, horizontal)
# 	elif command == "L" or command == "R":
# 		search(x, y, command, vertical)

# for i in range(1, N + 1):
# 	for j in range(1, N + 1):
# 		result += horizontal[i][j] * vertical[i][j]

# print(result)