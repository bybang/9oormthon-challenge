# Goormthon Challenge Day 8

### 구름톤 코딩테스트 챌린지 2주차 세 번째 날,

> 이번 문제는 그리디 알고리즘의 기초 활용법을 물어보는 문제였다.

# 🧩 문제

# 🎯 전략
### 배수 관계 확인하기
동전 문제로도 유명한 이 문제는, 주어진 모든 수가 배수 관계에 있다.
`bandage`, `medicine`, `painkiller`를 보면 1, 7, 14로 배수 관계이다.

### 모듈로(%), 나누기(//) 연산 적극 활용하기
통증을 아이템 수치만큼 나눠주면 해당 아이템 몇 개를 썼는지가 나온다. 몫만큼 result 값에 더해주자.
그 뒤 통증은 아이템 수치만큼 나눈 나머지로 재설정 해준다.


# 📌 느낀점
그리디의 기초 활용법에 대해 공부했는데, 게임의 알고리즘을 짠다고 생각하고 풀었더니
로직도 쉽게 짜지고 즐겁게 풀 수 있었던 문제였다.
풀이에 나와있듯이 너무 복잡하게 코드를 많이 썼다. 더 클린하고 DRY한 코드를 쓸 수 있었는데, 하는 아쉬움이 있다.

# 💻 풀이

```python
N = int(input())

def calculate_items_needed(N):
	bandage, medicine, painkiller = 1, 7, 14 # 1, 7, 14 = 1, 7x1, 7x2
	pain = N
	count = 0
	
	count += pain // painkiller # divide pain with 14 first
	pain %= painkiller # for ex) 8 % 14 = 0, but 100 % 14 = 2
	
	count += pain // medicine
	pain %= medicine
	# if pain less than 7, add pain to current count
	count += pain # if pain cannot divided with 14, 7, pain = bandage_count
	
	return count

print(calculate_items_needed(N))
```


# 🔖 복습
```python
주어진 숫자들이 배수 관계에 있다면 그리디 계산법 떠올리기

N = int(input())

result = N // 14 # painkiller 사용
N %= 14 # painkiller 사용하고 남은 나머지 == N

result += N // 7 # 나머지에 medicine 사용
N %= 7 # medicine 사용 후 남은 나머지 == N

result += N # 마지막 남은 나머지를 결과값에 더해주기

print(result)
```