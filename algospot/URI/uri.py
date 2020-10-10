# Problem: URI (https://algospot.com/judge/problem/read/URI)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.22

import urllib.parse


if __name__ == "__main__":
    n_case = int(input())
    for _ in range(n_case):
        s = input()
        print(urllib.parse.unquote(s))