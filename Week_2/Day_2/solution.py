# 9oormthon Challenge Week 2 - Day 2
# Goorm flag finder

# define directions (U, RU, R, RD, D, LD, L, LU)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, K = map(int, input().split())

matrix = [list(input().split()) for _ in range(N)]
'''
same as 
matrix = []

for _ in range(N):
    row = list(input().split())
    matrix.append(row)
'''

result = 0

for i in range(N):
    for j in range(N):
        # matrix[i][j] == "1" >>> "1" means the position has a cloud
        if matrix[i][j] == "1":
            continue
        # count for flag
        check = 0
        
        for z in range(8):
            x = i + dx[z]
            y = j + dy[z]
            
            if y in (-1, N) or x in (-1, N):
                continue
                
            if matrix[x][y] == "1":
                # check each next spots. if the spot has a cloud, counter goes up by 1
                check += 1
        # find the first match(greedy method)
        if check == K:
            result += 1

print(result)


'''
My solution #####################################
'''
# N, K = map(int, input().split())
# # get input for 2 dimensional list
# M = []
# for i in range(N):
# 	M.append(list(map(int, input().split())))
	
# # define directions (U, RU, R, RD, D, LD, L, LU)
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]

# def count_flag(N, K, M):
# 	count = 0
	
# 	for y in range(N):
# 		for x in range(N):
# 			flag_count = 0
			
# 			# If the spot contains 1 (cloud), ignore
# 			if M[x][y] == 1:
# 				continue
# 			# Loop through all directions
# 			for z in range(8):
# 				nx = x + dx[z]
# 				ny = y + dy[z]
# 				# Ignore if nx or ny goes over the map
# 				if nx < 0 or nx >= N or ny < 0 or ny >= N:
# 					continue
				
# 				flag_count += M[nx][ny] == 1
# 			# print("flag_count: ", flag_count)
# 			# Check if the flag count matches K
# 			if flag_count == K:
# 				count += 1
# 	print(count)

# count_flag(N, K, M)