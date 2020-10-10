# MISPELL problem (https://algospot.com/judge/problem/read/MISPELL)
# Author: JeongminCha (cjm9236@me.com)

def MISPELL(case, input):
    n = int(input[0])
    input_str = list(input[1])
    del input_str[n-1]
    print(case+1),
    print(''.join(input_str))

if __name__ == "__main__":
    test_case = int(raw_input())
    for case in range(test_case):
        MISPELL(case, raw_input().split(' '))