sdorq = []
T=int(input())
for _ in range(0,T):     
# _ 는 여러가지 용도로 사용된다는데, 여기선 빈칸으로 둘수없는곳에 강제로 채우는 용도로 사용된다.    
# 다른 용법은 좀 찾아보자. 즉 이문법은 T번 반복(0~T-1이기때문에)을 실행시키는 방법인셈                           
    for _ in range(9):
    # 굳이 range(0,T)같이 범위를 정하지않아도 횟수제한이면 range(9)같이 사용해도 된다.
        sdorq.append(list(map(int, input().split())))
        # 이 코드를 짜게된 핵심. 파이썬은 여러 입력을 한번에 받는데에 아주 좋은 수단이 있다.
        # 그중 하나는 list(map(int,input().split())) 식으로 하거나 
        # 여러행을 받고자하면 list(map(int,input().split()) for _ in range(n)) 이런식으로 n*x 행렬을 받을수도 있다.
        # 이와중에 있는 for문은 한줄로 for문쓰는 용법때 사용되는것인데, 기존 :를 써서 여러줄을 사용하는것대신 깔끔하게 사용 가능하다.
        # 다만 이방식으로하면 한줄을 받고 다시 초기화가 되기때문에 어딘가에 다시 넣어줘야 유효한 입력을 할 수 있다(계속 첫번째행에만 넣는다)
        # 그래서 사용하는 방식이 [list].append 형식인셈. append 특성상 계속 밀어넣기만 해서 입력을받을때는 오히려 좋다.


error_t =["1"]*T
# 에러값을 담을 리스트

for test_case in range(0,T) : 
# 가로검증
    for x in range(test_case*9,(test_case+1)*9-1):                                         
        for y in range(0,8):        
            for y_check_range in range(y+1,9):                                   
                if sdorq[x][y] == sdorq[x][y_check_range]:     
                    error_t[test_case]="0"

# 세로검증
    for y in range(0,9):        
        for x in range(test_case*9,(test_case+1)*9-1):		                        
            for x_check_range in range(x+1,(test_case+1)*9):
                if sdorq[x][y] == sdorq[x_check_range][y]:
                    error_t[test_case]="0"

"""
# 3*3 검증 작성중
    y , y_check = 0
    x = test_case*9
    x_check = test_case*9+1
    count = 0
        while(x==(test_case+1)*9-1 and y==8):
            while(count!=36):
                if sdorq[x][y] == sdorq[x_check][y_check]:
                    error_t[test_case]="0"
                x_check =+ 1
                if x_check % 3 == 0:
                    x_check = test_case*9
                    y_check += 1
                x += 1
                if x % 3 == 0:
                    x =- 3
                    y += 1
                    if y % 3 == 0:
                        y =- 3
            count +=1
        
"""
# 결과값 출력
for test_case in range(1,T+1):
    print("#" , test_case , error_t[test_case-1])


