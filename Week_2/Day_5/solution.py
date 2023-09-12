# 9oormthon Challenge Week 3 - Day 1
# Pain (2)

N = int(input())
A, B = map(int, input().split())

dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(N + 1):
    if i - A >= 0:
        dp[i] = min(dp[i], dp[i - A] + 1)
    if i - B >= 0:
        dp[i] = min(dp[i], dp[i - B] + 1)

print(dp[N] if dp[N] != float('inf') else -1)


##################### My Solution #####################
# '''
# Ai = minimum number to make N
# k = each conditions(Ap, Bp in this case)

# Recurrence Relation
# if A(i-k) is exist, Ai = min(Ai, (A(i-k) + 1))

# ---> A(i-Ap) or A(i-Bp), 2<= Ap < Bp <= 13, so loop range(2, N+1)
# ---> if N == 2 k == 2 i == 2, 0(starting) + 1, hence d[2] == 1

# if A(i-k) doesn't exist(Ap, Bp can't make 0), Ai = -1
# '''

# N = int(input())
# Ap, Bp = map(int, input().split())

# # make and fill array with very big number. This number means that no combinations can make 0
# # calculate and save(memoization) the result in d[i]
# d = [1e7] * (N + 1)
# # resetting d[0] to 0(starting point)
# d[0] = 0

# for i in range(N + 1):
# 	if i - Ap >= 0:
# 		# d[i - Ap] + 1, because we used the item(Ap)
# 		d[i] = min(d[i], d[i - Ap] + 1)
# 	if i - Bp >= 0:
# 		d[i] = min(d[i], d[i - Bp] + 1)

# # Is it possible to make N with Ap, Bp?
# if d[N] == 1e7: # case that impossible to make 0 with Ap, Bp
# 	print(-1)
# else:
# 	print(d[N])
