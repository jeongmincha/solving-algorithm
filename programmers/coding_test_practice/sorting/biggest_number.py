# Problem: https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    from functools import cmp_to_key
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(lambda x,y: int(y+x)-int(x+y)))
    return str(int(''.join(numbers)))


if __name__ == '__main__':
    test_cases = [
        ([6,10,2], "6210"),
        ([3,30,34,5,9], "9534330")
    ]
    for test_case in test_cases:
        numbers, expected = test_case
        answer = solution(numbers)
        print('My answer: ', answer)
        print('Expected:  ', expected)
        assert answer == expected
