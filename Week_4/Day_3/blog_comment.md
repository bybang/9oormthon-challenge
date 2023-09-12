# Goormthon Challenge Day 18

### 구름톤 코딩테스트 챌린지 4주차 세 번째 날,

> 이번 문제는 다이내믹 프로그래밍과 시뮬레이션의 혼합 문제이다

# 🧩 문제

# 🎯 전략
### 문제 이해하기
먼저 문제를 읽고 문제에서 요구하는 사항이 무엇인지 파악해야 한다. 반직선 뭐라고 되어 있는데, 결국 중요한 건
출발하는 지점과, 방향을 받아서 가로/세로 라인을 그리고 다 그린 뒤에 그 라인들의 "교점"을 찾으면 되는 문제였다.

### 교점 기록하기
다이내믹 프로그래밍(이하 dp)의 메모이제이션을 활용해 가로/세로 라인이 각 좌표에 몇개나 지나가는 지 기록해준다.
`[0,0]` 을 각각 지나간 세로선의 개수 / 가로선의 개수 로 지정해준 뒤 N번 만큼 가로로, N번 만큼 세로로 만들어서
행렬의 크기와 동일하게 만들어 준다.

```python
matrix = [ [ [0,0] for _ in range(N) ] for _ in range(N)]
```

### 좌표와 방향 받아서 가로/세로선 그리기
M개 만큼의 좌표와 방향이 있고 (y, x) 는 헷갈리기 쉬우니 서로 바꿔준 뒤 정수 처리 후 (0,0)부터 시작한다고 정의하자.

```python
for _ in range(M):
    y, x, commmand = input().split()
    
    x, y = int(y)-1, int(x)-1
```

다음으로 각 방향별로 가로 혹은 세로선이 지날 때 마다 설정해둔 지나간 선의 개수 좌표에 1씩 더해준다.
세로선을 그릴 때는 y는 그대로 두고 x의 변수를 바꿔주며 해당 좌표[0] (지나간 선의 개수) `matrix[i][y][0]`에
+1 만큼 해준다. 이 때 설정한 맵을 넘어가지 않도록 범위를 고려하며 x의 변수를 바꿔주어야 한다.

가로선을 그릴때도 위에서 고려한 변수들을 반대로만 설정해준다면 가로선과 세로선이 지나가는 개수를 모두 기록할 수 있다.
가로선이 지나간 것을 기록할 때는 미리 설정해 둔 dp값중 두 번째 즉, 해당 좌표[1]을 써주는 것 잊지말자.

```python
for _ in range(M):
    ...
    
    if command == "U":
        for i in range(x + 1):
            matrix[i][y][0] += 1
    elif command == "D":
        for i in range(x, N):
            matrix[i][y][0] += 1
            
    elif command == "R":
        for j in range(y, N):
            matrix[x][j][1] += 1
    elif command == "L":
        for j in range(y + 1):
            matrix[x][j][1] += 1
```

### 답안 도출하기
여기까지 마쳤다면 현재 dp 테이블에는 그려놓은 가로선의 개수, 세로선의 개수가 따로 기록이 되어 있을 것이다.
이 가로선의 개수와 세로선의 개수가 겹치는 부분이 교점이므로 이 부분을 구해주는 식은 가로선의 수 * 세로선의 수 이다.

```python
result = 0

for i in range(N):
    for j in range(N):
        result += matrix[i][j][0] * matrix[i][j][1]
```

# 📌 느낀점
문제를 이해한다면 그래도 쉽게 풀이를 떠올릴 수 있는 문제지만 문제를 해석하는 데 너무 오래걸렸다.
확실히 많이 접해보지 않아서 그런가 가로/세로 라인을 따로 그려서 마지막에 합친다는 개념은 생소했다.

하지만 접근법을 그쪽으로 가져가 보니 문제 풀이는 떠올릴 수 있어서 다행이였다. 마지막 주간에는 문제들이
어려워지고 있는 거 같은 느낌이 드는데, 이런 유형 문제들을 많이 풀어보지 않아서 그런거 같아 이쪽 문제들도
꾸준히 풀어야겠다는 생각이 든다.

# 💻 풀이
```python
N, M = map(int, input().split())
matrix = [[[0, 0] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    y, x, command = input().split()
    x, y = int(y) - 1, int(x) - 1
    
    if command == "U":
        for i in range(x + 1):
            matrix[i][y][0] += 1
    elif command == "D":
        for i in range(x, N):
            matrix[i][y][0] += 1
    elif command == "L":
        for j in range(y + 1):
            matrix[x][j][1] += 1
    elif command == "R":
        for j in range(y, N):
            matrix[x][j][1] += 1
            
result = 0

for i in range(N):
    for j in range(N):
        result += matrix[i][j][0] * matrix[i][j][1]
        
print(result)
```

- My Solution

```python
def search(x, y, command, line):
	directions = {
		"U": (-1, 0),
		"R": (0, 1),
		"D": (1, 0),
		"L": (0, -1)
	}

	x_current = x
	y_current = y

	for _ in range(1, N + 1):
		if 1 <= x_current < N + 1 and 1 <= y_current < N + 1:
			line[x_current][y_current] += 1
			x_current += directions[command][0]
			y_current += directions[command][1]

N, M = map(int, input().split())
matrix = []

for _ in range(M):
	y, x, command = input().split()
	matrix.append(((int(y), int(x)), command))

# print(matrix)

result = 0

horizontal = [[0] * (N + 1) for _ in range(N + 1)]
vertical = [[0] * (N + 1) for _ in range(N + 1)]

for (x, y), command in matrix:
	if command == "U" or command == "D":
		search(x, y, command, horizontal)
	elif command == "L" or command == "R":
		search(x, y, command, vertical)

for i in range(1, N + 1):
	for j in range(1, N + 1):
		result += horizontal[i][j] * vertical[i][j]

print(result)
```


# 🔖 복습
```python
(가로선의 수, 세로선의 수)를 행렬의 각 좌표에 넣어 기록하기

[[[0, 0] for _ in range(N)] for _ in range(N)]

방향 받고 탐색 범위가 매트릭스 이상 넘어가지 않게 지정해준 뒤 가로/세로선 그리고 위에서 만든 변수에
해당 좌표를 지나가는 선의 개수 기록하기.

if command == "L":
    for j in range(y + 1):
        matrix[x][j][1] += 1
elif command == "R":
    for j in range(y, N):
        matrix[x][j][1] += 1
        
입력 받은 모든 데이터로 가로/세로선 그리기를 완료했다면 매트릭스를 탐색하며 좌표들에 기록된 데이터를
바탕으로 교점의 개수 찾기 (x,y)에 가로선 둘, 세로선 하나가 지나간다면 2*1 둘, 둘이면 2*2가 교점의 개수

for i in range(N):
    for j in range(N):
        result += matrix[i][j][0] * matrix[i][j][1]
```