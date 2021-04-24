#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    answer = 0
    matches = {}
    for i in range(n):
        if ar[i] not in matches:
            matches[ar[i]] = ""
        else:
            del matches[ar[i]]
            answer += 1

    return answer


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
