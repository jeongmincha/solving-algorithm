# Problem: NQUEEN (https://algospot.com/judge/problem/read/NQUEEN)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.16


def place_queen(pos, x, y):
    """
    :param pos: a dict (key=x, value=y)
    :param x: pos x to put
    :param y: pos y to put
    :return: bool value meaning possibility
    """
    if y in pos.values():
        return False
    row = 1
    while row < x:
        diff_x = abs(row - x)
        diff_y = abs(pos[row] - y)
        if diff_x == diff_y:
            return False
        row += 1
    return True


def clear_future_blocks(pos, row, n):
    for r in range(row, n+1):
        pos[r] = None
    return pos


def nqueen(pos, row, n):
    for col in range(1, n+1):
        pos = clear_future_blocks(pos, row, n)
        if place_queen(pos, row, col):
            pos[row] = col
            if row == n:
                global answer
                answer += 1
                return
            else:
                nqueen(pos, row+1, n)


if __name__ == "__main__":
    num_case = int(input())
    for _ in range(num_case):
        answer = 0
        pos = {}
        n = int(input())
        nqueen(pos, 1, n)
        print (answer)
