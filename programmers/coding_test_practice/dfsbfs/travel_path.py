# Problem: https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    tickets.sort(key=lambda x: x[1], reverse=True)

    path = {}
    for ticket in tickets:
        start, end = ticket
        if start in path:
            path[start].append(end)
        else:
            path[start] = [end]
    
    stack = ["ICN"]
    answer = []

    while len(stack) > 0:
        curr = stack[-1]
        if curr not in path or len(path[curr]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(path[curr].pop())

    return list(reversed(answer))


if __name__ == '__main__':
    test_cases = [
        ([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], ["ICN", "JFK", "HND", "IAD"]),
        ([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]], ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]),
        ([["ICN", "SFO"]], ["ICN", "SFO"])
    ]
    for test_case in test_cases:
        tickets, expected = test_case
        answer = solution(tickets)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
