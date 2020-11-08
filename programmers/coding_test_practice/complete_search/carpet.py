# Problem: https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    import math

    answer = []
    area = brown + yellow
    cases = []
    for height in range(3, int(math.sqrt(area)) + 1):
        if area % height == 0:
            cases.append((int(area/height), height))
    
    for case in cases:
        width, height = case
        if (width-2) * (height-2) == yellow:
            answer = [width, height]

    return answer


if __name__ == '__main__':
    test_cases = [
        ((10, 2), [4,3]),
        ((8, 1), [3,3]),
        ((24, 24), [8,6])
    ]
    for test_case in test_cases:
        brown, yellow = test_case[0]
        expected = test_case[1]
        answer = solution(brown, yellow)
        print('My answer: ', answer)
        print('Expected:  ', expected)
        assert answer == expected
