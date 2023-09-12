# Goormthon Challenge Day 10

### 구름톤 코딩테스트 챌린지 2주차 다섯 번째 날,

> 이번 문제는 다양한 조건들은 만족하도록 구현하는 시뮬레이션 문제이다.

# 🧩 문제

# 🎯 전략
### 초기 세팅을 제대로 하자
1. 입력받을 변수들이 많다. 보드 크기(nxn) N부터, 두 플레이어의 좌표와 게임판까지 받아야 한다.
`Rg, Cg = map(int, input().split()`
`game_board = [list(input().split()) for _ in range(N)]`

2. 이동 범위와 방향 행렬도 따로따로 설정하고, 방향 좌표는 딕셔너리를 활용해 저장하자.
나중에 1L, 2R, 10D 등으로 되어있는 문자열을 숫자 따로 문자따로 나눌 것이다. `move`는 0으로
`command`는 `None`타입으로 채운 행렬을 만들어 놓고, 방향 좌표는 `key-value` 페어를 활용해
`direction` 변수에 저장한다.

3. 슬라이싱을 통해 게임판의 숫자부분과 문자부분을 나누고 각각의 변수에 넣어준다.
- 게임판을 직접 어레인지 하는 것보다는 임시 변수에 게임판을 넣고 바꿔주는 것이 좋다.
`temp = game_board[i][j]`
- 이동 범위는 1이 될 수도, 10, 100이 될 수도 있으니 마지막 문자까지 슬라이싱해서 int 처리 후 변수에 넣는다.
`move[i][j] = int(temp[:-1])`
- 이동 방향은 항상 마지막에 위치한다. index(-1)를 통해 방향을 찾고, direction을 이용하기 위한 key에 넣는다.
`key = temp[-1]`
- 앞서 설정한 key는 direction dictionary의 key에 들어가서 해당하는 value를 꺼내어 command에 넣어준다.
`command[i][j] = direction[key]`

### 방문한 서로 다른 칸의 개수를 반환하는 함수 만들기 - 1 
각 플레이어의 좌표와 맵의 크기를 변수로 받는 함수를 만들자. 좌표들을 직접 만지기 보다는 임시 변수를 생성해준다.
`visited` 행렬(방문 여부를 체크하는 행렬)을 만들어주고, 현재 위치도 방문처리한다.(0이면 미방문, 1이면 방문)
`visited[x][y] = 1 `

### 방문한 서로 다른 칸의 개수를 반환하는 함수 만들기 - 2
이제 반복문을 통해 주어진 맵의 `command`와 `move`에 따라서 한 칸씩 움직이며 방문했다면 방문처리를 할 것이다.
1. 가장 먼저 반복문을 시작하기 위한 초기값을 True로 설정해주고, 범위와 방향도 각각의 변수에 설정 해준다.

```python
game_play = True

while game_play:
    shift = move[x][y]
    dx, dy = command[x][y]
```

2. 그 이동 범위만큼 반복문을 돌리면서, 이동 하는 좌표가 맵 밖으로 나가면 각각의 처리를 해준다.

```python
for _ in range(shift):
    x = (x + dx)

    if x == N:
        x = 0
    elif x == -1:
        x = N - 1

    y = (y + dy)

    if y == N:
        y = 0
    elif y == -1:
        y = N - 1
```
2. (2-1) 위의 식을 두 문장으로 줄일 수 있다.

```python
다른 계산식은 실제로 대입해보면 되지만 (-1 % N) 의 경우(x+dx == -1)는
좀 다른데, 이를 알기 쉽게 설명하면 N = 5이고 N+1만큼 루프시킨 (i % N)의
값은 0, 1, 2, 3, 4, 0 이 나온다. 그리고 (-1 % N) 을 해보면 N-1의 값인
4가 나오게 되는 것을 확인할 수 있다. 따라서 우리가 원하던 좌표 값이
N을 넘으면 0으로 돌아오고, -1이 되면 N-1값이 되는 똑같은 로직이 되는것이다.

x = (x + dx) % N
y = (y + dy) % N
```

3. 방문한 좌표를 재방문한다면, 반복문의 조건을 False처리, 그렇지 않다면 방문처리 해주자.

```python
if visited[x][y] == 1:
    game_play = False
    break

visted[x][y] = 1
```

### 방문한 서로 다른 칸의 개수를 반환하는 함수 만들기 - 3
마지막으로 리턴 값은 방문한 노드의 총 개수를 다 더해주는 방식으로 구하면 된다.
첫번째 줄(리스트)의 값을 `sum(i) for i in visited` 로 구해주고 리스트에 넣어준다

