# 9oormthon Challenge Week 2 - Day 3
# Pain reducer

N = int(input())

result = N // 14
N %= 14

result += N // 7
N %= 7

result += N

print(result)

###################### My solution ########################

# N = int(input())

# def calculate_items_needed(N):
# 	bandage, medicine, painkiller = 1, 7, 14 # 1, 7, 14 = 1, 7x1, 7x2
# 	pain = N
# 	count = 0
	
# 	count += pain // painkiller # divide pain with 14 first
# 	pain %= painkiller # for ex) 8 % 14 = 0, but 100 % 14 = 2
	
# 	count += pain // medicine
# 	pain %= medicine
# 	# if pain less than 7, add pain to current count
# 	count += pain # if pain cannot divided with 14, 7, pain = bandage_count
	
# 	return count

# print(calculate_items_needed(N))