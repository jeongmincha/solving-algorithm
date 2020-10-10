# DRAWRECT Problem
# Author: JeongminCha (cjm9236@me.com)

def different_one(list):
    if list[0] != list[1]:
        if list[0] != list[2]:
            return list[0]
        else:
            return list[1]
    else:
        if list[1] != list[2]:
            return list[2]

def decide_another_point(pt1, pt2, pt3):
    x = [pt1[0], pt2[0], pt3[0]]
    y = [pt1[1], pt2[1], pt3[1]]
    return (different_one(x), different_one(y))

if __name__ == "__main__":
    test_case = int(raw_input())
    for case in range(test_case):
        pt1 = map(int, raw_input().split(' '))
        pt2 = map(int, raw_input().split(' '))
        pt3 = map(int, raw_input().split(' '))
        pt4 = decide_another_point(pt1, pt2, pt3)
        print ("%d %d" % (pt4[0], pt4[1]))

