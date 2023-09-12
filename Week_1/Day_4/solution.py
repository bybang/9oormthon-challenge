# 9oormthon Challenge Day 4
# A Perfect hamburger

N = int(input())
k = list(map(int, input().split()))

# find the max and index of the max in arr k
MAX = max(k)
maxIndex = k.index(MAX)

# important! array(list) slicing 
# slice k(list) by "maxIndex"
left = k[:maxIndex] # list that doesn't include max val
right = k[maxIndex:] # list that includes max val

# sort/sorted --> chose sorted to avoid data manipulation
sortedLeft = sorted(left)
sortedRight = sorted(right, reverse=True) # sort in descending order

sortedArr = sortedLeft + sortedRight # combine two lists again to check sortedArr and the list k

for i in range(N):
    # case that k and sortedArr doesn't match
	if k[i] != sortedArr[i]:
		print(0)
		break
else:
	print(sum(k))
    
# ========== my solution ===========
# N = int(input())

# k = list(map(int, input().split()))

# result = 0

# # check if the given k's length is not over/under N
# if len(k) == N:
#     # find the index of the biggest number from k
#     max_index = k.index(max(k))
#     # divide the list into ascending and descending order
#     ascending = k[:max_index]
#     descending = k[max_index:]
#     # check if the ascending is sorted in increasing order
#     ascending_sort = all(ascending[i] <= ascending[i+1] for i in range(len(ascending) - 1))
#     # check if the ascending is sorted in decreasing order
#     descending_sort = all(descending[i] >= descending[i+1] for i in range(len(descending) - 1))
#     # if both conditions are True
#     if ascending_sort and descending_sort:
#         result = sum(k)

# print(result)