# Problem: https://programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    m = len(words[0])
    N = len(words)
    connected = {}
    for i in range(N):
        for j in range(N):
            if sum([words[i][idx] != words[j][idx] for idx in range(m)]) == 1:
                if i in connected:
                    connected[i].append(j)
                else:
                    connected[i] = [j]
    
    begin_index, end_index = 0, 0
    for i in range(N):
        if sum([words[i][idx] != begin[idx] for idx in range(m)]) == 1:
            begin_index = i
        if words[i] == target:
            end_index = i

    visited = [False] * N
    visited[begin_index] = True
    stack = [begin_index]
    while len(stack) > 0:
        curr = stack.pop()
        answer += 1
        if curr == end_index:
            break
        for neighbor in connected[curr]:
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True

    return answer


if __name__ == '__main__':
    test_cases = [
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4),
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
    ]
    for test_case in test_cases:
        begin, target, words = test_case[0]
        expected = test_case[1]
        answer = solution(begin, target, words)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected