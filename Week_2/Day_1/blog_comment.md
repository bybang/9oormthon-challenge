# Goormthon Challenge Day 6

### 구름톤 코딩테스트 챌린지 2주차 첫 번째 날,

> 구름톤 2주차가 시작됐다. 이번주차는 완전탐색 중심의 문제가 나오는 주라고 한다.

# 🧩 문제

# 🎯 전략
### 조합을 짜는 법
`abcde`가 있다고 가정할때, 이것을 하나하나 나누면 `a b c d e`가 되고,
각 문자 사이에 공백이 들어가게 되는데, 바로 이 공백으로 조합을 짜면 된다. `a (1) b (2) c (3) d (4) e`
이런식으로 이루어진 공백이 있다고 가정하자. 이때 문자열을 둘로 나누는 방법은 공백을 하나만 선택하는 것이고,
문자열을 셋으로 나누고 싶다면 공백을 두개를 선택하면 `a b cde` 등으로 나눌 수 있다.

### 인덱스 슬라이싱 활용
앞선 공백들을 통해 공백의 조합들을 ((1,2) == 1번 2번 자리의 공백과 함께 `abcde` 나누기를) 찾았다면,
이제 공백들을 직접 문자에 넣고 슬라이싱(`.slice() or [:]`)을 통해 문자배열을 받아야한다.


### 조합을 활용해 점수 계산하기
조합을 활용하면 점수까지도 계산할 수 있다. (1,2)의 조합의 점수, (1,3), (2,3)의 조합의 점수들이 각각 존재한다.
이 점수들을 합치고, `max()`를 활용해 조합의 점수를 비교해가며 최댓값을 도출할 수 있다.

# 📌 느낀점
이번에는 조합을 짜는 법을 몰랐다 더 많은 문제 유형들을 접해서 문제에 익숙해져야 할 필요성을 느꼈다.

# 💻 풀이

```python
from itertools import combinations

N = int(input())
S = input()


P = set()

blank = [i for i in range(1, N)]

comb = list(combinations(blank, 2))

for first, second in comb:
    P.add(S[:first])
    P.add(S[first:second])
    P.add(S[second:])

P = list(P)
P.sort()

result = 0

for first, second in comb:
    score = 0
    
    score += P.index(S[:first]) + 1
    score += P.index(S[first:second]) + 1
    score += P.index(S[second:]) + 1
    
    result = max(result, score)

print(result)
```


# 🔖 복습
```python
조합을 만들기 위해 공백 갯수를 N-1개 만큼 받기 (문자열이 N개라면 공백은 N-1개만큼 발생)
blank = [i for i in range(1, N)]

2개의 공백 갯수를 가지고 문자열 조합만들기
comb = list(combinations(blank, 2))

만들어진 조합을 루프하면서 `set()`에 슬라이싱해서 문자 각각 저장하기
for f, s in comb:
    P.add(S[:first])
    P.add(S[first:second])
    P.add(S[second:])
```