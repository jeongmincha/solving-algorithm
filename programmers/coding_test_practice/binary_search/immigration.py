# Problem: https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0

    num_gates = len(times)
    left = 1
    right = num_gates * max(times)

    while left <= right:
        mid = (left + right) // 2

        num_pass = 0
        for time in times:
            num_pass += mid // time
            if num_pass >= n:
                break
        
        if num_pass >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1

    return answer


if __name__ == '__main__':
    test_cases = [
        ((6, [7, 10]), 28)
    ]
    for test_case in test_cases:
        n, times = test_case[0]
        expected = test_case[1]
        answer = solution(n, times)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
