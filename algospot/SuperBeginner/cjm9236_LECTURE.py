# LECTURE problem (https://algospot.com/judge/problem/read/LECTURE)
# Author: JeongminCha (cjm9236@me.com)

def sort_strings(str):
    str_list = []
    for index in range(0,len(str),2):
        str_list.append(str[index:index+2])
    printing_string = ""
    for elem in sorted(str_list):
        printing_string += elem
    print(printing_string)

if __name__ == "__main__":
    test_case = int(raw_input())
    for case in range(test_case):
        sort_strings(raw_input())