# Goormthon Challenge Day 19

### 구름톤 코딩테스트 챌린지 4주차 네 번째 날,

> 이번 문제는 그래프에서 최단거리를 구하는 문제이다.

# 🧩 문제

# 🎯 전략
### 문제의 요구사항 정리하기
문제가 복잡할 수록 요구사항을 하나하나 정리해야한다.
1. start 도시에서 end 도시까지 이동하는데 거쳐가는 중간 도시가 적은 쪽으로 가야한다.
2. 거쳐가는 중간 도시의 수를 출력해야 한다.
3. 플레이어는 N일동안 N번 도시를 이동하는데, i일에는 i번 도시가 공사를 한다.
4. 출발,도착 도시에서 공사중이거나 s에서 e까지 도달할 수 없다면 -1을 출력한다.

### BFS 함수 설정 - 1
1. 함수에 들어갈 변수와 초기 설정
BFS에서 구할 값과 들어가야하는 변수를 구해보자. 먼저 start 도시와 공사중인 도시 i는 들어가야 출발 도시 설정과
공사중인지 아닌지 여부를 체크할 수 있을 것이다. 그리고 1번 도시부터 N번까지 반복문을 돌며 최단 경로를 구해서
리턴값을 받아 출력한다면 출력 예시처럼 출력할 수 있다.

```python
... 

for i in range(1, N+1):
    print(BFS(S, i))
```
2. BFS로 변수 받아서 시작 도시가 공사중인지 체크하기
초기 설정이 완료 되었고, 리턴 받을 값도 정했다면 요구사항에 만족하는 조건을 하나하나 체크하며 세부 코드를 작성한다.
가장 처음 체크해야 할 것은 시작 도시가 공사중인지 여부이다.

시작 도시 `start`와 공사중인도시 `constr(abbreviation for construction)`를 받아 시작 도시가 공사중이라면 -1
을 출력해준다.

```python
def BFS(start, constr):
    if start == constr:
        return -1
```

### BFS 함수 설정 - 2
1. 방문 배열, 큐, 경로 변수 설정
BFS에 없어서는 안될 큐와 방문 배열, 최단 경로 카운트를 위한 경로 변수를 설정해 주어야한다. 방문 배열은 공사중인 도시 i를
체크할때마다 리셋 해주어야 하니 BFS 안쪽에 설정해주어야하고, 경로는 시작도시부터 카운트해 1에서 시작한다.

```python
def BFS(start, constr):
    ...
    
    visited = [0] * (N + 1)
    q = deque([start])
    
    visited[start] = 1
    distance = 1
```

2. while 반복문 설정
큐가 존재할때 마다 반복해 갈 수 있는 모든 연결된 도시를 탐색하는 반복문을 만들어 주자. 큐는 현재 방문하는 도시를 의미하고
반복문이 돌아간다면 방문할 새로운 도시가 큐에 존재한다는 것이므로 조건을 따지기 전에 먼저 경로 + 1을 해주고 조건문을 설정한다.
(시작 도시 경로 1, 1에서 연결된 도시 2개 = 경로 2...)

```python
def BFS(start, constr):
    ...
    
    while q:
        distance += 1
```

3. 현재 경로에 해당하는 모든 도시 체크하는 반복문
BFS이므로 현재 방문하는 도시에서 갈 수 있는 모든 경로를 체크한다! 이것을 위해서는 다음과 같은 식이 필요하다.

```python
...
    while q:
        distance += 1
        
        for _ in range(len(q)):
            current = q.popleft()
```

### BFS 함수 설정 - 3
1. 현재 도시 변수와 함께 그래프 탐색
큐에서 확인하고자 하는 변수를 빼서 `current`라는 변수에 넣어주고, 그래프[현재도시]에 있는 변수들을 `item`이라고 하자.
그래프 안의 `item`들을 방문배열 체크를 통해 방문했는지, 그리고 공사중이 아닌지 체크하고 만약 방문했거나 공사중이면 패스한다.

```python
    ...
        ...
        
        for item in graph[current]:
            if visited[item] or item == constr:
                continue
```

2. 반복문 종료 조건과 다음 도시 체크
현재 반복문은 시작도시에서 출발해 목표도시 `E(end city)`에 도착하면 최단 경로를 리턴하며 종료하는 것이 목표이다. 따라서 해당 조건을
설정해준 뒤에 위의 조건을 모두 만족하지 않는 다면 다음 도시로 이동해 똑같은 과정을 거쳐주면 모든 이동 가능한 도시를 체크할 수 있다.

