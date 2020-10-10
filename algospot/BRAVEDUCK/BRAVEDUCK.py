# Problem: BRAVEDUCK (https://algospot.com/judge/problem/read/BRAVEDUCK)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.24
import math


def dist(s1, s2):
    x1, y1 = s1
    x2, y2 = s2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def solve_braveduck(J, stones):
    visit = [False] * len(stones)
    q = [stones[0]]
    visit[0] = True

    while len(q) is not 0:
        cur = q.pop()
        for i in range(len(stones)):
            d = dist(cur, stones[i])
            if d != 0 and d <= J and visit[i] is False:
                q.append(stones[i])
                visit[i] = True
                if i == len(stones)-1:
                    return "YES"
    
    return "NO"


if __name__ == "__main__":
    n_case = int(input())
    for _ in range(n_case):
        J = int(input())
        start = [int(_) for _ in input().split()]
        end = [int(_) for _ in input().split()]
        n = int(input())
        stones = [None] * n
        for i in range(n):
            stones[i] = [int(_) for _ in input().split()]
        stones.insert(0, start)
        stones.append(end)
        print (solve_braveduck(J, stones))