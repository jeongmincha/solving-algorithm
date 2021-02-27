# Problem: https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    idx = 0
    
    moves = [min(ord(_) - ord('A'), ord('Z') - ord(_) + 1) for _ in name]
    while True:
        answer += moves[idx]
        moves[idx] = 0
        if sum(moves) == 0:
            break
    
        left, right = 1, 1
        while moves[idx - left] == 0:
            left += 1
        while moves[idx + right] == 0:
            right += 1

        if left < right:
            idx -= left
            answer += left
        else:
            idx += right
            answer += right

    return answer


if __name__ == '__main__':
    test_cases = [
        ("JAZ", 11),
        ("JEROEN", 56),
        ("JAN", 23)
    ]
    for test_case in test_cases:
        name = test_case[0]
        expected = test_case[1]
        answer = solution(name)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected