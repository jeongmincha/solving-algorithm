# Problem: https://programmers.co.kr/learn/courses/30/lessons/42897


def solution(money):
    N = len(money)
    memo = [money[0], money[0]]
    memo2 = [0, money[1]]

    for i in range(2, N-1):
        memo.append(max(memo[i-2] + money[i], memo[i-1]))
    
    for i in range(2, N):
        memo2.append(max(memo2[i-2] + money[i], memo2[i-1]))

    return max(memo[-1], memo2[-1])


if __name__ == '__main__':
    test_cases = [
        ([1,2,3,1], 4)
    ]
    for test_case in test_cases:
        money, expected = test_case
        answer = solution(money)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected