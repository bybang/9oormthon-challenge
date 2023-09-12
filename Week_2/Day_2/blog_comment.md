# Goormthon Challenge Day 7

### 구름톤 코딩테스트 챌린지 2주차 두 번째 날,

> 이번 문제는 행렬에서 요구 사항을 만족하는 값을 찾아내는 완전탐색 문제이다.

# 🧩 문제

# 🎯 전략
### 행렬을 입력받자
```python
matrix = []

for _ in range(N):
    row = list(input().split())
    matrix.append(row)
```

### 8방향 체크
행렬을 입력받고, 행렬을 탐색하는 방법을 알았다면, 각 칸별로 옆에 구름이 있는지 여부를 체크 해야한다.
방향을 설정하고 dx, dy 아래의 로직을 통해 한칸 한칸 대입해보며 체크하자
```python
for z in range(8):
            x = i + dx[z]
            y = j + dy[z]
            
            if y in (-1, N) or x in (-1, N):
                continue
```


### 그리디 메소드
마지막 답을 찾는 과정은 그리디로, 원하는 답을 찾았다면 더 찾지 말고 바로 리턴해주면 된다.

# 📌 느낀점
행렬을 입력받고, 탐색하는 과정을 BFS를 공부할 때 살짝 배워두어서 비교적 쉽게 로직을 짤 수 있었지만
8방향 체크와 입력받은 행렬의 범위를 넘어갈 때 어떻게 해야하는지 생각하고 응용해볼 수 있는 기회였다.

# 💻 풀이

```python
N, K = map(int, input().split())
# get input for 2 dimensional list
M = []
for i in range(N):
	M.append(list(map(int, input().split())))
	
# define directions (U, RU, R, RD, D, LD, L, LU)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def count_flag(N, K, M):
	count = 0
	
	for y in range(N):
		for x in range(N):
			flag_count = 0
			
			# If the spot contains 1 (cloud), ignore
			if M[x][y] == 1:
				continue
			# Loop through all directions
			for z in range(8):
				nx = x + dx[z]
				ny = y + dy[z]
				# Ignore if nx or ny goes over the map
				if nx < 0 or nx >= N or ny < 0 or ny >= N:
					continue
				
				flag_count += M[nx][ny] == 1
			# print("flag_count: ", flag_count)
			# Check if the flag count matches K
			if flag_count == K:
				count += 1
	print(count)

count_flag(N, K, M)
```


# 🔖 복습
```python
행렬을 입력받을 때 리스트 컴프리헨션을 통해 한 문장으로 축약하는 법
matrix = [list(input().split()) for _ in range(N)]

맵을 넘어가는지 여부에 대해, 부등호 대신 사용할 수 있는 방법
if x in (-1, N) or y in (-1, N):
    continue
```