# ENCRYPT problem (https://algospot.com/judge/problem/read/ENCRYPT)
# Author: JeongminCha (cjm9236@me.com)

def encrypt(input_str):
    e_str = input_str[0::2]
    del input_str[0::2]
    return ''.join(e_str + input_str)

if __name__ == "__main__":
    test_case = int(raw_input())
    for case in range(test_case):
        ans = encrypt(list(raw_input()))
        print(ans)