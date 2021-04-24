#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    # Write your code here
    N = len(c)
    memo = [101 for _ in range(N)]
    memo[0] = 0

    if c[1] == 0:
        memo[1] = 1

    for i in range(2, N):
        if c[i] == 1:
            continue
        memo[i] = min(memo[i - 1] + 1, memo[i - 2] + 1)

    return memo[-1]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + "\n")

    fptr.close()
