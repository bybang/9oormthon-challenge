# 9oormthon Challenge Week 3 - Day 3
# Generator (2)

# directions(U,R,D,L)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(i, j):
	stack = [(i, j)]
	
	apt_num = matrix[i][j]
	count = 0
	
	while stack:
		x, y = stack.pop()
		
		if matrix[x][y] != apt_num:
			continue
			
		matrix[x][y] = 0
		count += 1
		
		for a in range(4):
			nx, ny = x + dx[a], y + dy[a]
			
			if nx in (-1, N) or ny in (-1, N) or matrix[nx][ny] != apt_num:
				continue
				
			stack.append((nx, ny))
			
	return count

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
housing_complex = [0] * 31

for i in range(N):
	for j in range(N):
		if matrix[i][j]:
			apt_num = matrix[i][j]
			
			if DFS(i, j) >= K:
				housing_complex[apt_num] += 1
				
result, temp = 0, 0

for z in range(31):
	if temp <= housing_complex[z]:
		result = z
		temp = housing_complex[z]
		
print(result)

###################### My solution ########################
# N, K = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# visited = [[None] * N for _ in range(N)]
# housing_complex = [0] * 31
# # directions(U,R,D,L)
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# result = 0

# def BFS(i, j, complex_num, visited):
# 	q = deque([(i, j)])
# 	visited[i][j] = True
# 	count = 1
	
# 	while q:
# 		x, y = q.popleft()

# 		for a in range(4):
# 			nx, ny = x + dx[a], y + dy[a]
			
# 			if nx in (-1, N) or ny in (-1, N):
# 				continue
# 			if matrix[nx][ny] == complex_num and not visited[nx][ny]:
# 				q.append((nx, ny))
# 				visited[nx][ny] = True
# 				count += 1
				
# 	return count
					
# for i in range(N):
# 	for j in range(N):
# 		if not visited[i][j]:
# 			# if bfs
# 			if BFS(i, j, matrix[i][j], visited) >= K:
# 				housing_complex[matrix[i][j]] += 1
				
# # find largest_complex in housing_complex
# largest_complex = max(housing_complex)
# for b in range(len(housing_complex)):
# 	if housing_complex[b] == largest_complex:
# 		result = b
		
# print(result)