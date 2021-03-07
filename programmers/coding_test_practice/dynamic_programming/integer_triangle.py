# Problem: https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = 0

    N = len(triangle)
    memo = []
    for h in range(N):
        memo.append([])
        for i in range(h+1):
            memo[h].append(0)
    memo[0][0] = triangle[0][0]

    for h in range(1, N):
        for i in range(h+1):
            curr = triangle[h][i]
            if i == 0:
                memo[h][i] = memo[h-1][i] + curr
            elif i == h:
                memo[h][i] = memo[h-1][i-1] + curr
            else:
                memo[h][i] = max(memo[h-1][i-1] + curr, memo[h-1][i] + curr)

    return max(memo[N-1])


if __name__ == '__main__':
    test_cases = [
        ([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], 30)
    ]
    for test_case in test_cases:
        triangle = test_case[0]
        expected = test_case[1]
        answer = solution(triangle)
        print('Solution: ', answer)
        print('Expected; ', expected)
        assert expected == answer
