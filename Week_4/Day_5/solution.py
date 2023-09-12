# 9oormthon Challenge Week 4 - Day 5
# Remove connected component

def DFS(i, j, letter):
    matrix[i][j] = letter
    
    stack = [(i, j)]
    visited = set()
    
    while stack:
        x, y = stack.pop()
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            
            if nx in (-1, N) or ny in (-1, N) or matrix[nx][ny] != matrix[x][y]:
                continue
                
            stack.append((nx, ny))
            
    if len(visited) >= K:
        for x, y in visited:
            matrix[x][y] = "."
    
N, K, Q = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(Q):
    i, j, d = input().split()
    
    DFS(int(i) - 1, int(j) - 1, d)
    
for row in matrix:
    print("".join(row))

###################### My solution ###################### 
# from collections import deque

# # BFS should return the modified matrix
# def BFS(x, y):
# 	visited = [[0] * N for _ in range(N)]
# 	q = deque([(x, y)])
	
# 	visited[x][y] = 1
# 	connected = []
	
# 	while q:
# 		current_x, current_y = q.popleft()
		
# 		connected.append((current_x, current_y))
		
# 		for i in range(4):
# 			nx, ny = current_x + dx[i], current_y + dy[i]
			
# 			if nx in (-1, N) or ny in (-1, N):
# 				continue
# 			if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
# 				q.append((nx, ny))
# 				visited[nx][ny] = 1
			
# 	return connected
	
	

# N, K, Q = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(N)]
# matrix = []

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for _ in range(Q):
# 	y, x, d = input().split()
# 	x, y = int(y) - 1, int(x) - 1
	
# 	matrix.append((x, y, d))
	
# for x, y, letter in matrix:
# 	graph[x][y] = letter
	
# 	connected = BFS(x, y)
# 	count_connected = len(connected)
	
# 	if count_connected >= K:
# 		for x, y in connected:
# 			graph[x][y] = "."
			
# for i in graph:
# 	print("".join(i))