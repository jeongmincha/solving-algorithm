# Problem: XHAENEUNG (https://algospot.com/judge/problem/read/XHAENEUNG)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.23


def solve(sent):
    decode = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
    encode = {v: k for k, v in decode.items()}

    elems = sent.split()
    a = decode[elems[0]]
    b = decode[elems[2]]
    c = elems[4]

    ans = 0
    if elems[1] == '+':
        ans = a + b
    elif elems[1] == '-':
        ans = a - b
    else:
        ans = a * b

    if ans < 0 or ans > 10:
        return "No"

    sorted_ans = ''.join(sorted(encode[ans]))
    sorted_c = ''.join(sorted(c))
    if sorted_ans == sorted_c:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    n_case = int(input())
    for _ in range(n_case):
        sent = input()
        print (solve(sent))