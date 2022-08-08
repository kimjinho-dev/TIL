N = 7
num_list = [8, 1, 2, 7, 0, 8, 9]
cnt = [0] * 10
new = [0] * N
for i in range(N):  # 실행하는 횟수, 검색해야하는 마지막위치
    cnt[num_list[i]] += 1

for j in range(1, 10):
    cnt[j] = cnt[j] + cnt[j - 1]

for l in range(N - 1, -1, -1):
    cnt[num_list[l]] -= 1
    new[cnt[num_list[l]]] = num_list[l]
print(new)
