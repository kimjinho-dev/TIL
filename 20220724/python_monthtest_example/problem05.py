def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    if len(user_data['id']) == 0 or len(user_data['password']) == 0:
        return False
    else:
        return True

    # for a in user_data:
    #     if user_data[a] == '':
    #         return False
    # return True


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1))
    # False

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2))
    # True
