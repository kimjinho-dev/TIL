# 20220723 TIL

## 2차원 배열 값 추출하기

```python
A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

for a,b,c,d,e in A:           # 1행씩 2중 for문 안쓰고 한번에 뽑기
    print(a,b,c,d,e)

for a in A:                   # 1행씩 출력하는데 언패킹하여 깔끔하게
    print(*a)

for a in A:                   # 1행씩 출력하는데 리스트형태로
    print(a)

A = zip(*A)                    
for row in A:                
    print(row)               # zip 함수를 통해 리스트 열 뽑기로 재배열됨

```


## 배열 초기화

```python
B = [[0] * 5] * 5                   # 1. 얕은 복사로 인해 배열간의 참조가 발생
B = [([0] * 5) for _ in range(5)]     # 2. 일일히 생성하여 얕은 복사 X
B = []
for i in range(5):
    for j in range(5):
        B.append(0)
for i in range(5):
    for j in range(5):
        B[j][i] = A[i][j]           # 1.의 방식으로 초기화시 정상작동하지않는다. 2.방식을 해야 정상작동.

print([0 for x in range(5)])                                            # 1차원 배열 초기화
print([[0 for _ in range(5)] for _ in range(5)])                        # 2차원 배열 초기화
print([[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)])    # 3차원 배열 초기화
```

여기서 사용되는것은 지능형 리스트라고하여 generator object이다.
다른 형식의 오브젝트로 그냥 출력시에는 type에 대한것만 출력된다. 따라서  `print([[0 for _ in range(5)] for _ in range(5)])` 형태로 사용해야한다.
이를 풀면 `print(list(list(0 for _ in range(5)) for _ in range(5)))` 형식이다.
zip 함수도 유사한점을 보이는데, `print(zip(*A))` 는 타입명만 출력해낸다. 정상적 출력을 위해선 `print(list(zip(*A)))` 형태로 사용해야한다.

얕은 복사에 대한 문제는 `A = [0]*5` 정도의 한 행까지는 괜찮다.
즉 열을 늘리는 열복사에 대한것은 괜찮지만
그 이후 행복사는 얕은복사로 인해 서로가 서로값을 참조하는 형태가 된다.
따라서 `[[0 for _ in range(5)] for _ in range(5)]` 까지 아니더라도 `[ ([0] * 5) for _ in range(5) ]` 정도로 사용해도 된다.
얕은 복사에 대한 참조 링크 https://yechoi.tistory.com/52

## 얕은 복사 관련 예시 하나 더

```python
A = [1, 2, 3, 4, 5]

B = A

A[0] = 5
print(A)
print(B)
```

위 코드는 B는 A의 [1,2,3,4,5] 를 가져오고 A는 첫번째가 5로 바뀌었기때문에
[5,2,3,4,5]
[1,2,3,4,5]
가 출력될것같다. 하지만 얕은 복사관련으로
[5,2,3,4,5]
[5,2,3,4,5]
B 또한 바뀐것을 볼 수 있다.

이를 해결하기위해 리스트 값 대입시 간단하게 넣는게 아니라, 
.append() 메서드 활용등을 해야한다.