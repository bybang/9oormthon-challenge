# Goormthon Challenge Day 16

### 구름톤 코딩테스트 챌린지 4주차 첫 번째 날,

> 구름톤 4주차가 시작됐다. 이번 주에는 그래프 탐색문제 위주로 나오는 주라고 한다.

# 🧩 문제

# 🎯 전략
### 조건 분석하기
주어진 조건을 살펴보면 크게 세 가지로 다음과 같다고 볼 수 있다.
1. 임의의 두 섬 a, b에 양방향 다리(간선이)가 있다면 '연합'으로 취급한다.
2. a, b가 연합이고 b, c 가 연합일 때는 a, b, c를 같은 연합에 속해있다고 본다.
(즉, 어떤 섬에서 출발하더라도 연합이라면 연합 내의 모든 섬을 갈 수 있는 것이다.)
3. 다른 섬과 연합을 결성 하지 않아도 모든 섬은 각각 하나의 연합에 속해있다.

모든 섬을 체크해 연합에 속하는지 확인해야 하므로, BFS를 활용해 문제를 풀자.

### 데이터 입력 받기
그래프를 입력받을 때 인접 리스트 방식을 활용하여 그래프를 그리고, 간선(edge)와 빈 연합 배열도 선언해주자.
시작 노드(s)와 끝 노드(e)를 입력받았다면, 그래프를 이용해 s-e 형식으로 `append(e)` 해주자.

마지막은 연합의 수를 나타내는 `union_count`를 0으로 초기화 해 선언해주면 데이터 초기 세팅은 완료된다.

```python
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
union = [0] * (N + 1)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

union_count = 0
```

### 반복문 활용해 BFS 조건 만들기
0번 섬은 없으므로 1번 섬부터 N번 섬까지 반복문을 선언해주자 범위: `(1, N+1)`

섬들을 돌면서 이번 섬이 연합에 이미 속해 있다면 무시해주고, 속해있지 않다면 섬 번호를 큐에 넣어서
BFS를 활용해 전체 탐색을 진행해준다. 현 과정을 진행한다면 연결 되어있는 섬이 있든 없든 자체적으로 연합을
가지기에 `union_count + 1`을 해주고 현재 섬을 연합[i]에 0 대신 1을 채워주며 연합 체크 완료 표시를 해준다.

(만약 연합[i]가 존재한다면(1이라면), 양방향 간선이라는 뜻이므로 더 이상의 데이터 처리를 해줄 필요가 없다.)

```python
...
for i in range(1, N + 1):
    if union[i]:
        continue
        
    q = deque([i])
    union_count += 1
    union[i] = 1
    
    while q:
        current = q.popleft()  
```

그리고 현재 노드를 탐색에 사용해주기 위해 `q.popleft()`로 처리해준다.

### 그래프 탐색하기
현재 노드를 구했다면 탐색에 활용할 때다.
1. 먼저 그래프를 현재 노드값을 활용해 탐색해준다.
그래프는 리스트들로 이루어진 인접 리스트 방식의 그래프 이므로, `graph[current]`는 리스트를 종속 변수로 가지고 있다.
`item`은 그래프[현재노드] 리스트의 첫 번째 변수이므로 현재 노드(섬)에서 체크 가능한 섬들 중에서 n번째 변수는... 라고 할 수 있다.

```python
...
    while q:
        current = q.popleft()
        
        for item in graph[current]:
```
2. 조건문을 활용하여 연합인지 여부를 체크해 준다.
가장 먼저 연합[n번째 변수]를 활용하여 연합 체크를 마쳤는지(0인지 1인지)를 파악해주고 0이라면, 다음으로 현재 노드(섬 번호)가
그래프[n번째 변수]의 안에 존재하는지 체크해 준다. 그래프 안의 섬과 현재 섬의 번호가 같다면 간선이 존재하는 것이다.

```
(예) 첫 번째 예시 중 - 
현재노드 == 1, 그래프[1] == [2,4] / 그래프[2] == [3,4] / 그래프[4] == [1], 첫 번째 아이템 == 2

아이템 == 2 일때, 연합[2] == 0(미체크), 1 in 그래프[2] ? > False
아이템 == 4 일때, 연합[4] == 0(미체크), 1 in 그래프[4] ? > True )
```

두 가지 조건을 모두 만족할 때(연합 체크가 아직인 변수, 간선의 여부) 다음 큐에 대기시켜주고, 연합[n번째변수]를 체크 완료 처리(1) 해준다.

```python
...
    while q:
        current = q.popleft()
        
        for item in graph[current]:
            if not union[item] and current in graph[item]:
                q.append(item)
                union[item] = 1
```

마지막으로 연합의 개수를 출력해주면 된다. 연합의 개수는 `if union[i]` 부분이 결정하는 것이다.(양방향 간선이라면 일련의 과정을 생략하므로 카운트 변화 X)

# 📌 느낀점
BFS로 풀면 더 간단하게 풀 수 있었는데 BFS의 활용법이 생각나지 않아서 전에 공부했던 유니온 파인드의 개념을 활용해서 풀었다.
확실히 어려운 개념으로 접근하지 않아도 DFS/BFS면 풀리는 문제들이 많은 것 같다는 느낌이 든다. 리트코드를 활용해서 탐색 쪽 문제를
더 많이 접해봐야 쉽게 BFS로 접근할 수 있지 않을까 라는 생각이 든다.

# 💻 풀이

```python
from collection import deque

N, M = map(int, input().split())
graph =[[] for _ in range(N + 1)]
union = [0] * (N + 1)

union_count = 0

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    
for i in range(N + 1):
    if union[i]:
        continue
    
    q = deque([i])
    union_count += 1
    union[i]
    
    while q:
        current = q.popleft()
        
        for item in graph[current]:
            if not union[item] and current in graph[item]:
                q.append(item)
                union[item] = 1
                
print(union_count)
```

내가 풀었던 방법

```python
# My Solution
def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b:
		parent[b] = a
	else:
		parent[a] = b

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for i in range(1, N + 1):
	parent[i] = i

union_count = set()

for _ in range(M):
	s, e = map(int, input().split())
	graph[s].append(e)

for start in range(1, N+1):
	for item in graph[start]:
		if start in graph[item]:
			union_parent(parent, start, item)

for k in range(1, N + 1):
	union_count.add(find_parent(parent, k))

print(len(union_count))
```


# 🔖 복습
```python
BFS로 문제 접근해보기
전에 썼었던 방문 배열, 이번에 쓴 연합 체크 배열도 같은 맥락의 문제이다!

union = [0] * (N + 1)

for i in range(N + 1):
    if union[i]:
        continue
        
BFS로 접근했다면 어떤 데이터 구조를 통해 원하는 답을 도출할 것인가 를 생각해보기
실제로 이번 BFS를 쓰지 못했던 이유 중 하나는 union_count를 원하는 방식대로 도출해 낼 수 없었기 때문이다.

for i in range(N + 1):
    if union[i]:
        continue
        
    union_count += 1
    union[i] = 1
    
복잡한 조건문은 말로 풀어서 쓰며 이해하기
실제로 유용한 디버깅 방법중 하나인 rubber duck debugging을 봐도 알 수 있듯이 말로 설명하면 못풀던 문제도 해결되곤 한다.
예)
아이템 == 2 일때, 연합[2] == 0(미체크), 1 in 그래프[2] ? > False
아이템 == 4 일때, 연합[4] == 0(미체크), 1 in 그래프[4] ? > True
    ...
    while q:
        current = q.popleft()
        
        for item in graph[current]:
            if not union[item] and current in graph[item]:
                q.append(item)
                union[item] = 1
```