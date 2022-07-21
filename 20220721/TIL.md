# 20220721 TIL

## 복습간 헷깔린것

### map

```python
A = map(int, "123")
print(A)
# 123이 아니라 "1" "2" "3"이다. 스트링도 리스트형이기때문에 하나씩

a,b,c = map(int , "123")
print(a+b+c)
# 출력은 6, 위처럼 abc에는 각각 1,2,3이 들어가고 이 합이 6이 나온다 
```

### lambda

```
lambda는 일일히 def로 함수를 만드는게 아닌
한줄로 함수를 만드는데에 용이하다.
`funtion = lambda x : x+1`
같이 변수에 함수를 넣을수도있다.
funtion(n)같이 사용도 가능한것이다.
```

## 온라인 실습문제


정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로
   나타나는 숫자는 하나만 남기고 제거한 list를 출력하라. 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다. 
   입력 예시	[1, 1, 3, 3, 0, 1, 1] 
   츨력 예시	[1, 3, 0, 1]


```python
a = list(map(int, input().split()))

for idx, val in enumerate(a):
    if idx + 1 < len(a):
        while idx + 1 < len(a):
            if a[idx] == a[idx + 1]:
                del a[idx + 1]
            else:
                break
print(a)
```

조금 더럽게 작성된 코드..
for문 하나만 쓰면 del를 한번하고 계속 칸을 이동해버려서 중첩 for - while문 사용..
