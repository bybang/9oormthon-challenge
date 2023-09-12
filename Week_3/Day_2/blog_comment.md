# Goormthon Challenge Day 12

### 구름톤 코딩테스트 챌린지 3주차 두 번째 날,

> 이번 문제는 행렬에서의 효율적인 탐색을 요구하는 문제이다.

# 🧩 문제

# 🎯 전략
### 간단하게 재귀법으로 문제를 풀어보자
처음의 주어진 입력조건은 동일하다고 가정했을 때,
```python
def DFS(i, j):
    matrix[i][j] = 0 # make (i, j) visited
    
    for k in range(4):
       x, y = i + dx[k], j + dy[k]
       # if x = -1 or N or y = -1, N or if matrix[x][y] == 0, ignore
       if x in (-1, N) or y in (-1, N) or not matrix[x][y]:
           continue
       
       DFS(x, y)
...  
(아래의 매트릭스를 탐색해 발전기 갯수를 구하는 식도 동일하다)
```

### 런타임 에러가 난다면, `stack`을 이용한 비재귀 DFS를 활용하자
논리적인 오류는 없지만, 파이썬의 기본 깊이 제한은 1000번으로 제한되어 있고, 보통 코딩테스트의 경우에선
`sys`를 활용해 재귀 깊이 제한을 푸는 문제 또한 요구되지 않기에 이러한 방식보단 스택을 활용해보자

```python
def DFS(i, j):
    stack = [(i, j)]
    
    while stack:
        x, y = stack.pop()
        # if matrix[x][y](popped) == visited, ignore
        if not matrix[x][y]:
            continue
        matrix[x][y] = 0
    
        for k in range(4):
           nx, ny = i + dx[k], j + dy[k]
           # if nx = -1 or N or ny = -1, N or if matrix[nx][ny] == 0(visited), ignore
           if nx in (-1, N) or ny in (-1, N) or not matrix[nx][ny]:
               continue

           stack.append((nx, ny))
```


### 발전기 설치는 그룹에 하나씩
마지막 발전기의 수는, DFS 함수를 통해 찾은 그룹의 갯수와 동일하다. 따라서 매트릭스(마을)를 탐색한 후에
집을(1) 찾았다면 발전기를 설치하고, DFS 함수를 실행시켜 인접한 집들이 있는지 살펴본후 없다면 다시 돌아와
탐색을 진행하면 된다.

# 📌 느낀점
BFS와 DFS를 통해 풀 수 있었던 문제였지만 어제 배웠던 다이내믹 프로그래밍에 너무 매몰되어서 그쪽으로만
생각하고 있었던게 발목을 잡아 어렵게 문제를 풀어 나갔다. 제출은 BFS로 했지만 비재귀 DFS도 공부하기 위해
블로그에는 비재귀 DFS 풀이법으로 남겨놓는다. (일반적인 재귀법으로 풀었을때는 런타임 에러가 나온다.)

# 💻 풀이

```python
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

generator = 0

def DFS(i, j):
    stack = [(i, j)]
    
    while stack:
        x, y = stack.pop()
        # if matrix[x][y](popped) == visited, ignore
        if not matrix[x][y]:
            continue
        matrix[x][y] = 0
    
        for k in range(4):
           nx, ny = i + dx[k], j + dy[k]
           # if nx = -1 or N or ny = -1, N or if matrix[nx][ny] == 0(visited), ignore
           if nx in (-1, N) or ny in (-1, N) or not matrix[nx][ny]:
               continue

           stack.append((nx, ny))

for i in range(N):
	for j in range(N):
		if arr[i][j]:
			generator += 1
			DFS(i, j)

print(generator)
```


# 🔖 복습
```python
DFS에서 stack을 활용하는 법은

def DFS(i, j):
    stack = [(i, j)]
    
    while stack:
        x, y = stack.pop()
        
    ...
    stack.append((nx,ny))
    
위와 같고, 이때 (parenthesis)를 활용해 튜플을 스택에 넣어주고, append 할 때도 튜플을 넣어주자

BFS에서 queue를 활용하는 법은 먼저 collections 라이브러리에서 deque을 불러와준 뒤에

from collections impore deque

def BFS(i, j):
    queue = deque([(i, j)])
    
    while queue:
        queue.popleft()
    ...
    queue.append((nx, ny))
    
위와 같이 처리하면 된다.
```