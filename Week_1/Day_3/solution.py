# 9oormthon Challenge Day 3
# Calculator 1


import math

T = int(input())

result = 0

for _ in range(T):
	N = input().split()
	first_num = int(N[0])
	op = N[1]
	last_num = int(N[-1])
	
	if op == "+":
		result += first_num + last_num
		
	elif op == "-":
		result += first_num - last_num
		
	elif op == "*":
		result += first_num * last_num
		
	elif op == "/":
		result += math.trunc(first_num / last_num)
		
print(result)

# N = [input().split() for _ in range(T)]

# addAll = []
# result = 0

# for calculations in N:
# 	for cal in calculations:
# 		if "+" in cal:
# 			x = int(calculations[0]) + int(calculations[-1])
# 			addAll.append(x)
# 		elif "-" in cal:
# 			x = int(calculations[0]) - int(calculations[-1])
# 			addAll.append(x)
# 		elif "*" in cal:
# 			x = int(calculations[0]) * int(calculations[-1])
# 			addAll.append(x)
# 		elif "/" in cal:
# 			x = int(calculations[0]) / int(calculations[-1])
# 			addAll.append(math.trunc(x))

# for i in addAll:
# 	result += i

# print(result)