`[sum(i) for i in visted]`

그리고 4개의 값(N x N 이기 때문에)이 들어가 있을텐데, 이 값들을 다 더해주면 끝이다.

`sum[sum(i) for i in visted]`



# 📌 느낀점
그냥 어려웠다. 당일 정답률도 평소와는 다르게 많이 낮았었고, 여러가지 소스들을 찾아보면서 최대한 풀려고
노력해 봤지만 결국 풀지 못했다. 마지막엔 어찌저찌 풀어서 제출했지만 테스트 FAIL까지 뜨면서 제출을 못했다.

이번엔 행렬을 게임보드, 이동 범위 행렬, 이동 방향 행렬, 마지막으로 방문했는지 체크하는 행렬까지, 4개의
행렬을 전부 활용해서 푸는 문제였기에 감을 못잡았던것 같다. 맵을 벗어나면 첫번째, 마지막 칸으로 돌아가는
로직을 짜는것도 어렵다고 생각했는데, 나머지 연산을 통해서 쉽게 구할 수 있었다.

2주차지만 부족함을 많이 느끼고, 더욱 많은 알고리즘 문제를 접해봐야 이런 문제도 보자마자 풀 수 있지 않을까
생각하게 하는 문제였다.

# 💻 풀이

```python
def visited_node(starting_x, starting_y, N):
    x, y = starting_x, starting_y
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    
    game_play = True
    
    while game_play:
        shift = move[x][y]
        dx, dy = command[x][y]
        
        for _ in range(shift):
            x = (x + dx) % N
            y = (y + dy) % N
        
            if visited[x][y]:
                game_play = False
                break
            
            visited[x][y] = 1
        
    return sum([sum(i) for i in visited])
    

N = int(input())
Rg, Cg = map(int, input().split())
Rp, Cp = map(int, input().split())

Rg -= 1
Cg -= 1
Rp -= 1
Cp -= 1

game_board = [list(input().split()) for _ in range(N)]

move = [[0] * N for _ in range(N)]
command = [[None] * N for _ in range(N)]
direction = {
    "U": [-1, 0],
    "R": [0, 1],
    "D": [1, 0],
    "L": [0, -1]
}

for i in range(N):
    for j in range(N):
        temp = game_board[i][j]
        
        move[i][j] = int(temp[:-1])
        
        key = temp[-1]
        
        command[i][j] = direction[key]
        
g_score = visited_node(Rg, Cg, N)
p_score = visited_node(Rp, Cp, N)

if g_score > p_score:
    print("goorm", g_score)
else:
    print("player", p_score)
```


# 🔖 복습
```python
두 개의 좌표가 나왔을 때는 처음부터 설정해주는 것도 방법이다.

조건이 여러가지가 나왔을 때는 하나 하나 작은 피스들로 잘라가며 확인해준다.
이번 문제는 게임판 말고도 이동 범위와 이동 방향, 방문 여부 체크까지 총 4개의
행렬을 설정해 주는 문제이다.

game_board = [list(input().split()) for _ in range(N)]
move = [[0] * N for _ in range(N)]
command = [[None] * N for _ in range(N)]

visited = [[0] * N for _ in range(N)]

방향을 설정해줄 때 너무 코드가 길고 반복되는 if-else 문을 사용하는 거 같다면
딕셔너리를 활용해서 key-value 페어에 넣어두고 그것을 이용하는 방식을 채택하자.

매트릭스를 루프하면서 x, y축을 헷갈리지 않도록 하고, 만약 문자와 숫자의 혼합
String일 경우 슬라이싱을 통해 자를 수 있다. 임시변수를 이용해서 미리 설정한
변수에 원하는 값을 넣어줄 수 있다.

for i in range(N):
    for j in range(N):
        temp = game_board[i][j]
        move[i][j] = int(temp[:-1])
        key = temp[-1]
        command[i][j] = direction[key]

while 반복문을 통해서 범위와 좌표를 받고 체크해가며 방문한 노드를 만나기 전까지
방문처리 해준다. 이 때 맵 밖으로 넘어갔을 때의 조건을 설정하는 방식은 다음과 같다.
또한 각 행을 더해준 뒤, 다시 그 행들의 합을 구하면 방문 노드의 총 갯수를 구할 수 있다.

while game_play:
    shift = move[x][y] # 범위
    dx, dy = command[x][y] # 해당 좌표(방향도)
    
    for _ in range(shift):
        x = (x + dx) % N
        y = (y + dy) % N
        
        if visited[x][y] == 1:
            game_play = False
            break
        
        visited[x][y] = 1

return sum([sum(i) for i in visted]) 
```