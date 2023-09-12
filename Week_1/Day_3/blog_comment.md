# Goormthon Challenge Day 3

### 구름톤 코딩테스트 챌린지 세번째날,

이번 문제는 계산식이 input으로 들어가고, 각 계산식들의 합을 구하는 문제였다.

문제 자체는 전에 접해본적이 있어서 어렵지 않았지만, 일단 생각나는대로 하다보니
아래에 보이는 것 같이 nested loop이 나와버렸다.
시간복잡도적인 측면에서 O(n^2)이 나오면 안될 문제는 아닌거 같았지만,
조건: `(1 <= T <= 100)`, `(1 <= num1, num2 <= 1000)`

```python
import math

T = int(input())

N = [input().split() for _ in range(T)]

addAll = []
result = 0

for calculations in N:
	for cal in calculations:
		if "+" in cal:
			x = int(calculations[0]) + int(calculations[-1])
			addAll.append(x)
		elif "-" in cal:
			x = int(calculations[0]) - int(calculations[-1])
			addAll.append(x)
		elif "*" in cal:
			x = int(calculations[0]) * int(calculations[-1])
			addAll.append(x)
		elif "/" in cal:
			x = int(calculations[0]) / int(calculations[-1])
			addAll.append(math.trunc(x))

for i in addAll:
	result += i

print(result)
```

조금 더 줄여보고자 노력했고, 결과적으로 O(n)의 시간복잡도를 가지는 코드를 작성할 수 있었다.
일단은 통과했고, 해설이 나오면 다시 복습해볼 예정이다. 첫째날에 `math.trunc()`를 쓰는 문제에서
`int()`를 써서 넘어갔기 때문에 한 번 더 써보고 싶었는데 마침 활용할 수 있는 문제가 나왔다!
우연히 들어간 부분이든 의도한 복습이든 좋은 기회로 삼으면 그만이기에 기분좋게 풀 수 있었다.