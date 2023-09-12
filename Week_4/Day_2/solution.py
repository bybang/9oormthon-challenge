# 9oormthon Challenge Week 4 - Day 2
# Analyze network

# 1 - 3 - 5				2 - 4
# 	\	|					|
# 		7				    6

from collections import deque

def BFS(start):
    q = deque([start])
    
    component = set()
    
    while q:
        current = q.popleft()
        
        if visited[current]:
            continue
        
        visited[current] = 1
        component.add(current)
        
        for item in graph[current]:
            if not visited[item]:
                q.append(item)
                
    edge = 0
        
    for number in component:
        for item in graph[number]:
            if item in component:
                edge += 1
                    
    return sorted(list(component)), edge / len(component)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
result, density = [], 0

for i in range(1, N + 1):
    if not visited[i]:
        current_comp_list, tempDen = BFS(i)
        
    if abs(tempDen - density) < 1e-8:
        if len(current_comp_list) < len(result):
            density = tempDen
            result = current_comp_list
        elif len(current_comp_list) == len(result):
            if current_comp_list[0] < result[0]:
                density = tempDen
                result = current_comp_list
    elif tempDen > density:
        density = tempDen
        result = current_comp_list
        
print(*result)