# Problem: https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    current_weight = 0
    q = []

    for truck in truck_weights:
        while True:
            if len(q) == bridge_length:
                current_weight -= q.pop(0)
            else:
                if current_weight + truck > weight:
                    q.append(0)
                    answer += 1
                else:
                    q.append(truck)
                    current_weight += truck
                    answer += 1
                    break

    return answer + bridge_length


if __name__ == '__main__':
    test_cases = [
        ((2, 10, [7,4,5,6]), 8),
        ((100, 100, [10]), 101),
        ((100, 100, [10,10,10,10,10,10,10,10,10,10]), 110)
    ]

    for test_case in test_cases:
        bridge_length, weight, truck_weights = test_case[0]
        expected = test_case[1]
        answer = solution(bridge_length, weight, truck_weights)
        print('My answer: ', answer)
        print('Expected: ', expected)
        assert answer == expected
