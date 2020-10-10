# Problem: HOTSUMMER (https://algospot.com/judge/problem/read/HOTSUMMER)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.15

def hotsummer(goal, uses):
    if goal >= sum(uses):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    num_builds = int(input())
    for _ in range(num_builds):
        goal = int(input())
        uses = [int(_) for _ in input().split()]
        print (hotsummer(goal, uses))