# Goormthon Challenge Day 9

### 구름톤 코딩테스트 챌린지 2주차 네 번째 날,

> 이번 문제는 (구)폭탄 구현하기에 조건을 추가한 완전탐색 문제다. 무려 N사 기출 변형문제라고 한다!

# 🧩 문제

# 🎯 전략
### 게임보드 행렬과 점수 계산 행렬 따로 선언하기
1. 첫 행렬은 구름 깃발 찾기에서와 같은 방법으로 선언한다.
`matrix = [list(input().split()) for _ in range(N)]`
2. 그리고 점수 행렬을 통해 원본 게임보드를 건드리지 않고 점수 계산을 할 수 있게 하자.
`score =[[9] * N for _ in range(N)]`

### 제자리 체크 및 영역과 벽("#")을 만났을 때의 조건문 만들기
폭탄이 떨어진 자리와 4방향 모두를 체크하기 위해서 dx, dy를 제자리를 포함해서 5방향으로 선언해주자.
다섯 가지의 방향을 체크하면서 영역 밖으로 벗어나는지, 그리고 "#"를 만나지 않는지 체크하자.
이때 "#"은 가장 마지막에 체크해줘야한다. 왜냐하면 조건이 하나라도 만족하면 바로 `True` 값이
되어버리는 `or` 조건문 특성상 처음부터 체크한다면 영역밖을 체크하지 않고 `True`가 나오기 때문.

### 최대 값을 찾는 리스트 컴프리헨션
`score` 행렬은 리스트를 각 원소값으로 가진다. 각 `score`의 `i`에 대한 `i`의 최대값을 구해보면,
`temp = [max(i) for i in score]` 가 된다. 각 x축의 최댓 값을 구했다고 보면 된다.
이제 이 `temp`의 값들 중 최대값을 구하면, `result = max(temp)`가 되고, 이를 줄이면
`result = max([max(i) for i in score])`가 된다. (위의 x축 최대값을 구하는 식`temp`를 바로 넣음)



# 📌 느낀점
결론론부터 말하면 다 풀지 못했다. 폭탄 구현하기를 풀어보고 그 로직을 활용해서 풀어보려고 했는데,
잘 되지를 않고 BFS의 `deque` library를 통해 `queue`를 추가한 방법을 써봤지만 타임오버가 났다.

또, 두개의 `matrix`를 통해 답변을 도출해낼 수 있다는 점도 새롭게 배운점이다.

# 💻 풀이

```python
N, K = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]
score = [[0] * N for _ in range(N)]

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

for _ in range(K):
	x, y = map(int, input().split())
	x -= 1
	y -= 1
	
	for k in range(5):
		nx = x + dx[k]
		ny = y + dy[k]
		
		if ny < 0 or ny >= N or nx < 0 or nx >= N or arr[ny][nx] == "#":
			continue
		
		if arr[nx][ny] == "@":
			score[nx][ny] += 2
		else:
			score[nx][ny] += 1

result = 0

result = max([max(i) for i in score])

print(result)
```


# 🔖 복습
```python
게임보드가 주어졌을 때는 그 매트릭스를 건드리지 않고, 새로운 행렬을 만들어 점수 계산을 하자
matrix = [list(input().split() for _ in range(N)]
score = [[0] * N for _ in range(N)]

제자리 체크할때는 5방향 체크하고, 밖이거나 "#"라면 폭탄값 변하지 않게 하기 위해 조건문 설정
이 때, 조건문의 순서를 파악해서 배치해야한다.
dx = [0, 1, 0, 1, -1] dy = [0, 0, 1, 0, -1]
if k in range(5):
    ...
    if nx < 0 or nx >= N or ny < 0 or ny >= 0 or matrix[nx][ny] == "1":
    ...

행렬 안에서 최댓 값을 도출해 낼 때는 먼저 x축 최댓 값을 구하고,
그 최댓 값들의 최댓 값(y축)을 한 번 더 비교해주자.
temp = [max(i) for i in score]
result = max(temp)
```