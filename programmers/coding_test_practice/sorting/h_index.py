# Problem: https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for index, cite in enumerate(citations):
        answer = max(answer, min(index+1, cite))
    return answer


if __name__ == '__main__':
    test_cases = [
        ([3,0,6,1,5], 3)
    ]
    for test_case in test_cases:
        citations, expected = test_case
        answer = solution(citations)
        print('My answer: ', answer)
        print('Expected: ', expected)
        assert answer == expected