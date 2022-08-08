N = 8
num_list = [1, 5, 4, 2, 2, 3, 4, 5]
for i in range(N - 1, 0, -1):  # 실행하는 횟수, 검색해야하는 마지막위치
    for j in range(0, i):  # 첫칸부터 마지막위치까지 움직여야하는 idx
        if num_list[j] < num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
print(num_list)
