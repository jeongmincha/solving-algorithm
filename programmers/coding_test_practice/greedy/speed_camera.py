# Problem: https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    camera = 0
    routes.sort(key=lambda x: x[1])
    N = len(routes)
    checked = [False for _ in range(N)]
    print(routes)

    for idx in range(N):
        if not checked[idx]:
            camera = routes[idx][1]
            answer += 1
        for another in range(idx+1, N):
            start, end = routes[another]
            if start <= camera <= end and not checked[another]:
                checked[another] = True
    
    return answer


if __name__ == '__main__':
    test_cases = [
        ([[-20,15], [-14,-5], [-18,-13], [-5,-3]], 2)
    ]
    for test_case in test_cases:
        routes, expected = test_case
        answer = solution(routes)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected