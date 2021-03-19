import sys

# def dijkstra(cost, a, b):
#     dist = [sys.maxint for i in range()]

def solution(n, s, a, b, fares):
    answer = sys.maxsize
    cost = {k: {k2: sys.maxsize for k2 in range(1, n+1)} for k in range(1, n+1)}

    for i in range(1, n+1):
        cost[i][i] = 0

    for fare in fares:
        cost[fare[0]][fare[1]] = fare[2]
        cost[fare[1]][fare[0]] = fare[2]
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    
    for middle in range(1, n+1):
        answer = min(answer, cost[s][middle] + cost[middle][a] + cost[middle][b])

    return answer


if __name__ == '__main__':
    test_cases = [
        ((6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]), 82),
        ((7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]), 14),
        ((6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]), 18)
    ]
    for test_case in test_cases:
        n, s, a, b, fares = test_case[0]
        expected = test_case[1]
        answer = solution(n, s, a, b, fares)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected