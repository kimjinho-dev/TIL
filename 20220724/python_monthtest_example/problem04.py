def turn(temperatures):
    pass
    # 여기에 코드를 작성합니다.
    max_min_dict = {'maximum': [], 'minimum': []}
    for t in temperatures:
        if t[0] > t[1]:
            max_min_dict['maximum'].append(t[0])
            max_min_dict['minimum'].append(t[1])
        else:
            max_min_dict['maximum'].append(t[1])
            max_min_dict['minimum'].append(t[0])
    return max_min_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [[9, 3], [9, 0], [11, -3], [11, 1], [8, -3], [7, -3], [-4, -12]]
    print(turn(temperatures))
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4],
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }
