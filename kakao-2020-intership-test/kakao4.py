#-*- coding: utf-8 -*-

def solution(board):
    import heapq, math

    DIRECTIONS = [(0,1),(1,0),(-1,0),(0,-1)]
    N = len(board)
    D = len(DIRECTIONS)

    # N X N X D
    dist = [[[math.inf for _ in range(D)] for _ in range(N)] for _ in range(N)]
    for i, _ in enumerate(DIRECTIONS):
        dist[0][0][i] = 0
    
    # 처음에는 (0,0) 위치에서 4방향으로 가려는 상태를 queue에 넣어둔다.
    q = []
    for _, direction in enumerate(DIRECTIONS):
        q.append((0,0,0,direction))

    # queue를 사용하여 BFS 사용. (매 노드에서 이동 가능한 경우를 queue에 넣고 queue가 비어질때까지 반복)
    while len(q) is not 0:
        cur_x, cur_y, cur_dist, last_direction = q.pop()

        for i, current_direction in enumerate(DIRECTIONS):
            new_x = cur_x + current_direction[0]
            new_y = cur_y + current_direction[1]
            new_dist = cur_dist

            # 다시 되돌아가려는 경우, 무시
            if abs(last_direction[0] - current_direction[0]) == 2 or abs(last_direction[1] - current_direction[1]) == 2:
                continue
                
            # 접근할 수 없는 곳으로 가려 할 때, 무시
            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N or board[new_x][new_y] == 1:
                continue

            if last_direction is current_direction: # 직진일 경우
                new_dist += 100
            else:                                   # 직진이 아닌 경우 코너가 생성됨
                new_dist += 600
            
            if dist[new_x][new_y][i] > new_dist:
                dist[new_x][new_y][i] = new_dist
                q.append((new_x, new_y, new_dist, current_direction))

    # dist[N-1][N-1]에 저장되어 있는 4방향의 값 중 가장 최소값을 사용
    return min(dist[N-1][N-1])


if __name__ == "__main__":
    board = [
        [[0,0,0],[0,0,0],[0,0,0]],
        [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
        [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],
        [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
    ]
    answer = [
        900,
        2100,
        3800,
        3200
    ]
    assert len(board) == len(answer)

    for case_idx in range(len(board)):
        result = solution(board[case_idx])
        print("board: {}".format(board[case_idx]))
        print("result: {}".format(result))
        assert result == answer[case_idx]
