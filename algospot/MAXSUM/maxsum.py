# Problem: MAXSUM (https://algospot.com/judge/problem/read/MAXSUM)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.24
def find_max_subsum(arr):
    mx = -100 * len(arr)
    cum_sum = 0
    for i in range(len(arr)):
        if cum_sum < 0:
            cum_sum = arr[i]
        else:
            cum_sum += arr[i]
        mx = max(mx, cum_sum)
    return mx


if __name__ == "__main__":
    n_case = int(input())
    for _ in range(n_case):
        N = int(input())
        arr = [int(_) for _ in input().split()]
        print (find_max_subsum(arr))