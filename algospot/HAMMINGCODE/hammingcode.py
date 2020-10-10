# Problem: HAMMINGCODE (https://algospot.com/judge/problem/read/HAMMINGCODE)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.24


def XOR(a,b):
    return not((not a or b) and (a or not b))


def decode(s):
    idx = 0
    idx += XOR(XOR(s[0], s[2]), XOR(s[4], s[6])) * 1
    idx += XOR(XOR(s[1], s[2]), XOR(s[5], s[6])) * 2
    idx += XOR(XOR(s[3], s[4]), XOR(s[5], s[6])) * 4
    
    if idx != 0:
        if s[idx-1] == 1:
            s[idx-1] = 0
        elif s[idx-1] == 0:
            s[idx-1] = 1
    
    return str(s[2]) + str(s[4]) + str(s[5]) + str(s[6])


if __name__ == "__main__":
    n_case = int(input())
    for _ in range(n_case):
        string = input()
        string = [int(_) for _ in list(string)]
        print(decode(string))