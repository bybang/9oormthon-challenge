# 9oormthon Challenge Week 3 - Day 2
# Generator

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

generator = 0

def DFS(i, j):
    stack = [(i, j)]
    
    while stack:
        x, y = stack.pop()
        # if matrix[x][y](popped) == visited, ignore
        if not matrix[x][y]:
            continue
        matrix[x][y] = 0
    
        for k in range(4):
           nx, ny = x + dx[k], y + dy[k]
           # if nx = -1 or N or ny = -1, N or if matrix[nx][ny] == 0(visited), ignore
           if nx in (-1, N) or ny in (-1, N) or not matrix[nx][ny]:
               continue

           stack.append((nx, ny))

for i in range(N):
	for j in range(N):
		if matrix[i][j]:
			generator += 1
			DFS(i, j)

print(generator)


######################## My Solution ########################
# from collections import deque

# N = int(input())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * N for _ in range(N)]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# queue = deque()

# def connected_group(x, y):
# 	queue.append((x,y))
# 	visited[x][y] = 1
	
# 	while queue:
# 		x, y = queue.popleft()
# 		for k in range(4):
# 			nx = x + dx[k]
# 			ny = y + dy[k]

# 			if 0 <= nx < N and 0 <= ny < N:
# 				if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
# 					queue.append((nx, ny))
# 					visited[nx][ny] = 1

# generator = 0

# for i in range(N):
# 	for j in range(N):
# 		if matrix[i][j] == 1 and visited[i][j] == 0:
# 			generator += 1
# 			connected_group(i, j)

# print(generator)
# # loop the matrix
# # set starting point
# # for i in range(N)
# # for j in range(N)
# # if temp[i][j] == 1
# # assign current position
# # check four directions that is not contain current position
# # if next direction == 1
# # go next direction and check four direction
# # continue to check until there are no more 1