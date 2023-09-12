# Goormthon Challenge Day 15

### 구름톤 코딩테스트 챌린지 3주차 다섯 번째 날,

> 이번 문제는 그래프 탐색과 시뮬레이션의 혼합 문제이다.

# 🧩 문제

# 🎯 전략
### 문제 파악
1. 주어진 조건들 분석하기
문제에서 `N`은 행렬의 크기, `K`는 연결 요소의 수, `Q`는 좌표와 적고자하는 알파벳이다.

여기서 `Q`의 알파벳을 입력할때마다 행렬을 체크해서 연결 요소 `K`의 조건을 확인해서 지워주고, 마지막에
변경된 행렬을 출력해주면 된다. 행렬을 체크할때는 `발전기`문제에서 했듯이 4방향 체크를 통해 현재 좌표에서
같은 알파벳을 가지는 좌표를 체크, 그 좌표에서 4방향 체크하는 방식을 통해 연결되어 있는 모든 알파벳을 파악한다.

2. 입력 조건과 함수 설정
분석에서의 입력조건을 코드로 나타낸다면 다음과 같다.
추가로 행렬을 입력할때 한 문장이 아닌 한 단어씩 받고 싶다면 `input()`을 활용하자.

```python
N, K, Q = map(int ,input().split())
matrix = [list(input()) for _ in range(N)]

for _ in range(Q):
    i, j, d = input().split()
    
    DFS(i, j, d)
```

### DFS 함수 설정 - 1
1. 행렬에 문자 적어넣기
함수 `DFS`는 좌표와 알파벳을 받아서 그래프를 탐색해 연결요소를 파악할 것이다. 문제에서 문자를 적을 칸은
비어있음이 보장된다고 하였으므로, `matrix[i][j] = letter`를 통해 해당 좌표에 알파벳을 적어주자

```python
def DFS(i, j, letter):
    matrix[i][j] = letter
```
2. 스택과 방문 배열 설정
문자를 적었다면 해당 좌표를 기준으로 그래프를 탐색할 수 있도록 스택을 선언하고, 추가로 현재 포인트가 전에
방문 했던 포인트인지, 방문한 좌표는 총 몇 개인지 등을 기록하기 위해 `visited = set()`을 설정한다.
(반복 방문한 포인트는 삭제해주기 위해 `set()`을 이용해 준다)

```python
def DFS(i, j, letter):
    matrix[i][j] = letter
    
    stack = [(i, j)]
    visited = set()
```

### DFS 함수 설정 - 2
1. 스택을 활용한 그래프 탐색
스택 선언까지 완료했다면 그래프를 탐색할 차례이다. 현재 좌표를 방문한 적이 있다면 넘어가고, 아니라면 방문하는
현재 좌표를 방문처리 해준다. 그 뒤 4방향 탐색을 통해 원본 행렬의 다음 좌표의 문자가 현재 좌표의 문자와 같은지
체크해준뒤 같다면 스택에 넣어 같은 과정을 반복해준다.

```python
    ...
    
    while stack:
        x, y = stack.pop()
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            
            if nx in (-1, N) or ny in (-1, N) or matrix[nx][ny] != matrix[x][y]:
                continue
            
            stack.append((nx, ny))
```

2. 반복문 종료 후 연결 요소 체크
while 반복문이 종료됐다면 연결 요소 체크가 끝난 것이다 이제 반복문이 진행될 동안 방문했던 좌표들을 통해
연결 요소를 파악할 수 있다. 만약 연결 요소가 `K` 이상이라면 모든 연결 요소를 `"."`으로 바꿔주자
```python
    while stack:
        ...
        
    if len(visited) >= K:
        for x, y in visited:
            matrix[x][y] = "."
```

### 출력 조건
주어진 출력 조건을 보면 입력조건과 마찬가지로 모든 문자가 공백 없이 입력 되어 있다.
따라서 `''.join()`을 통해 변경된 행렬을 공백 없이 출력해주자.

```python
for row in matrix:
    print(''.join(row))
```


# 📌 느낀점
4주간의 챌린지의 마지막 문제이다. 문제 자체는 13일차 발전기(2) 문제와 유사한 조건으로 나온 문제라 크게 어려움은 없었지만
입력 조건에서 한 번 절었고, 출력 조건에서 한 번 더 절었다.

해설을 보니 조금 더 DRY한 코드를 짤 수 있지 않았을까 하는 아쉬움은 있었지만 전반적으로는 무난했던 문제였다.

# 💻 풀이
```python
def DFS(i, j, letter):
    matrix[i][j] = letter
    
    stack = [(i, j)]
    visited = set()
    
    while stack:
        x, y = stack.pop()
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            
            if nx in (-1, N) or ny in (-1, N) or matrix[nx][ny] != matrix[x][y]:
                continue
                
            stack.append((nx, ny))
            
    if len(visited) >= K:
        for x, y in visited:
            matrix[x][y] = "."
    
N, K, Q = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(Q):
    i, j, d = input().split()
    
    DFS(int(i) - 1, int(j) - 1, d)
    
for row in matrix:
    print("".join(row))
```
- My Solution
```python
from collections import deque

# BFS should return the modified matrix
def BFS(x, y):
	visited = [[0] * N for _ in range(N)]
	q = deque([(x, y)])
	
	visited[x][y] = 1
	connected = []
	
	while q:
		current_x, current_y = q.popleft()
		
		connected.append((current_x, current_y))
		
		for i in range(4):
			nx, ny = current_x + dx[i], current_y + dy[i]
			
			if nx in (-1, N) or ny in (-1, N):
				continue
			if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
				q.append((nx, ny))
				visited[nx][ny] = 1
			
	return connected
	
	

N, K, Q = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
matrix = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(Q):
	y, x, d = input().split()
	x, y = int(y) - 1, int(x) - 1
	
	matrix.append((x, y, d))
	
for x, y, letter in matrix:
	graph[x][y] = letter
	
	connected = BFS(x, y)
	count_connected = len(connected)
	
	if count_connected >= K:
		for x, y in connected:
			graph[x][y] = "."
			
for i in graph:
	print("".join(i))
```


# 🔖 복습
```python
연결된 문자열을 한 글자씩 분리해 입력 받고 싶다면
matrix = [list(input()) for _ in range(N)]

방문 체크 및 연결 요소의 길이를 위한 리스트 set()으로 만들어주기
visited = set()

방문 배열에 .add() .append()를 할 때는 하나의 정보만 받으므로 튜플 처리
visited.add((x, y))
visited.append((nx, ny))

변경된 행렬은 전부 탐색할 필요 없이 row만 탐색해주면서 .join()을 통해 리스트
한 단어로 만들어서 프린트 해주기
for row in matrix:
    print("".join(row))
```