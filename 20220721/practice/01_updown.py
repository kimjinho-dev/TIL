import random

# is_playing : True인 경우 게임을 계속 반복합니다. False인 경우 게임을 종료합니다.
# answer : 플레이어가 맞혀야 하는 정답 숫자입니다. 1 이상 10000 이하의 난수입니다.
# random은 난수 생성 기능을 제공하는 Python 모듈입니다.
# random.randint(a, b) 라고 작성하면 a <= N <= b 를 만족하는 임의의 정수 N을 반환합니다.
# counts : 몇 번 만에 정답을 맞혔는지 담는 변수입니다. 정답을 맞혔을 때 함께 출력합니다.

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    user_num = None
    # print(answer)
    while answer != user_num:
        user_num = int(input('1이상 10000이하의 숫자를 입력하세요. :'))
        if user_num <= 0 or user_num > 10000:  ## 예외처리 중요! 0빼먹음
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.')
            continue
        print('Up!!!' if user_num < answer else 'Down!!!')
        counts += 1
    print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.')
    replay = input('게임을 재시작하시려면 y, 종료를하시려면 n을 입력하세요 :')
    if replay == 'y':
        is_playing = True
    elif replay == 'n':
        is_playing = False
        print('이용해주셔서 감사합니다. 게임을 종료합니다')
    else:
        is_playing = False
        print('잘못된 값을 입력하셨습니다. 게임을 종료합니다')
