# Problem: https://programmers.co.kr/learn/courses/30/lessons/42898


def solution(m, n, puddles):
    memo = [[0 for _ in range(m+1)] for _ in range(n+1)]
    memo[1][1] = 1

    for puddle in puddles:
        memo[puddle[1]][puddle[0]] = -1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            
            if memo[i][j] == -1:
                memo[i][j] = 0
            else:
                memo[i][j] = memo[i-1][j] + memo[i][j-1]

    return memo[n][m] % 1000000007


if __name__ == '__main__':
    test_cases = [
        ((4, 3, [[2, 2]]), 4)
    ]
    for test_case in test_cases:
        m, n, puddles = test_case[0]
        expected = test_case[1]
        answer = solution(m, n, puddles)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected