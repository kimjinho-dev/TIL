# 1859 백만장자 프로젝트

T = int(input())
margin = []

for test_case in range(0,T):
    N = int(input())
    C = list(map(int , input().split()))
    max = C
    margin.append('0')
    print(margin[test_case])
    for x in range(0,N-1):
        for y in range(1,N):            
            if max[x] < C[y]:
                print(max[x])
                max[x] = C[y]
                print("check")
                print(max[x])
        margin[test_case] = max[x]-C[x]
        print(margin[test_case])            ## 이 더하는값이 뭔가 문제가있음

for test_case in range(0,T):
    print(f'#{test_case+1} {margin[test_case]}')



    #print(C)


