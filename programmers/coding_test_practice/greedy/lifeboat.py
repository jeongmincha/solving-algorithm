# Problem: https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    N = len(people)
    people.sort(reverse=True)

    left_idx, right_idx = 0, N-1
    while left_idx <= right_idx:
        if people[left_idx] + people[right_idx] <= limit:
            right_idx -= 1
        answer += 1
        left_idx += 1

    return answer


if __name__ == '__main__':
    test_cases = [
        (([70, 50, 80, 50], 100), 3),
        (([70, 80, 50], 100), 3)
    ]
    for test_case in test_cases:
        people, limit = test_case[0]
        expected = test_case[1]
        answer = solution(people, limit)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected