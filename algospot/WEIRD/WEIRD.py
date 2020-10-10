# Problem: WEIRD (https://algospot.com/judge/problem/read/WEIRD)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.23
import math


def proper_divisors(num):
    divisors = []
    for n in range(1, int(math.sqrt(num))+1):
        if num % n == 0:
            divisors.append(n)
            divisors.append(int(num / n))
    divisors = sorted(divisors)
    divisors = divisors[:-1]
    return divisors


def find_subset(arr, subset, sum, idx, subsetIdx):
    if idx == len(arr):
        return False
    if arr[idx] == sum:
        subset[subsetIdx] = arr[idx]
        return True

    for i in range(idx, len(arr)):
        if arr[i] > sum:
            continue
        if arr[i] == sum:
            subset[subsetIdx] = arr[i]
            return True
        subset[subsetIdx] = arr[i]
        if find_subset(arr, subset, sum-arr[i], i+1, subsetIdx+1):
            return True

    return False

def find_subset_sum(arr, sum):
    subset = [0] * len(arr)
    return find_subset(arr, subset, sum, 0, 0)


def is_weird(num):
    divisors = proper_divisors(num)
    if sum(divisors) < num:
        return "not weird"

    if find_subset_sum(divisors, num):
        return "not weird"
    else:
        return "weird"


if __name__ == "__main__":
    n_case = int(input())
    # n_case = 1
    for _ in range(n_case):
        num = int(input())
        print(is_weird(num))