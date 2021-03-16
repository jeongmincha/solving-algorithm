# Problem: https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0
    wins = {k: set() for k in range(1, n+1)}
    loses = {k: set() for k in range(1, n+1)}

    for a, b in results:
        wins[a].add(b)
        loses[b].add(a)
    
    for i in range(1, n+1):
        for loser in wins[i]:
            loses[loser].update(loses[i])
        for winner in loses[i]:
            wins[winner].update(wins[i])
    
    return sum([len(wins[i]) + len(loses[i]) == n-1 for i in range(1, n+1)])


if __name__ == '__main__':
    test_cases = [
        ((5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
    ]
    for test_case in test_cases:
        n, results = test_case[0]
        expected = test_case[1]
        answer = solution(n, results)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected