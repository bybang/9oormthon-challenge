# Goormthon Challenge Day 15

### 구름톤 코딩테스트 챌린지 3주차 다섯 번째 날,

> 이번 문제는 그리디의 응용 문제이다.

# 🧩 문제

# 🎯 전략
### 문제를 이해하자
1. 주어진 조건들 분석하기
문제에서 `N`은 과일의 종류이고 `한 개씩` 있다고 한다. 가격은 price, 포만감은 calories로 표현하기로 하자.
특이한 조건을 제시한 것은 조각 단위로 과일 구매가 가능하다는 것과 이 때의 조각의 가격은 1이라는 것. 

2. 예제 분석하기
첫 번째 예제에서의 설명을 통해서 문제를 어떻게 풀어나가야 할지 감을 잡을 수 있다. 먼저 칼로리를 기준으로
내림차순 정렬해보았지만 이것으로는 문제를 풀 수 없었다.
```python
35 30 12 8 7 5 = c
7  10  3 2 1 1 = p
```

그럼 다음으로 주어진 조건은 조각 단위이므로, `c // p`를 해주고 다시 한 번 내림차순 정렬해주면 조건에 만족하는
답을 구할 수 있다. (1+7+1+3) + 1 == 13 / (7+35+5+12) + 4 == 63
```python
7 5  5  4  4  3 == c/p in order, calories per piece
1 7  1  3  2  10 == price
7 35 5. 12 8  30 == calories
```

### PseudoCode를 함수로 변환하자 - 1
1. 데이터 input용 변수들 설정하기
과일의 종류 N과 가지고 있는 돈 K를 입력받는 것은 크게 어렵지 않다.
과일 가격과 포만감(칼로리)를 가지고 있는 리스트까지 설정해주면 인풋 데이터용 변수는 끝이다.
```python
N, K = map(int, input().split())
fruits = [list(map(int, input().split())) for _ in range(N)]
```
2. 데이터 정렬 후 반복문 설정하기
위의 예제에서 분석했듯이, 과일을 정렬해주어야 하는데, 기준은 `c // p`로 해야하므로 아래와 같이 표현한다.
`lambda`를 활용해 한 문장으로 처리해주고, `while` 반복문을 가진 돈을 기준으로 설정해주자.
```python
fruits.sort(key = lambda x : x[1] // x[0])

while K:
```

### PseudoCode를 함수로 변환하자 - 2
1. 각 과일의 변수 [price, calories] 를 pop을 통해 꺼내어 주기
앞서 정렬해준 과일 리스트의 과일을 꺼내기 위해서 `pop()`을 활용해주면, 리스트 오른쪽에서부터 데이터를
꺼내올 수 있다. 과일의 데이터가 두 가지 이므로 두 가지 변수를 선언해주어야 각각의 값을 빼낼 수 있다.
```python
while K:
    price, calories = fruits.pop()
```

2. if-else 조건 활용해 총 합 칼로리 계산해주기
문제에서 구하고자 하는 것은 구매한 과일의 최대 포만감의 합이다. 가지고 있는 돈 K와 과일의 가격을 비교한 뒤
과일의 가격이 K보다 작으면 통째로 구매한다.(그리디이기에 큰 것부터 빼주면 되고, 과일은 1개씩 밖에 없다)
```python
while K:
    ...
    if K >= price:
        total_cal += calories
        K -= price
```
마지막으로 과일의 가격이 남은 돈 K보다 크다면 해당 과일을 조각내주고 조각의 포만감 만큼 더해준 뒤 반복문을 종료하기 위해
`k = 0`를 해준다. 이 때 과일을 모두 구매해도 소지금 K가 남을 수 있는 데, 이러한 엣지케이스를 방지하기 위해
`while` 반복문에 `fruits` 리스트에 과일이 존재할 때에만 반복문을 계속하라 라는 조건을 추가한다.
```python
while K and fruits:
    ...
    if K >= price:
        total_cal += calories
        K -= price
    else:
        total_cal += (calories // price) * K
        k = 0
```



# 📌 느낀점
PseudoCode를 짜고 문제를 이해하는 데 시간이 걸렸다. 막상 어떻게 푸는지 알고 난 뒤에는 그렇게 어렵진 않았다.
다만 주어진 풀이를 보니까 더 줄일 수 있었는데 하는 아쉬움도 있고, 아직 코드를 클린하게 짜는 법은 부족한거 같다.

# 💻 풀이

```python
N, K = map(int, input().split())
fruits = [list(map(int, input().split())) for _ in range(N)]
# sort by p//c, sorted ==> (price, calories)
fruits.sort(key = lambda x : x[1] // x[0])

total_cal = 0

while K and fruits:
    price, calories = fruits.pop()
    
    if K >= price:
        total_cal += calories
        K -= price
    else:
        # if K < price, get calories per price and purchase fruit with the remaining money from the above
        total_cal += (calories // price) * K
        # purchased every fruit, change K = 0 to break the while loop
        K = 0

print(total_cal)
```

내가 풀은 방식
```python
N, K = map(int, input().split())
matrix = []

for _ in range(N):
	price, calories = map(int, input().split())
	matrix.append((price, calories))


cpp_values = []
total_cal = 0
	
for price, calories in matrix:
	# calories per piece (calories/price)
	cpp = calories // price
	cpp_values.append((cpp, calories, price))
	
cpp_values.sort(reverse=True)
budget = K
	
for cpp, calories, price in cpp_values:
	if budget >= price:
		budget -= price
		total_cal += calories
	else:
		total_cal += cpp * budget
		break

print(total_cal)
```


# 🔖 복습
```python
이상하게 행렬을 입력 받을 때 한 줄로 줄인 코드가 에러가 났다. 또 lambda를 이용하면 여러줄의 코드를 한 줄로 줄일 수 있다.
fruits = [list(map(int, input().split())) for _ in range(N)]

fruits.sort(key = lambda x : x[1] // x[0])

반복문 while을 활용할 때 조건을 제대로 설정해주고, 반복문 종료 조건(k=0)을 잊지말고 설정하기
리스트에서 데이터를 꺼낼 때는 destructuring을 활용해주기
while K and fruits:
    price, calories = fruits.pop()
    
    ...
    else :
        total_cal += (calories // price) * K
        K = 0
```