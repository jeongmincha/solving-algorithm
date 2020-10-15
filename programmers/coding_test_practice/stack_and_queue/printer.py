# Problem: https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):    
    count = 1
    q = []
    for idx, p in enumerate(priorities):
        q.append((idx, p))
    
    while len(q) > 0:
        max_idx = 0
        max_val = 0

        for idx, elem in enumerate(q):
            if max_val < elem[1]:
                max_idx = idx
                max_val = elem[1]
        
        q = q[max_idx:] + q[:max_idx]
        
        current = q.pop(0)
        if current[0] == location:
            return count
        count += 1

    return len(priorities)


if __name__ == '__main__':
    test_cases = [
        (([2,1,3,2], 2), 1),
        (([1,1,9,1,1,1], 0), 5)
    ]

    for test_case in test_cases:
        priorities, location = test_case[0]
        expected = test_case[1]
        answer = solution(priorities, location)
        print('My answer: ', answer)
        print('Expected: ', expected)
        assert answer == expected
