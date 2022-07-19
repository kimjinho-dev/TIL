# 20220719 workshop_기초문법과 데이터 타입


## 1. 숫자의 입력과 출력

```python
first = int(input())
second = int(input())
print(first+second)
```


## 2. Dictionary를 활용하여 평균 구하기

```python
dict_lunch = {'ramen' : '5000' , 'row fish' : '10000'}
total = 0
list_of_key = list(dict_lunch.keys())

for menu in list_of_key:
    total += int(dict_lunch[menu])

print(total)
```

`파이썬 딕셔너리는 키와 값을 받을수 있는 방법이 있다. 딕셔너리.keys() 와 딕셔너리.value() 인데 이를 활용하여 일일히 입력하지않고 딕셔너리 값을 사용할 수 있다.`