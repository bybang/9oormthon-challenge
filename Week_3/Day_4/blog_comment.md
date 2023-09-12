# Goormthon Challenge Day 14

### 구름톤 코딩테스트 챌린지 3주차 네 번째 날,

> 이번 문제는 그래프, 노드, 간선에 대한 개념과 인접리스트 개념 등을 묻는 문제이다.

# 🧩 문제

# 🎯 전략
### 입력조건 설정하기
1. 인접 리스트 `adjacency list` 설정하기
`N + 1` 만큼의 인접리스트를 생성해준다. 이 때 밑에서 변수로 받는 `s, e`의 범위가 `1 <= s, e <= N` 이기에
인덱스를 맞춰주려면 `[s - 1], [e - 1]` 이와 같이 처리해주어야 하기에 차라리 `N + 1` 을 해주어 맞춰 준다. 
```python
graph = [[] for in range(N + 1)]
```
2. 양방향 간선 (edge) 
`graph`의 설정이 끝났다면 이제 그래프에 노드와 간선을 입력받아 넣어준다.
```python
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
```
3. 방문 배열
`visited` 배열을 설정해 원본 배열을 건드리지 않고 방문한 노드의 개수를 처리할 수 있는
배열을 설정해주자.
```python
visited = [0] * (N + 1)
```

### BFS 함수 설정
1. 시작 노드 받고 방문처리
시작노드는 처음 입력받은 `K` 이다. 이것을 `start_node` 로써 함수에 받고, `current_node` 를
`pop()` 을 통해 받아준 뒤에 방문 배열에 방문처리 (1) 해주자.

```python
def BFS(start_node):
    q = deque([start_node])
    
    while q:
        current_node = q.popleft()
        visited[current_node] = 1
```
2. 반복문을 통해 현재 노드에서 방문 가능한 노드들을 탐색
`for-loop`을 통해 그래프 탐색을 진행한다. 이 때 그래프의 리스트는 정렬되있는 상태가 아니므로 `sorted()`를 통해
오름차순 정렬이 될 수 있게 정렬해주자.

```python
    while q:
        ...
        for item in sorted(graph[current_node]):         
```
3. 탐색은 방문 가능한 노드중 가장 작은 순으로, 방문하지 않은 노드들도 처리하자
주어진 조건에 `방문할 수 있으면서 번호가 가장 작은 노드로 이동한다`는 말이 있기에 위에서 정렬을 해주었다.
다음으로 방문하지 않은 노드를 확인하면서, 방문하지 않았다면 큐에 넣어준다. 반복문이 종료되면 더 이상 이동할 수 있는
노드가 없다는 뜻이므로, 현재 노드는 마지막으로 방문한 노드가 된다.

```python
    while q:
        ...
        for item in sorted(graph[current_node]):
            if not visited[item]:
                q.append(item)
                break
    else:
        return current_node
```

### 함수의 리턴 값과 방문 배열 활용해 답변 도출하기
함수에서의 리턴 값은 가장 마지막으로 방문한 노드의 번호를 의미하며, 방문 배열을 통해 1이 체크된 곳들의 합을 구하면 방문 노드 개수를 구할 수 있다.


# 📌 느낀점
그래프는 처음 접해보는 터라 영상을 찾아보며 풀어봤다. 유니온 파인드라던지 그런 문제형식으로 접근하는 줄
착각해서 한참 풀어봤는데 안되길래 찾아보고 BFS로 풀었더니 오히려 알고 있는 개념으로도 충분히 풀 수 있는
BFS 문제였다. 중요한 점은 인접리스트(adjacency list)를 알고 활용할 수 있는지 인접 리스트와 그래프,
노드, 간선의 개념을 아는지를 묻는 문제였다는 것. 이 부분을 몰라 처음에 시간을 많이 잡아 먹었다.

역시나 코테는 경험이 중요한거 같고, 좀 더 많은 문제를 접해볼 필요성을 챌린지를 진행하면서 항상 느낀다.

# 💻 풀이

```python
from collections import deque

def BFS(start_node):
    q = deque([start_node])
    
    while q:
        current_node = q.popleft()
        visited[current_node] = 1
        
        for item in sorted(graph[current_node]):
            if not visited[item]:
                q.append(item)
                break
        else:
            return current_node
        
N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
visited = [0] * (N + 1)

result = BFS(K)

print(sum(visited), result)
```


# 🔖 복습
```python
인접 리스트의 방식으로 그래프 만들고, 입력받은 데이터로 양방향 간선 그래프 그린 뒤, 방문 처리 기록할 배열 만들기

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [0] * (N + 1)

시작 노드를 입력 받았다면, 시작 노드를 활용해서 큐 생성후 시작 노드에 연결된 노드들 탐색하기(리스트 정렬 처리!)
반복문 안에서 각각의 노드에 연결된 노드들을 확인해주면서, 방문하지 않은 노드는 큐에 넣어주기
반복문이 종료되었다면 마지막으로 방문한 노드는 현재 노드이므로 현재 노드 번호 리턴해주기

def BFS(start_node):
    q = deque([start_node])
    
    while q:
        current_node = q.popleft()
        visited[current_node] = 1
        
        for item in sorted(graph[current_node]):
            if not visited[item]:
                q.append(item)
                break
        else:
            return current_node
```