# 20220720 Homework

## 1. Built-in 함수

```python
len()
print()
input()
sum()
sorted()
```

## 2. 홀수만 담기

```python
num = list(range(1,51,2))        # range내 슬라이싱
# num = list(range(1,51)[0::2])  # 슬라이싱
```

## 3. 반복문으로 네모 출력

```python
n = 5
m = 9
for x in range(0,m):
    for y in range(0,n):
        print('*',end='')
    print('\n')
```

## 4. 조건 표현식

```python
temp = 36.5
print('입실 물가' if temp >= 37.5 else '입실 가능')
```

## 5. 정중앙 문자

```python
def get_middle_char(char):
    if len(char) % 2 == 1:
        print(char[ len(char) // 2 ])
    else:
        print(char[ len(char) // 2 - 1 ] , char[ len(char) // 2] , sep='')

```