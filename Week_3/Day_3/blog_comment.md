# Goormthon Challenge Day 13

### 구름톤 코딩테스트 챌린지 3주차 세 번째 날,

> 이번 문제는 어제 문제와 비슷하지만 완전 탐색의 개념도 필요한 행렬 탐색 문제이다.

# 🧩 문제

# 🎯 전략
### DFS / BFS
먼저 문제를 읽고 비재귀 DFS 함수(스택)를 활용할 것인지 BFS(큐)를 활용할 것인지 정한다.
이 전략 파트에서는 DFS식으로 풀어 연습하는 것을 선택했다.

### DFS 내에서의 조건과 함수의 역할을 확실히 하자
먼저 스택을 설정 했다면, 조건을 설정해주자. 현재 DFS 함수가 해야 하는 역할은 원본 행렬의 아파트 번호(1,2,3, ...)를
가지고 와서 아파트 번호 변수에다가 설정 해주는 것, 그리고 이 번호의 해당하는 아파트가 연결되어 있는가 체크, 연결된
아파트들이 총 몇 개나 있는지 세어서 리턴해주는 것이다.

```python
def DFS(i, j):
    stack = ([i, j])
    apt_num = matrix[i][j]
    count = 0
```

### 함수에 받은 좌표를 pop 처리해주고 방문했는지 체크 후 방문 처리하기
함수 DFS에 넘긴 변수는 i, j 이고 이것을 다시 `pop()` 처리 후 x, y에 넣어준다. 이로써 x, y를 좌표로 삼아
원본 행렬을 체크한다. 아파트 번호가 다르다면 무시해주고 아파트 번호가 같다면 0으로 바꿔준다. (방문처리)
이 때 방문한 아파트의 갯수를 세려면 `count += 1`을 해준다.

```python
def DFS(i, j):
    ...
    
    while q:
        x, y = stack.pop()
        
        if matrix[x][y] != apt_num:
            continue
        matrix[x][y] = 0
        count += 1
```

### 다음 좌표 설정과 함께 4방향 탐색
방문 처리 과정까지 끝났다면 다음은 그 좌표를 기준점으로 삼아 상하좌우를 탐색해준다. 주의할 점은 역시
다음 좌표의 값 `matrix[nx][ny]` 가 현재 아파트 번호와 같은지 까지 체크 후에 같지 않다면 무시해주는 것이다.
조건을 모두 만족시킨다면 `append((nx, ny))`를 통해 다음 좌표를 체크해주고 모든 과정 후엔 `count`를 리턴해준다.

```python
def DFS(i, j):
    ...
    
    while q:
        ...
        
        for a in range(4):
            nx, ny = x + dx[a], y + dy[a]
            
            if nx in (-1, N) or ny in (-1, N) or matrix[nx][ny] != apt_num:
                continue
                
            stack.append((nx, ny))
            
    return count
```

### 원본 행렬을 돌면서 데이터 처리하기
이제 함수 바깥에서 함수를 `call` 해줄 차례이다. 문제에서 주어진 입력 자료들을 받는 변수들을 설정해주고,
추가로 `housing_complex`를 통해 단지 번호별로 몇 개의 단지들이 있는지를 저장해 주어야 한다. 아파트 번호는
함수 `DFS()` 처리 후에는 바뀔 수 있기에 미리 설정해주도록 한다. `housing_complex` 는 M의 범위
`1 <= M <= 30`보다 큰 임의의 수를 지정해 주면 된다. `DFS()` 의 리턴값이 K 보다 크다면 문제에서
제시된 조건을 만족하므로 `housing_complex`의 단지 번호 배열에 하나씩 추가해주자
(예) 주어진 예시 1번 - 아파트 3번이라면 2개(K) 이상의 묶음이 총 2개이므로 배열 `housing_complex` 3번에, +1, +1)

```python
...

housing_complex = [0] * 31

for i in range(N):
    for j in range(N):
        # 만약 matrix[i][j] 가 존재한다면, 아래의 동작을 실행
        if matrix[i][j]:
            apt_num = matrix[i][j]
            
            if DFS(i, j) >= K:
                housing_complex[apt_num] += 1
```

# 📌 느낀점
어제의 문제에서 조건이 추가된 형식의 문제였다. 비슷한 문제였기에 로직을 짜는데 큰 문제는 없을 줄 알았는데,
아파트 단지의 수를 세어서 나타내는 변수 `count`, 그리고 함수 DFS/BFS 에서 리턴되는 값이 K보다 클 때 각각의
아파트 단지의 수를 저장해주는 배열을 동적 계획법에서의 메모이제이션을 활용해 풀어내는 것 이 두 가지의 활용법에서
좀 막혀서 돌아돌아 겨우 풀어냈다. 이번 문제도 DFS/BFS 둘 다 연습해 봤다. 확실히 해설에 나오는 방법에 비해서
코드가 지저분하다. 더 연습이 필요한 부분이라고 생각한다.

# 💻 풀이
- DFS

```python
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(i, j):
    stack = [(i, j)]
    apt_num = matrix[i][j]
    count = 0
    
    while stack:
        x, y = stack.pop()
        
        if matrix[x][y] != apt_num:
            continue
            
        matrix[x][y] = 0
        count += 1
        
        for a in range(4):
            nx, ny = x + dx[a], y + dy[a]
            
            if nx in (-1, N) or ny in (-1, N) or matrix[nx][ny] != apt_num:
                continue
                
            stack.append((nx, ny))
            
    return count

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
housing_complex = [0] * 31
    
for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            apt_num = matrix[i][j]
            
            if DFS(i ,j) >= K:
                housing_complex[apt_num] += 1

result, temp = 0, 0

for z in range(31):
    if temp <= housing_complex[z]:
        result = z
        temp = housing_complex[z]
        
print(result)
```

- BFS (My Solution)

```python
N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[None] * N for _ in range(N)]
housing_complex = [0] * 31
# directions(U,R,D,L)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def BFS(i, j, complex_num, visited):
	q = deque([(i, j)])
	visited[i][j] = True
	count = 1
	
	while q:
		x, y = q.popleft()

		for a in range(4):
			nx, ny = x + dx[a], y + dy[a]
			
			if nx in (-1, N) or ny in (-1, N):
				continue
			if matrix[nx][ny] == complex_num and not visited[nx][ny]:
				q.append((nx, ny))
				visited[nx][ny] = True
				count += 1
				
	return count
					
for i in range(N):
	for j in range(N):
		if not visited[i][j]:
			# if bfs
			if BFS(i, j, matrix[i][j], visited) >= K:
				housing_complex[matrix[i][j]] += 1
				
# find largest_complex in housing_complex
largest_complex = max(housing_complex)
for b in range(len(housing_complex)):
	if housing_complex[b] == largest_complex:
		result = b
		
print(result)
```


# 🔖 복습
```python
dp에서 배운 메모이제이션 기법 활용하기

이번 문제에서 가장 오래 걸렸던 부분은 housing_complex 의 기초 설정이었고,
나중에는 housing_complex를 단순히 리스트로 설정해보려고 했지만 잘 안됐다.

housing_complex = [0] * 31

행렬 탐색 조건 확실하게 정하기

for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            apt_num = matrix[i][j]
            
            if DFS(i, j) >= K:
                housing_complex[apt_num] += 1
                
마무리 조건 
문제에서 결국 요구하는 조건은 아파트 단지의 `번호`이다

result, temp = 0, 0

for z in range(31):
    if temp <= housing_complex[z]:
        result = z
        temp = housing_complex[z]

print(result)
```