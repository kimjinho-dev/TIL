# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_final_position(N, mat, moves):
    pass
    move_val = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 0,1,2,3 값에 따른 xy축 변동값
    for i, row_mat in enumerate(mat):  # 1의 위치를 찾기위한 인덱스값과 값을 받는 enumerate
        for j, val in enumerate(row_mat):
            if val == 1:
                xy_val = [i, j]  # 1의 위치 xy_val에 저장

    for move in moves:  # xy_val에서 키입력에 따른 위치 계산
        xy_val[0] += move_val[move][0]
        xy_val[1] += move_val[move][1]
        if xy_val[0] > N - 1 or xy_val[0] < 0:  # 범위밖 벗어날시 즉시 none 반환
            return None
        elif xy_val[1] > N - 1 or xy_val[1] < 0:
            return None

    return xy_val


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    moves1 = [3, 3, 0]
    print(get_final_position(N, mat, moves1))  # [2, 1]

    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2))  # [1, 2]
