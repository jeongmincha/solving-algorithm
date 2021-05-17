#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    answer = 0

    last_character = s[0]
    consecutive_words = [[last_character, 1]]
    for c in s[1:]:
        if c == last_character:
            consecutive_words[-1][1] += 1
        else:
            consecutive_words.append([c, 1])
        last_character = c
    answer += len(consecutive_words)

    for pair in consecutive_words:
        n = pair[1]
        if n > 1:
            answer += n * (n + 1) // 2 - 1

    for i in range(1, len(consecutive_words) - 1):
        prev_char = consecutive_words[i - 1][0]
        prev_count = consecutive_words[i - 1][1]
        next_char = consecutive_words[i + 1][0]
        next_count = consecutive_words[i + 1][1]
        curr_count = consecutive_words[i][1]

        if prev_char == next_char and curr_count == 1:
            answer += min(prev_count, next_count)

    return answer


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + "\n")

    fptr.close()
