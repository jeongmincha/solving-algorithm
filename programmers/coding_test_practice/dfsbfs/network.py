# Problem: https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    bfs = []
    visited = [False] * n

    while sum(visited) < n:
        unvisited_index = 0
        for idx, elem in enumerate(visited):
            if elem == False:
                unvisited_index = idx
                break
        bfs.append(unvisited_index)

        while len(bfs) > 0:
            curr = bfs.pop(0)
            visited[curr] = True
            for idx in range(n):
                if visited[idx] is False and computers[curr][idx] == 1:
                    bfs.append(idx)
        answer += 1

    return answer


if __name__ == '__main__':
    test_cases = [
        ((3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2),
        ((3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
    ]
    for test_case in test_cases:
        n, computers = test_case[0]
        expected = test_case[1]
        answer = solution(n, computers)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
