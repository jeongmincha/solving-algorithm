# Problem: https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    import math
    answer = []
    remaining = []

    for idx, progress in enumerate(progresses):
        remaining.append(math.ceil((100 - progress) / speeds[idx]))

    print(remaining)
    current_num = 1
    current_boss = remaining[0]
    for elem in remaining[1:]:
        if elem <= current_boss:
            current_num += 1
        else:
            answer.append(current_num)
            current_num = 1
            current_boss = elem
    answer.append(current_num)

    return answer


if __name__ == '__main__':
    test_cases = [
        (([93, 30, 55], [1,30, 5]), [2,1]),
        (([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]), [1, 3, 2]),
        (([95, 96, 97, 98], [1,1,1,1]), [4])
    ]
    for test_case in test_cases:
        progresses, speeds = test_case[0]
        expected = test_case[1]
        answer = solution(progresses, speeds)
        print('My answer: ', answer)
        print('Expected: ', expected)
        assert answer == expected