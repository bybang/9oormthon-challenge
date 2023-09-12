# 9oormthon Challenge Day 2
# Become a Project Manager!

from datetime import datetime, timedelta

N = int(input())
T, M = map(int, input().split())
start_time = datetime(year=2023, month = 1, day =1, hour = T, minute = M)

time_consumption = timedelta()

for i in range(N):
	c = int(input())
	time_consumption += timedelta(minutes = c)
	
final_time = (start_time + time_consumption).strftime("%-H %-M")
	
print(final_time)

# N = int(input())
# T, M = map(int, input().split())
# c = [int(input()) for _ in range(N)]

# time = (T * 60 + M + sum(c)) % 1440

# hour = time // 60
# minute = time % 60

# print(hour, minute)