# 20220721 workshop

## 1. 간단한 N의 약수

```python
for i in range(1,N+1):
  if N % i == 0:
    print(i)
```

## 2. List의 합 구하기

```python
def list_sum(num):
    total = 0
    for i in num:
        total += i
    return total
```

## 3. Dictionary로 이루어진 List의 합 구하기

```python
def dict_list_sum(num):
    total = 0
    for i in num:
        total += i['age']
    return total
```

## 4. 2차원 List의 전체 합 구하기

```python
def all_list_sum(num):
    total = 0
    for n in num:
        for m in n:
            total += m
    return total
```

## 5. 숫자의 의미

```python
def get_secret_word(num):
    str_total = ''
    for n in num:
        str_total += chr(n)
    return str_total
```


## 6. 내 이름은 몇일까?

```python
def get_secret_number(x):
    str_total = 0
    for n in x:
        str_total += ord(n)
    return str_total
```

## 7. 강한이름

```python
def get_strong_word(x, y):
    str_total_x = 0
    str_total_y = 0
    for n in x:
        str_total_x += ord(n)
    for n in y:
        str_total_y += ord(n)
    if str_total_x == str_total_y:
        return x + y
    elif str_total_x > str_total_y:
        return x
    elif str_total_x < str_total_y:
        return y
```