# Problem: https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    if N == number:
        return 1
    
    MEMO_SIZE = 8
    answer = -1
    memo = [set() for _ in range(MEMO_SIZE+1)]
    for idx in range(1, MEMO_SIZE+1):
        memo[idx].add(int(str(N) * idx))
    
    for idx in range(1, MEMO_SIZE+1):
        for k in range(1, idx):
            for left in memo[k]:
                for right in memo[idx-k]:
                    memo[idx].add(left + right)
                    memo[idx].add(left - right)
                    memo[idx].add(left * right)
                    if right != 0:
                        memo[idx].add(left // right)
        if number in memo[idx]:
            answer = idx
            break

    return answer


if __name__ == '__main__':
    test_cases = [
        ((5, 12), 4),
        ((2, 11), 3)
    ]
    for test_case in test_cases:
        N, number = test_case[0]
        expected = test_case[1]
        answer = solution(N, number)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected