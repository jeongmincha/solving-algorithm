#-*- coding: utf-8 -*-

def solution(numbers, hand):
    assert hand == "left" or hand == "right"

    # numbers 안에서 0만 11로 바꾸고 나머지는 그대로 둔다.
    # #과 * 표시의 경우 12라고 설정하고, 0을 11이라고 설정한 후에 알고리즘 풀이를 시작하는 것이다.
    nums = [(e+10) % 11 + 1 for e in numbers]
    lp = 12
    rp = 12
    result = ""

    for num in nums:
        if num == 1 or num == 4 or num == 7:
            result += "L"
        elif num == 3 or num == 6 or num == 9:
            result += "R"
        else:
            # 현재 손가락 위치와 이동하고자 하는 손가락 위치 사이의 거리를 계산하는 로직
            # 그 둘의 숫자 차이를 빼고, 3으로 나눈 몫과 나머지를 합하면 그 길이를 계산할 수 있다.
            # ex.8과 5 사이에는 3의 차이가 있고, 3으로 나눈 몫과 나머지의 합은 1
            # ex.8과 3 사이에는 5의 차이가 있고, 3으로 나눈 몫과 나머지의 합은 3
            ld = abs(lp-num)
            ld = int(ld / 3) + ld % 3
            rd = abs(rp-num)
            rd = int(rd / 3) + rd % 3

            if ld < rd:
                result += "L"
            elif ld > rd:
                result += "R"
            else:
                if hand == "left":
                    result += "L"
                elif hand == "right":
                    result += "R"
        
        # 마지막으로 이동한 손가락에 따라서 해당 손가락의 위치를 업데이트 해줌.
        last_p = result[-1]
        if last_p == "L":
            lp = num
        elif last_p == "R":
            rp = num

    return result
        

if __name__ == "__main__":
    print("=================== TEST ====================")
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
    hand = "right"
    print("numbers: {}\nhand: {}".format(numbers, hand))
    print("answer: {}\n".format(solution(numbers, hand)))

    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2];
    hand = "left"
    print("numbers: {}\nhand: {}".format(numbers, hand))
    print("answer: {}\n".format(solution(numbers, hand)))

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
    hand = "right"
    print("numbers: {}\nhand: {}".format(numbers, hand))
    print("answer: {}".format(solution(numbers, hand)))
    print("================ TEST DONE =================")
