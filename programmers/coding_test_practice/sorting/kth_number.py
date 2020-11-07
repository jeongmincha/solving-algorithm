# Problem: https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer


if __name__ == '__main__':
    test_cases = [
        (([1,5,2,6,3,7], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]), [5,6,3])
    ]
    for test_case in test_cases:
        array, commands = test_case[0]
        expected = test_case[1]
        answer = solution(array, commands)
        print('My answer: ', answer)
        print('Expected: ', expected)
        assert answer == expected
