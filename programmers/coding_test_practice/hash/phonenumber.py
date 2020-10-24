# Problem: https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    def is_same_prefix(a, b):
        length = min(len(a), len(b))
        return a[:length] == b[:length]

    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i == j:
                continue
            if is_same_prefix(phone_book[i], phone_book[j]):
                return False

    return True


if __name__ == '__main__':
    test_cases = [
        (['119', '97674223', '1195524421'], False),
        (['123', '456', '789'], True),
        (['12', '123', '1235', '567', '88'], False)
    ]

    for test_case in test_cases:
        phone_book, expected = test_case
        answer = solution(phone_book)
        print('My answer: ', answer)
        print('Expected: ', expected)
        assert answer == expected