# Problem: https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = n - len(lost)
    reserved_index = [False] * (n+1)
    for idx in reserve:
        if idx in lost:
            answer += 1
            continue
        reserved_index[idx] = True

    for idx in lost:
        if idx in reserve:
            continue
        if idx > 1 and reserved_index[idx-1] == True:
            answer += 1
            reserved_index[idx-1] = False
        elif idx < n and reserved_index[idx+1] == True:
            answer += 1
            reserved_index[idx+1] = False

    return answer


if __name__ == '__main__':
    test_cases = [
        ((5, [2,4], [1,3,5]), 5),
        ((5, [2,4], [3]), 4),
        ((3, [3], [1]), 2)
    ]
    for test_case in test_cases:
        n, lost, reserve = test_case[0]
        expected = test_case[1]
        answer = solution(n, lost, reserve)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
