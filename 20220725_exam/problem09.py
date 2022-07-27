# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    x, y = position
    if x == 0 and M == 0:
        return False
    elif y == 0 and M == 2:
        return False
    elif x == N - 1 and M == 1:
        return False
    elif y == N - 1 and M == 3:
        return False
    else:
        return True


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
