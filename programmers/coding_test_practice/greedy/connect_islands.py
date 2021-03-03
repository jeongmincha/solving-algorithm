# Problem: https://programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = 0
    _costs = sorted(costs, key=lambda x: x[2], reverse=False)
    connected = set([_costs[0][0]])

    while len(connected) < n:
        for idx, cost in enumerate(_costs):
            a, b = cost[:2]
            # If only one node is included in 'connected', update
            if (a not in connected and b in connected) or \
                (b not in connected and a in connected):
                connected.update(cost[:2])
                answer += cost[2]
                _costs[idx] = [-1, -1, -1]
                break
    return answer


if __name__ == '__main__':
    test_cases = [
        ((4, [[0,1,1], [0,2,2], [1,2,5], [1,3,1], [2,3,8]]), 4)
    ]
    for test_case in test_cases:
        n, costs = test_case[0]
        expected = test_case[1]
        answer = solution(n, costs)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected