# 9oormthon Challenge Week 4 - Day 1
# Union

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
# a list to use in BFS search
union = [0] * (N + 1)

union_count = 0

# get the edges by M
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

for i in range(1, N + 1):
    # if i exist in union, ignore
    if union[i]:
        continue

    q = deque([i])
    # every node that is possible to reach from this node is under union, hence union_count + 1
    union_count += 1
    # check 1 if it is under same union
    union[i] = 1

    while q:
        current = q.popleft()
        # in nodes(item in graph[current]) that can reachable from the current node
        for item in graph[current]:
            # if the item is not under union, and current node has edge from graph[item]
            if not union[item] and current in graph[item]:
                # append item to queue and now item is under union, so check 1
                q.append(item)
                union[item] += 1

print(union_count)

############################# My solution #############################
# def find_parent(parent, x):
# 	if parent[x] != x:
# 		parent[x] = find_parent(parent, parent[x])
# 	return parent[x]

# def union_parent(parent, a, b):
# 	a = find_parent(parent, a)
# 	b = find_parent(parent, b)

# 	if a < b:
# 		parent[b] = a
# 	else:
# 		parent[a] = b

# N, M = map(int, input().split())
# graph = [[] for _ in range(N + 1)]
# parent = [0] * (N + 1)

# for i in range(1, N + 1):
# 	parent[i] = i

# union_count = set()

# for _ in range(M):
# 	s, e = map(int, input().split())
# 	graph[s].append(e)

# for start in range(1, N+1):
# 	for item in graph[start]:
# 		if start in graph[item]:
# 			union_parent(parent, start, item)

# for k in range(1, N + 1):
# 	union_count.add(find_parent(parent, k))

# print(len(union_count))