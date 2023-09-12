# 9oormthon Challenge Week 3 - Day 4
# small node

from collections import deque

def BFS(start_node):
	q = deque([start_node])
	
	while q:
		current_node = q.popleft()
		# make current node as 'visited'
		visited[current_node] = 1
		# loop through possible nodes that can visit from the current node
		for item in sorted(graph[current_node]):
			if not visited[item]:
				q.append(item)
				break
		else:
			# else means there is no more node to visit(not in for-loop)
			# which means current_node == last visited node
			return current_node

N, M, K = map(int, input().split())
# adjacency list
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	s, e = map(int, input().split())
	# connected edge
	graph[s].append(e)
	graph[e].append(s)
	
visited = [0] * (N + 1)
# call the last node's number(lastly visited node)
result = BFS(K)
# visited == 1 is visited node, hence sum(visited) == the counts of node that bfs() visited.
print(sum(visited), result)