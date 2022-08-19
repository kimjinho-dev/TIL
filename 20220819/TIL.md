# 20220819

## 이차원 격자 DFS

### 기본적인 생성구조

(1) 입력값 받을것 받기  

```python
w, h = map(int, input().split())
```

(2) 방문 리스트 크기에 맞게 생성  

```python
visit = [[False] * w for _ in range(h)]
```

(3) 문제에 맞게 델타값 선언  

```python
di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]  # 상하좌우,좌상,우상,좌하,우하
```

(4) 2중 for문 행열 순회 반복문 생성  

```python
for i in range(h):
    for j in range(w):
        if not visit[i][j] and land[i][j] == 1:
```

(5) dfs 함수 생성. 해당위치를 방문처리하고, 델타값을 활용해 이동처리  

```python
def dfs(x, y):
    visit[x][y] = True
    for n in range(8):
        vx = x + di[n]
        vy = y + dj[n]
```

(6) 이동후 조건식을 확인하여 재귀, 및 탈출을 확인  

```python
if 0 <= vx < h and 0 <= vy < w and land[vx][vy] == 1 and not visit[vx][vy]:
```

(7) 필요한 값에 따라서 이중for문에 += 혹은 dfs 내부에서 += 넣기. 문제마다 다르다  

```python
dfs(i, j)
cnt += 1
```

### dfs 흐름

(1) 내부에서 아직 방문하지않고 해당값이 옳바르다면 dfs 실행  

```python
if not visit[i][j] and land[i][j] == 1:
```

(2) dfs 실행시, 해당 위치 방문으로 기록  

```python
visit[x][y] = True
```

(3) 지정된 델타값을 활용하여 하나씩 이동시켜보기  

```python
for n in range(8):
        vx = x + di[n]
        vy = y + dj[n]
```

(4) 조건문을 통해서 맵의 범위를 벗어나는지, 방문을 했는지, 값은 옳바른지 확인  

```python
if 0 <= vx < h and 0 <= vy < w and land[vx][vy] == 1 and not visit[vx][vy]:
```

(5) 조건을 통과하면 해당 좌표값으로 재귀  

```python
dfs(vx, vy)
```

(6) 2번에서 반복  
(7) 만약 모든 델타값 이동이 불가능하다면, 해당 함수는 종료하고 이전 함수로 돌아감. 즉 한단계 이전으로 돌아가는것.  
(8) 해당 함수에서도 나머지 델타값 이동을 확인, 만약 불가능하다면 마찬가지로 이전 단계로 이동  
(9) 이를 반복하다가 처음 호출된 dfs로 돌아오고 모든 이동이 불가능하다면 dfs 종료  
(10) 다음 [i][j] 확인  
(11) 이미 dfs에서 방문처리를 했기때문에 확인한 위치는 재확인하지않음.  
