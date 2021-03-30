import sys
from heapq import heappop, heappush

def dijkstra(costs, src, dst):
    distances = [sys.maxsize for _ in range(len(costs))]
    distances[src] = 0
    priority_queue = [(0, src)]

    while priority_queue:
        distance, node = heappop(priority_queue)

        if distances[node] < distance:
            continue

        for item in costs[node]:
            new_node, new_cost = item
            new_cost += distance
            if new_cost < distances[new_node]:
                distances[new_node] = new_cost
                heappush(priority_queue, (new_cost, new_node))

    return distances[dst]


def solution(n, s, a, b, fares):
    answer = sys.maxsize
    costs = [[] for _ in range(n+1)]

    for fare in fares:
        src, dst, cost = fare
        costs[src].append([dst, cost])
        costs[dst].append([src, cost])

    answer = dijkstra(costs, s, a) + dijkstra(costs, s, b)
    print(answer)
    for middle in range(1, n+1):
        if middle != s:
            answer = min(answer, 
                dijkstra(costs, s, middle) + \
                dijkstra(costs, middle, a) + \
                dijkstra(costs, middle, b)
            )

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