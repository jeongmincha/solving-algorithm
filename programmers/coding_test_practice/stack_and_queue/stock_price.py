# Problem: https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = [(0, prices[0])]

    for idx, price in enumerate(prices[1:]):
        while len(stack) > 0 and stack[-1][1] > price:
            answer[stack[-1][0]] = idx+1 - stack[-1][0]
            stack.pop()
        
        stack.append((idx+1, price))
        print(stack)

    while len(stack) != 0:
        idx, price = stack.pop()
        answer[idx] = len(prices)-1-idx

    return answer


if __name__ == '__main__':
    test_cases = [
        ([1,2,3,2,3], [4,3,1,1,0]),
        ([1,2,3,4], [3,2,1,0]),
        ([4,3,2,1], [1,1,1,0])
    ]

    for test_case in test_cases:
        prices, expected = test_case
        answer = solution(prices)
        print('My answer: ', answer)
        print('Expected: ', expected)
        assert answer == expected