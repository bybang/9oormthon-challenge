# Goormthon Challenge Day 4

### 구름톤 코딩테스트 챌린지 네 번째 날,

이번 문제는 처음엔 반복문을 통해 푸는 문제라고 생각했지만 그렇게 할 경우 시간복잡도 측면에서
너무 복잡해진다고 봤기에 다른 방법을 궁리해야 했다.


```python
check if the given k's length is not over/under N
if len(k) == N:

    max_index = k.index(max(k))

    ascending = k[:max_index]
    descending = k[max_index:]
```

처음부터 난관에 봉착했다. `max()`와 `index()`를 통해 `max`의 `index`를 찾아 슬라이싱하는 것을 물어보는 문제였는데, 정렬만
생각하다 보니까 슬라이싱은 까맣게 잊어버리고 있었다. 공부를 다시하고 와서 또 도전해서 이쪽 과제는 풀어냈지만 문제가 하나 더 기다리고 있었다.

정렬은 `sort()`나 `sorted()`로 하면 되지만 너무 복잡하게 생각해서 아래와 같은 복잡한 코드가 나오고 말았다.
`all()` 을 통해 ascending, descending 리스트의 [i]값과 그 다음 [i+1] 값을 비교한것인데,
그냥 `sorted()`를 쓰고 리스트를 합쳐서 원본 리스트와 비교하면 간단히 해결되는 문제였다.

```python
check if the ascending is sorted in increasing order
ascending_sort = all(ascending[i] <= ascending[i+1] for i in range(len(ascending) - 1))

check if the ascending is sorted in decreasing order
descending_sort = all(descending[i] >= descending[i+1] for i in range(len(descending) - 1))


==================>> fix
sortedLeft = sorted(left)
sortedRight = sorted(right, reverse=True) # sort in descending order

sortedArr = sortedLeft + sortedRight # combine two lists again to check sortedArr and the list k
```

확실히 알고리즘에 대해서 응용력과 이해도가 떨어지는게 느껴져서, LeetCode 와 유튜브 자료등을 통해서
따로 공부를 병행해 나가며 구름톤 코딩테스트 챌린지를 진행해 나가는 중이다.
설령 지금은 부족해도 매일 도전하고 공부해나가며 챌린지를 끝낼 무렵에는 이정도 문제는 간단하게 풀 수 있는 레벨에 오르고 싶다.