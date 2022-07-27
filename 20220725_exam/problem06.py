# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    caesar_word = ''
    for c in word:
        if ord(c) <= 90 and ord(c) + n > 90:
            caesar_word += chr(ord(c) + n - 26)
        elif ord(c) <= 122 and ord(c) + n > 122:
            caesar_word += chr(ord(c) + n - 26)
        else:
            caesar_word += chr(ord(c) + n)
    return caesar_word


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx
