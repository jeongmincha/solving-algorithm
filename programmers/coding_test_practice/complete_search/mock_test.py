# Problem: https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    from itertools import chain, repeat
    import math

    N = len(answers)
    result = {}
    result[0] = list(chain.from_iterable(repeat([1,2,3,4,5], math.ceil(N/5))))[:N]
    result[1] = list(chain.from_iterable(repeat([2,1,2,3,2,4,2,5], math.ceil(N/8))))[:N]
    result[2] = list(chain.from_iterable(repeat([3,3,1,1,2,2,4,4,5,5], math.ceil(N/10))))[:N]

    correct = [0] * 3
    for index, answer in enumerate(answers):
        for i in range(3):
            if result[i][index] == answer:
                correct[i] += 1

    ret = []
    for i in range(3):
        if correct[i] == max(correct):
            ret.append(i+1)

    return ret


if __name__ == '__main__':
    test_cases = [
        ([1,2,3,4,5], [1]),
        ([1,3,2,4,2], [1,2,3])
    ]
    for test_case in test_cases:
        answers, expected = test_case
        answer = solution(answers)
        print('My answer: ', answer)
        print('Expected:  ', expected)
        assert answer == expected