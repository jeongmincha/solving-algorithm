# Problem: https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    
    stack = []
    for idx, num in enumerate(number):
        while len(stack) > 0 and num > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        
        if k == 0:
            stack += number[idx:]
            break
        
        stack.append(num)
    
    if k > 0:
        stack = stack[:-k]
    return "".join(stack)


if __name__ == '__main__':
    test_cases = [
        (("9999", 3), "9"),
        (("9999", 4), ""),
        (("9999", 0), "9999"),
        (("1924", 2), "94"),
        (("1231234", 3), "3234"),
        (("4177252841", 4), "775841")
    ]
    for test_case in test_cases:
        number, k = test_case[0]
        expected = test_case[1]
        answer = solution(number, k)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