큐가 비어있어서 반복문을 마쳤는데 목표도시 E에 도달하지 못했다면 목표 도시로 갈 수 있는 방법이 없는 것이다. 따라서 -1을 리턴해준다.

```python
    ...
    
        for item in graph[current]:
            ...
            
            if item == E:
                return distance
                
            visited[item] = 1
            q.append(item)
            
    return -1
```

### BFS의 리턴 값과 반복문을 이용해 답변 도출하기
BFS의 리턴 값은 S에서 E까지의 최단 경로를 의미하며, 반복문은 공사중인 도시 i를 체크한다. 예를들어 예제 1번에 4번째 예제는
도시 1에서 출발해 도시 4로 가야하는데 4일째이기에 4번 도시가 공사중이므로 갈 수 있는 방법이 없다. 따라서 -1을 출력한다.

# 📌 느낀점
최단 경로 문제라고 해서 열심히 다익스트라 알고리즘을 공부해서 풀었는데 BFS로도 풀리는 문제였다.
다익스트라 알고리즘을 100% 이해한건 아니기에 BFS로 풀어볼껄 하는 아쉬움은 있다. 풀이를 보니 BFS가 조금 더
직관적인 이해가 가능했다(물론 중간에 하다가 막혔을 거 같긴하다)

# 💻 풀이

```python
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
```

- My solution(Dijkstra)

```python
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, S, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)
	
def dijkstra(i):
	if i in (S, E):
		return -1
	
	# heapq.heappush(q, (1, S))
	distance = [INF] * (N + 1)
	distance[S] = 1
	q = [(1, S)]
	
	while q:
		dist, current = heapq.heappop(q)
		
		if distance[current] < dist:
			continue
			
		if current == E:
			return distance[E]
			
		for item in graph[current]:
			if item != i and distance[item] > dist + 1:
				distance[item] = dist + 1
				heapq.heappush(q, (distance[item], item))
				
	return -1

for i in range(1, N + 1):
	result = dijkstra(i)
	print(result)
```


# 🔖 복습
```python
문제 파악해서 출력해야 하는 값이 무엇인지, 어떻게 출력할 것인지 정하기
BFS로도 문제에서 요구하는 출력값은 도출할 수 있었다. 최단경로를 구해야하고, N일동안 i일에 i도시가 공사를 진행한다.

for i in range(1, N + 1):
    print(BFS(S, i))
    
BFS안에서 방문배열과 최단경로 변수 설정하기
방문 배열은 위의 반복문에서 i가 변할때마다 항상 리셋되어야 하므로 BFS 바깥이 아닌 BFS안의 로컬 변수로 설정해주어야 한다.
만약 처음 도시가 공사중이라면 바로 -1을 리턴해주는 엣지케이스를 가장 먼저 설정해주고 방문한 도시의 개수 == 최단경로니까
출발하면서 경로 1로 설정해준다.

def BFS(start, constr):
    if start == constr:
        return -1
        
    visited = [0] * (N + 1)
    q = deque([start])
    
    visited[start] = 1
    distance = 1

while 반복문과 BFS 특성 살려서 현재 방문 도시에서 이동 가능한 모든 도시 체크하기
반복문이 시작함과 동시에 1번 도시에서 다음 도시로 이동하는 것이니 경로 + 1을 해주고 시작한다. 큐에 있는 도시 == 현재 방문하는
도시에서 방문 가능한 모든 도시이므로 반복문 범위 range(len(q))를 통해 이 도시들을 모두 처리해준다.

    while q:
        distance += 1
        
        for _ in range(len(q)):
            current = q.popleft()
            
현재 방문 도시와 함께 그래프 탐색하기
그래프 안의 현재 방문 도시에 해당하는 노드를 꺼내와서 조건들을 확인한다. (방문 여부, 공사중인 도시인가, 현재 도시가 목표 도시인가?)
만약 반복문을 전부 돌았는데도 목표하는 도시에 도달을 못했다면 그 도시는 현재 갈 수 없는 도시이므로 -1을 출력해준다.

    while q:
        ...
        
        for _ in range(len(q)):
            current = q.popleft
            
            for item in graph[current]:
                if visited[item] or item == constr:
                    continue
                if item == E:
                    return distance
                
                visited[item] = 1
                q.append(item)
                
    return -1
```