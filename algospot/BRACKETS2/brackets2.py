# Problem: BRACKETS2 (https://algospot.com/judge/problem/read/BRACKETS2)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.17


def solve_brackets2(string):
    string = list(string)
    match = {"(": ")", "{": "}", "[": "]"}
    stack = []

    if len(string) % 2 is not 0:
        return "NO"

    for i in range(len(string)):
        c = string[i]
        if c is "(" or c is "{" or c is "[":
            stack.append(c)
        else:
            if len(stack) is 0:
                return "NO"
            elif c is not match[stack.pop()]:
                break

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    n_case = int(input())
    for _ in range(n_case):
        string = input()
        print (solve_brackets2(string))