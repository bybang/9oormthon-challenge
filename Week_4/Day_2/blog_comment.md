# Goormthon Challenge Day 17

### 구름톤 코딩테스트 챌린지 4주차 두 번째 날,

> 이번 문제는 그래프의 컴포넌트 개념과 다중 조건 정렬을 활용한 유형을 복합적으로 섞어 놓은 문제이다.

# 🧩 문제

# 🎯 전략
### 문제 요구 조건 이해하기
문제를 풀기 위해 구해야 하는 조건은 세 가지로, 다음과 같다.
1. 컴포넌트(유니온)에 속한 통신 회선(간선/엣지)의 개수
2. 컴포넌트에 속한 컴퓨터(노드)의 개수
3. 컴포넌트에 속한 컴퓨터 중 가장 작은 컴퓨터의 번호

### 무엇을 출력하는가?
출력 조건에 나와 있는 조건을 만족시키려면,
1. 밀도(통신 회선의 개수 / 컴퓨터의 수)가 가장 높은 컴포넌트여야 하고
2. 만약 밀도가 같다면 컴포넌트(유니온)에 속한 컴퓨터의 수가 가장 적어야 하며
3. 만약 1, 2의 조건 모두 동일할 경우 컴포넌트에 속한 컴퓨터의 번호가 작은 쪽을 출력한다.

즉 컴포넌트를 정렬해주고 컴포넌트의 첫번째 값을 비교하면 3번의 조건을 만족시킬 수 있을 것이다.

### 데이터 입력처리
먼저 그래프를 탐색하기에 앞서 원하는 탐색기법(여기서는 BFS)을 정했다면 탐색 후 어떤 데이터로 가지고 올 것인가
BFS에 넣어야 하는 데이터는 무엇인가 정도를 생각해보자. 그 외에는 16일차에서 데이터를 입력받던 방식과 비슷하다.

다만 양방향 간선이기에 그래프를 그릴때 양쪽 모두 연결해 주는 것을 잊지말자.

```python
N, M = map(int, input().split())
# 인접 리스트 설정
graph = [[] for _ in range(N + 1)]
# 방문 배열 설정
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 탐색 후 원하는 데이터셋(리스트(컴포넌트=유니온)와 밀도)
result, density = [], 0

for i in range(1, N + 1):
    if not visited[i]:
        # 현재 컴포넌트(리스트), 임시 밀도를 가지고 올 것이다.
        current_comp_list, tempDen = BFS(i)
        ...
```

### 그래프 탐색하기 - 1
이제 그래프를 탐색하여 원하는 조건(현재 체크하는 컴포넌트와 해당 컴포넌트의 밀도)을 뽑아내자.

`component`는 `set()` 처리를 통해 데이터를 `hashing` 해주어야 시간 복잡도를 줄일 수 있는데,
쉽게 말하자면 `dictionary`의 `key-value` 탐색을 활용하는 방식으로 이 방식의 시간 복잡도는
`O(1)`의 상수시간을 지니게 된다. 자세한건 영어 유튜브나 블로그 글을 참고했다.

다음 과정은 16일차 집합에서 배운것과 유사한 과정이고, 컴포넌트에 현재 탐색하는 노드를 추가해주고
인접 리스트로 이루어진 그래프중 그래프[현재노드]에 해당하는 아이템을 꺼내어 이 아이템을 방문한 적
있는지 체크해줌으로써 간선이 연결된 그래프인지 체크하고 연결되어 있다면 같은 컴포넌트에 넣어준다.

```python
def BFS(start):
    q = deque([start])
    
    component = set()
    
    while q:
        current = q.popleft()
        
        if visited[current]:
            continue
        
        visited[current] = 1
        component.add(current)
        
        for item in graph[current]:
            if not visited[item]:
                q.append(item)
```

### 그래프 탐색하기 - 2
한 그룹의 컴포넌트를 생성했다면 컴포넌트 안에서 회선(간선/엣지)의 수 또한 찾아야 한다. 회선의 수까지 찾아줘야
밀도를 구할 수 있기 때문이다.

