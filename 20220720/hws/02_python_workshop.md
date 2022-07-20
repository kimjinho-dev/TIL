# 20220720 Workshop

## 1. 세로로 출력하기

```python
number = int(input())

for num in range(1,number+1):
    print(num)
```

## 2. 가로로 출력하기

```python
number = int(input())

for num in range(1,number+1):
    print(num,end=' ')
```

## 3. 거꾸로 세로로 출력하기

```python
number = int(input())

for num in range(number,-1,-1):
    print(num)
```

## 4. 거꾸로 출력해 보아요

```python
number = int(input())

for num in range(number,-1,-1):
    print(num,end=' ')
```

## 5. N줄 덧셈

```python
num_sum = 0
for num in range(1,int(input())+1):
    num_sum += num 
print(num_sum)
```

## 6. 삼각형 출력하기

```python
num = int(input())
for star in range(1,num+1):
    triangle = [' '] * num
    for x in range(0,star):
        triangle[x] = '*'
    print(triangle[-1:-num-1:-1])
```

## 7. 중간값 찾기

```python
sort_number = sorted(numbers)
print(sort_number)
print(sort_number[len(sort_number) // 2])
```