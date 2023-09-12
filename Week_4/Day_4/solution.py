# 9oormthon Challenge Week 4 - Day 4
# detour

from collections import deque


def BFS(start, constr):
    if start == constr:
        return -1

    visited = [0] * (N + 1)
    q = deque([start])

    visited[start] = 1
    distance = 1

    while q:
        distance += 1

        for _ in range(len(q)):
            current = q.popleft()

            for item in graph[current]:
                if visited[item] or item == constr:
                    continue
                if item == E:
                    return distance

                visited[item] = 1
                q.append(item)
    return -1


N, M, S, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    print(BFS(S, i))

# import heapq
# import sys

# input = sys.stdin.readline
# INF = int(1e9)

# N, M, S, E = map(int, input().split())
# graph = [[] for _ in range(N + 1)]

# for _ in range(M):
# 	u, v = map(int, input().split())
# 	graph[u].append(v)
# 	graph[v].append(u)

# def dijkstra(i):
# 	if i in (S, E):
# 		return -1

# 	# heapq.heappush(q, (1, S))
# 	distance = [INF] * (N + 1)
# 	distance[S] = 1
# 	q = [(1, S)]

# 	while q:
# 		dist, current = heapq.heappop(q)

# 		if distance[current] < dist:
# 			continue

# 		if current == E:
# 			return distance[E]

# 		for item in graph[current]:
# 			if item != i and distance[item] > dist + 1:
# 				distance[item] = dist + 1
# 				heapq.heappush(q, (distance[item], item))

# 	return -1

# for i in range(1, N + 1):
# 	result = dijkstra(i)
# 	print(result)