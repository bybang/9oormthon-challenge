# 9oormthon Challenge Week 2 - Day 1
# String separator

# get N, S
# Separate S to loop through the given word
# loop through Char list
# separate char list into 3 pieces
# separated = [{a, b, cd}, {a, bc, d}, {ab, c, d}]
# Use set() to remove duplicated data and assign altogether in P
# loop through P and get the index that matches {ab, c, d}
# This logic always have to find the last element of list 'separated'
# Add index of each element ab, c, d + 1
# print the max_score
from itertools import combinations

N = int(input())
S = input()

# assign set to separate the input
P = set()
# blank for combinations of words
blank = [i for i in range(1, N)]
# combinations with 2 blanks
# e.g) if N=4 (1,2), (1,3), (2,3)...
comb = list(combinations(blank, 2))

# get the blank combinations from comb
for first, second in comb:
    # slice by combinations, add it to the set
    # e.g) if S=abcd, S[:1] = 'a'
    P.add(S[:first])
    P.add(S[first:second])
    P.add(S[second:])
# put P into the list and sort
P = list(P)
P.sort()

result = 0
# find the maximum combinations
for first, second in comb:
    score = 0
    # find the indicies for each combs, add 1(because index starts at 0)
    # add score altogether, and find the maximum score through the combinations
    score += P.index(S[:first]) + 1
    score += P.index(S[first:second]) + 1
    score += P.index(S[second:]) + 1
    # result finds the max between current result and given score
    result = max(result, score)

print(result)
# # ========================== My solution ============================ # #

# N = int(input())
# S = input()

# P = set() # Create set for remove duplicated data and store sorted result
# str_bundle = []

# for i in range(1, len(S)):
#     for j in range(i+1, len(S)):
#         sub_strings = [S[:i], S[i:j], S[j:]]
#         sorted_strings = sorted(sub_strings)
#         P.update(sorted_strings)
#         # str_bundle.append(sorted_strings)
# sorted_P = sorted(P)

# # last_bundle = str_bundle[-1]
# result = 0

# for target1 in range(1, N - 1):
#     for target2 in range(target1 + 1, N):
#         char_indices = [sorted_P.index(S[:target1]) + 1, sorted_P.index(S[target1:target2]) + 1, sorted_P.index(S[target2:]) + 1]
#         result = max(result, sum(char_indices))
# # if last_bundle:
# # 	char_indicies = [sorted_P.index(char) + 1 for char in last_bundle]
# # 	result = sum(char_indicies)

# print(result)