# Problem: https://programmers.co.kr/learn/courses/30/lessons/49190

def solution(arrows):
    from collections import deque
    
    CHANGE_X = [-1, -1, 0, 1, 1, 1, 0, -1]
    CHANGE_Y = [0, 1, 1, 1, 0, -1, -1, -1]

    answer = 0
    visited = {}
    path = {}
    q = deque()

    visited[(0, 0)] = False
    q.append((0, 0))

    x, y = 0, 0
    for arrow in arrows:
        for _ in range(2):
            new_x = x + CHANGE_X[arrow]
            new_y = y + CHANGE_Y[arrow]
            visited[(new_x, new_y)] = False
            path[(x, y, new_x, new_y)] = False
            path[(new_x, new_y, x, y)] = True
            q.append((new_x, new_y))
            x, y = new_x, new_y

    x, y = q.popleft()
    visited[(x, y)] = True
    while q:
        new_x, new_y = q.popleft()

        if visited[(new_x, new_y)]:
            if path[(x, y, new_x, new_y)] is False:
                answer += 1
                path[(x, y, new_x, new_y)] = True
                path[(new_x, new_y, x, y)] = True
        else:
            visited[(new_x, new_y)] = True
            path[(x, y, new_x, new_y)] = True
            path[(new_x, new_y, x, y)] = True
            
        x, y = new_x, new_y

    return answer


if __name__ == '__main__':
    test_cases = [
        ([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0], 3)
    ]
    for test_case in test_cases:
        arrows, expected = test_case
        answer = solution(arrows)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