이해하기 쉽게 컴포넌트의 `number` 라는 이름으로 지정했지만 원래 기본적인 `str, number, int` 등은
변수 이름으로 사용하지 않는 것이 좋긴 하다.

다시 한 번 그래프를 체크할때 `item`을 활용해 체크해주고, 이번에는 그래프[컴포넌트 안의 n번째 수]를 체크해보자.
그래프를 탐색해서 (컴포넌트의 n번째 수)의 노드가 컴포넌트에 속해있다면 컴포넌트의 내부 회선이다.

컴포넌트를 리턴해 줄 때 리스트로 바꾸어 오름차순 정렬해주고, 밀도까지 리턴하면 초기에 목표했던 데이터를 가져올 수 있다.

```python
    while q:
        ...
        
        ...
    # 내부 회선 기록용 변수
    edge = 0
    
    for number in component:
        for item in graph[number]:
            if item in component:
                edge += 1
                
    return sorted(list(component)), edge / len(component)
```

### 함수에서 뽑아낸 데이터를 바탕으로 조건문 활용해서 답 도출해내기
다시 한 번 출력 조건을 정리하자면 뽑아낸 데이터셋을 바탕으로 (1. 밀도, 2. 컴퓨터의 수, 3. 컴포넌트 중 가장 작은 수)이다.
이제 BFS를 통해 뽑아낸 컴포넌트들을 비교하면서 출력조건에 맞는 답만 도출해 낼 수 있다.

밀도 `density`는 실수 값이기 때문에 실수 값 오차가 발생할 수 있는데, 이를 없애기 위해 절대값 `abs()`를 해주고
현재 밀도와 구해놓은 밀도간의 오차가 아주 작은 경우를 두 밀도가 같은 경우로 취급해 처리해준다.

밀도가 같다면 두 번째 조건인 컴퓨터의 수를 확인해주고, 컴퓨터의 수도 같다면 컴포넌트 리스트중 가장 첫 번째`[0]`를 비교해준다.

마지막으로 리스트 그대로 출력하면 답변에서 요구하는 양식이 아니기 때문에 파이썬의 `*(asterisk)`기능을 활용해 출력한다.

```python
...

for i in range(N + 1):
    if not visited[i]:
        current_comp_list, tempDen = BFS(i)
        
    if abs(tempDen - density) < 1e-8:
        # 결과 리스트의 컴퓨터의 수가 현재 체크하는 컴포넌트의 컴퓨터의 수보다 많을 때만 체크해주면 된다.
        if len(result) > len(current_comp_list):
            result = current_comp_list
            density = tempDen
        elif len(result) == len(current_comp_list):
            if current_comp_list[0] < result[0]:
                result = current_comp_list
                density = tempDen

    elif tempDen > density:
        result = current_comp_list
        density = tempDen
        
print(result)
```

# 📌 느낀점
못 풀었다. 그래프에 대한 이해도가 떨어지는건지 16일차 문제도 이해하는 데 어려웠는데 17일차 문제는 분석에 실패했다.
컨디션이 별로 좋지 않아서 분석을 제대로 하지 못한 것도 있지만 역시나 기본적인 그래프에 대한 이해도 부분이 부족한게
제일 큰 원인이 아닐까 싶다.

주어진 풀이를 통해 확실하게 복습해서 16, 17일차를 이해한 뒤 18일차 문제로 넘어가야 할 것 같다.

# 💻 풀이

