# Problem: https://programmers.co.kr/learn/courses/30/lessons/43165

answer = 0

def dfs(idx, numbers, target, curr):
    global answer
    if idx == len(numbers) and target == curr:
        answer += 1
        return
    if idx == len(numbers):
        return
    
    dfs(idx+1, numbers, target, curr+numbers[idx])
    dfs(idx+1, numbers, target, curr-numbers[idx])


def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer


if __name__ == '__main__':
    test_cases = [
        (([1,1,1,1,1], 3), 5)
    ]
    for test_case in test_cases:
        number, target = test_case[0]
        expected = test_case[1]
        answer = solution(number, target)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert expected == answer