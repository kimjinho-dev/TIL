# 20220719 homework_기초문법과 데이터 타입

## 1. Mutable & Immutable

```
mutable은 리스트, 세트, 딕셔너리 형식이 있고
immutable은 레인지, 듀플 형식이 있다.
따라서 
Mutable = string , list , set , dictinary
immutable = Tuple , range
```     

## 2. Dictionary 만들기

```python
dict_class = {'kim' : 23 , 'min' : 25 , 'song' : 26}
```


`디렉셔리는 {키이름 : 값} 형식이다. 키이름은 '' 을 넣지않을거면 변수이름또한 지정해야한다. 값이야 뭐 아무렇게나`

## 3. 평균 구하기

```python
scores = [80,89,99,83]
sum = 0
for x in range(0,len(scores)):
  sum += scores[x]

print(sum/len(scores))
```

`이런것도 필요없이 그냥 sum(list)를 해도 된다.`