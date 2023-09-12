# 9oormthon Challenge Day 5
# Binary sort

# In order to accomplish this goal,
# First, N, K = map(int, input().split())
# a = list(map(int, input().split()))
# Second, for i in a
# set the logic to check how many 1's in each number
# append binary numbers to a new Array in descending order 
# Next, for i in newArray
# if index == k's number, return index's number

N, K = map(int, input().split())
arr = list(map(int, input().split()))

newArr = []

for i in range(N):
	binaryNumber = bin(arr[i])[2:]
	
	count = 0
	
	for c in binaryNumber:
		if c == '1':
			count += 1
	
	newArr.append( [count, arr[i]] )

newArr.sort(reverse=True)
print(newArr[K - 1][1])

# # ====== My solution ======

# N, K = map(int, input().split())
# a = list(map(int, input().split()))

# binary_arr = []

# if N == len(a):
# 	for num in a:
# 		binary_num = '{0:b}'.format(num)
# 		count_one = binary_num.count('1')
# 		binary_arr.append((count_one, num))

# sorted_arr = sorted(binary_arr, key=lambda x: (-x[0], -x[1]))


# print(sorted_arr[K-1][1])