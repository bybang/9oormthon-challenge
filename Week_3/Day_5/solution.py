# 9oormthon Challenge Week 3 - Day 5
# Purchase fruit

N, K = map(int, input().split())
fruits = [list(map(int, input().split())) for _ in range(N)]
# sort by p//c, sorted ==> (price, calories)
fruits.sort(key = lambda x : x[1] // x[0])

# print(fruits)

total_cal = 0

while K and fruits:
    # sort increasing order, get the item from the right side(last elem, [1,7])
    price, calories = fruits.pop()
    
    if K >= price:
        total_cal += calories
        K -= price
    else:
        # if K < price, get calories per price and purchase fruit with the remaining money from the above
        total_cal += (calories // price) * K
        # purchased every fruit, change K = 0 to break the while loop
        K = 0

print(total_cal)

###################### My solution ###################### 
# N, K = map(int, input().split())
# matrix = []

# for _ in range(N):
# 	price, calories = map(int, input().split())
# 	matrix.append((price, calories))


# cpp_values = []
# total_cal = 0
	
# for price, calories in matrix:
# 	# calories per piece (calories/price)
# 	cpp = calories // price
# 	cpp_values.append((cpp, calories, price))
	
# cpp_values.sort(reverse=True)
# budget = K
	
# for cpp, calories, price in cpp_values:
# 	if budget >= price:
# 		budget -= price
# 		total_cal += calories
# 	else:
# 		total_cal += cpp * budget
# 		break

# print(total_cal)

#########################
# How to solve this problem?
# we have K which is the total price
# we have to loop through each list
# first number is the price, second number is the calories
# based on calories, check the price
# 1 1 2 3  7  10
# 5 7 8 12 35 30
# to find a combination
# money = K - biggest calories/price
# 1이 될때까지?
# 13 - 1 = 12
# 12 - 1 = 11
# 11 - 7 = 4
####### 4 - 3 = 1
# 1-1(biggest calories, 4 from 8)

# find c/p biggest calories without fruits that already taken
# (7 + 5 + 35) + 12 + 4 = 63
# reverse the calories
# 35 30 12 8 7 5 = c
# 7  10  3 2 1 1 = p

# 7 5  5  4  4  3 == c/p in order, calories per piece
# 1 7  1  3  2  10 == price
# 7 35 5. 12 8  30