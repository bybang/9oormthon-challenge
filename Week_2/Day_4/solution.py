# 9oormthon Challenge Week 2 - Day 4
# Drop the Bomb!!

N, K = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]
score = [[0] * N for _ in range(N)]

# directions (Center, U, R, D, L)
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

for _ in range(K):
	x, y = map(int, input().split())
	x -= 1
	y -= 1
	
	for k in range(5):
		nx = x + dx[k]
		ny = y + dy[k]
		
		if ny < 0 or ny >= N or nx < 0 or nx >= N or arr[ny][nx] == "#":
			continue
		
		if arr[nx][ny] == "@":
			score[nx][ny] += 2
		else:
			score[nx][ny] += 1

result = 0

result = max([max(i) for i in score])

print(result)

########################### My solution ###########################

# # loop through the matrix
# # iterate following logic:
# # drop the bomb
# # change the matrix(+1) with coordinates and adjacent coordinates
# # after the iteration, find the most biggest

# n, k = map(int, input().split())

# matrix = [list(input().split()) for _ in range(n)]
# exploded = [[0]*n for _ in range(n)] # create matrix with 0s to count bomb effect

# # directions (L,R,U,D)
# dx = [0, -1, 1, 0, 0]
# dy = [0, 0, 0, -1, 1]

# def check_bomb(y, x):
# 	for i in range(5): # loop through 4 directions(LRUD)
# 		nx = x + dx[i]
# 		ny = y + dy[i]
			
# 		# check if current coordinates goes over the matrix
# 		if 0 <= nx < n and 0 <= ny < n and matrix[ny][nx] != "#":
# 			# check the conditions
# 			if matrix[ny][nx] == "@":
# 				exploded[ny][nx] += 2
# 			else:
# 				exploded[ny][nx] += 1
		
# for _ in range(k):
# 	y, x = map(int, input().split())
# 	# exploded[y - 1][x - 1] += 1
# 	check_bomb(y - 1, x - 1) # the matrix starts at 0,0

# result = -1
# for row in exploded:
# 	if max(row) > result:
# 		result = max(row)
			
# print(result)