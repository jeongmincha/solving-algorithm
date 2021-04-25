#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    # Write your code here
    word_frequency = {}

    for c in s:
        if c in word_frequency:
            word_frequency[c] += 1
        else:
            word_frequency[c] = 1

    frequency_map = {}
    for k, v in word_frequency.items():
        if v in frequency_map:
            frequency_map[v].append(k)
        else:
            frequency_map[v] = [k]

    if len(frequency_map) == 1:
        return "YES"

    if len(frequency_map) == 2:
        max_frequency = max(word_frequency.values())
        min_frequency = min(word_frequency.values())

        # Case 1: remove 1 character of the max frequency
        if max_frequency - min_frequency == 1 and len(frequency_map[max_frequency]) == 1:
            return "YES"
        
        # Case 2: remove 1 chracter of the min frequency
        if min_frequency == 1 and len(frequency_map[min_frequency]) == 1:
            return "YES"

    return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = isValid(s)

    fptr.write(result + "\n")

    fptr.close()
