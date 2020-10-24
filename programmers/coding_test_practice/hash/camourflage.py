# Problem: https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    closet = {}
    for cloth in clothes:
        name, category = cloth
        if category not in closet:
            closet[category] = []
        closet[category].append(name)
    
    for v in closet.values():
        answer *= len(v)+1

    return answer-1


if __name__ == '__main__':
    test_cases = [
        ([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]], 5),
        ([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]], 3)
    ]

    for test_case in test_cases:
        clothes = test_case[0]
        expected = test_case[1]
        answer = solution(clothes)

        print('My answer: ', answer)
        print('Expected : ', expected)
        assert answer == expected
