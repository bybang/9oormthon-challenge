# Goormthon Challenge Day 11

### 구름톤 코딩테스트 챌린지 3주차 첫 번째 날,

> 구름톤 3주차가 시작됐다. 이번주차는 탐색과 동적 프로그래밍 중심의 문제가 나오는 주라고 한다.

# 🧩 문제

# 🎯 전략
### 다이내믹 프로그래밍 (동적 계획법)
저번 주에 나왔던 통증 문제와는 다르게 주어진 아이템들도 배수 관계가 아니고, 0보다 작은 아이템도 사용할 수 없다.
그렇다면 그리디 알고리즘을 사용할 수 없다는 의미이므로, 이 때 이용할 수 있는 것이 다이내믹 프로그래밍이다.

가장 유명한 다이내믹 프로그래밍 (이하 dp) 문제는 피보나치 수열인데 재귀를 활용해 답을 구하는 것이 가능하지만 그대로 계산한다면
시간복잡도가 감당할 수 없이 커지게 된다. 그래서 구한 값을 변수에 저장해두었다가 그 변수를 재활용 하는 것이 dp의 핵심이다.
(계산된 결과를 일시로 기록해 놓는 것을 메모이제이션 이라고도 한다)

### Dp를 활용해야 하는 문제 판별하기
그리디 알고리즘이나 수열 등을 통해서 문제를 풀 수 없거나, 풀어도 시간 복잡도가 너무 높게 나온다면 dp를 고려해보자.

아래의 조건들을 만족한다면, 처음부터 dp로 접근해서 풀면 된다.

1. 큰 문제를 작은 문제로 나눌 수 있어야 한다.
2. 이 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.(Optimal Substructure)
 - 피보나치 수열의 예
 - A(n) = A(n-1) + A(n-2), A1 = 1 A2 = 1
3. 동일한 작은 문제를 반복적으로 해결해야 한다(Overlapping Subproblem)
4. Top-Down 이나 Bottom-Up의 방식으로 해결할 수 있다.


### Dp 테이블 만들기
결과 저장용 리스트를 dp 테이블이라고 하는데, 먼저 사용할 리스트를 초기화 해주자.
이 때 고려해야 할 점은 아이템을 써서 통증을 0으로 만들 수 있는 경우의 수를 구하는 문제인만큼 0으로 만들 수 없는 경우의 수는 
N의 범위 이상의 큰 수를 지정해 주어야 혹시라도 겹치는 상황을 방지할 수 있다.
dp 테이블을 임의의 수(무한대)를 (N + 1) 만큼 - 0부터 시작하는 리스트를 고려해 N번까지 - 설정해 초기화한다.

`dp = [float('inf')] * (N + 1)`

그리고 통증이 0이면 사용할 수 있는 아이템의 갯수도 0이므로 `dp[0] = 0`으로 설정해준다.

### 주어진 조건 활용하기
통증을 `i`, 통증 수치를 0으로 만들 수 있는 아이템의 갯수를 `dp[i]`라고 할 때, 통증 - 아이템 A를 구해볼 수 있다.
이 때 통증 - 아이템이 마이너스인 상태는 고려하지 않고, 0 이상일 때 `min()` 함수를 활용해서 최소값을 구하자.

```python
현재값 dp[i] 와 아이템을 사용한 dp[i - A] + 1 값중 최소값을 리턴해주는 데, + 1은 아이템을 하나 사용했다는 의미이다.
if i - A >= 0:
    dp[i] = min(dp[i], dp[i - A] + 1)
```

아이템 B도 마찬가지로 구해주고, 바텀-업 방식으로 아래에서부터 N에 해당하는 숫자만큼 간다면 dp[N]을 구할 수 있다.

만약 dp[N]의 값을 구할 수 없다면, -1을 출력하면 된다.

# 📌 느낀점
다이내믹 프로그래밍을 처음 접해봐서 여러 매체를 통해 공부해야 했다. 공부하고 나서도 정확하게 구동법을 캐치하지 못했지만,
python tutor를 통해 어떻게 코드가 작동하는지 보고 나니까 생각보다 단순한 구조로 이루어져 있었다.

# 💻 풀이

```python
N = int(input())
A, B = map(int, input().split())

dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(N + 1):
    if i - A >= 0:
        dp[i] = min(dp[i], dp[i - A] + 1)
    if i - B >= 0:
        dp[i] = min(dp[i], dp[i - B] + 1)

print(dp[N] if dp[N] != float('inf') else -1)
```


# 🔖 복습
```python
다이내믹 프로그래밍을 활용하는 방법 이해하기

문제가 dp유형인지 파악이 먼저다. 그리디, 구현, 완전 탐색등의 아이디어로 풀이 방법이 떠오르지 않는다면 dp 고려하기
재귀함수로 비효율적인 완전 탐색을 작성한 뒤 작은 문제에서 구한 답이 큰 문제에 그대로 사용될 수 있다면 dp로 개선

dp 테이블 초기화 하기

주어진 조건을 고려해서 dp 값이 무언가의 조합(아이템 a+b)이면 dp = 큰 수(범위 이상) * (N + 1)
dp에 부분 문제의 값을 기록해야 한다면 dp = [0] * N 범위 이상 (N + 1)

dp = [float('inf')] * (N + 1)
or
dp = [0] * (N + 1)

처음 1~2번째의 값 설정하기

이 문제에서 d[0] = 0
피보나치 수열에서 d[1] = 1, d[2] = 2
```