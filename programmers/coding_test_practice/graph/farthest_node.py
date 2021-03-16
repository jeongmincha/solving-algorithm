# Problem: https://programmers.co.kr/learn/courses/30/lessons/49189

def solution(n, edge):
    answer = 0
    neighbors = {k: [] for k in range(1, n+1)}
    
    for e in edge:
        neighbors[e[0]].append(e[1])
        neighbors[e[1]].append(e[0])

    q = [(1,0)]
    distances = [0] * (n+1)
    visited = [False] * (n+1)
    visited[1] = True

    while q:
        current_node, distance = q.pop(0)
        distances[current_node] = distance

        for neighbor in neighbors[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, distance+1))
        
        distance += 1

    return distances.count(max(distances))


if __name__ == '__main__':
    test_cases = [
        ((6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
    ]
    for test_case in test_cases:
        n, vertex = test_case[0]
        expected = test_case[1]
        answer = solution(n, vertex)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
