# 9oormthon Challenge Day 1
# A Gymrat player


def solution(w, r):
    repmax = w * (1 + r/30)
    return int(repmax)


w, r = map(int, input().split())

result = solution(w, r)

print(result)