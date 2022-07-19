# 2070 큰놈, 작은놈, 같은놈

T=int(input())
C= []
for _ in range(0,T):
    C.append(list(map(int , input().split())))           # intput().split() 으로해도 2개 값은 받지만, 정수형으로 받으려면 이렇게 해야함.
    
for test_case in range(0,T):
    if C[test_case][0]>C[test_case][1]:
        print(f'#{test_case+1} >')
    elif C[test_case][0]<C[test_case][1]:
        print(f'#{test_case+1} <')
    elif C[test_case][0]==C[test_case][1]:
        print(f'#{test_case+1} =')