```python
from collections import deque

def BFS(start):
    q = deque([start])
    component = set()
    
    while q:
        current = q.popleft()
        
        if visited[current]:
            continue
        
        visited[current] = 1
        component.add(current)
        
        for item in graph[current]:
            if not visited[item]:
                q.append(item)
                
    edge = 0
    
    for number in component:
        for item in graph[number]:
            if item in component:
                edge += 1
                
    return sorted(list(component)), edge / len(component)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result, density = [], 0

for i in range(1, N + 1):
    if not visited[i]:
        current_comp_list, tempDen = BFS(i)
        
    if abs(tempDen - density) < 1e-8:
        if len(current_comp_list) < len(result):
            density = tempDen
            result = current_comp_list
        elif len(current_comp_list) == len(result):
            if current_comp_list[0] < result[0]:
                density = tempDen
                result = current_comp_list
    elif tempDen > density:
        density = tempDen
        result = current_comp_list
        
print(*result)
```


# 🔖 복습
```python
주어진 조건 활용하여 BFS에서 어떤 데이터 도출해 낼 것인가 정하기
현재 조건 하에서 BFS에서 뽑아낼 것은 밀도와 컴포넌트(리스트)이고, 이것을 바탕으로 두 번째
출력 조건(밀도, 컴포넌트 개수 등..)을 만족하는가 여부를 따져봐야 한다.

result, density = [], 0

for i in range(1, N+1): # 1부터 N까지 돌면서
    if not visited[i]: # 방문배열[i]에 방문했는지 여부를 체크한다
        current_comp_list, tempDen = BFS(i)

BFS의 큐와 while 반복문 통해 그래프를 탐색하며 현재 체크하는 노드와 연결되어 있는 노드들을
한 컴포넌트로 묶어준다. 방문한 노드는 방문 배열에 방문처리해주면서 두 번 방문하지 않도록 한다.

컴포넌트는 set() 함수를 이용해 해쉬 처리해 주어 O(1)의 시간복잡도를 가지게 만들어준다.

def BFS(start):
    q = deque([start])
    component = set()

    while q:
        current = q.popleft()
        
        if visited[current]:
            continue
            
        visited[current] = 1
        component.add(current)
        
        for item in graph[current]:
            if not visited[item]:
                q.append(item)
                
while 반복문을 통해 컴포넌트를 구했다면 컴포넌트 안의 노드들의 간선(엣지)개수를 파악해준다.
함수 종료시에는 정렬된 컴포넌트를 리스트에 담아주고, 밀도는 간선개수 / 컴퓨터(노드)의 수 로 구해 리턴한다.

    ...
    edge = 0
    
    for number in component:
        for item in graph[number]:
            if item in component:
                edge += 1
                
    return sorted(list(component)), edge / len(component)
    
출력 조건을 확인하자.
밀도가 실수값을 가지므로 == 보다는 abs()를 활용해 오차가 엄청 작은 값일 때(1e-8)를 밀도가 같다고 생각해준다.

...

for i in range(1, N + 1):
    if not visited[i]:
        current_comp_list, tempDen = BFS(i)
    
    if abs(tempDen - density) < 1e-8:
        ...
    elif tempDen > density:
        density = tempDen
        result = current_comp_list
        
밀도가 같거나 현재 밀도가 구해놓은 밀도보다 클때 현재 밀도와 컴포넌트 리스트가 구하고자 하는 답이 된다.
두 번재로 밀도가 같을 때 컴포넌트 리스트의 컴퓨터(노드)수를 비교해서 더 적은것이 구하고자 하는 답이므로

...
    if abs(tempDen - density) < 1e-8:
        if len(current_comp_list) < len(result):
            density = tempDen
            result = current_comp_list

마지막으로 밀도도 같고, 컴포넌트 리스트 안의 컴퓨터 수도 같다면 가장 작은 컴퓨터 번호를 비교해
더 작은 번호를 가지고 있는 리스트가 구하고자 하는 답이 된다. 
            
        elif len(current_comp_list) == len(result):
            if current_comp_list[0] < result[0]:
                density = tempDen
                result = current_comp_list
                
리스트를 출력할때 *(asterisk) operator 를 활용해 출력하면 리스트 안의 변수들을 콤마 없이
공백(' ')과 함께 출력할 수 있다.
```