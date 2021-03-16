# Problem: https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0
    rocks += [0, distance]
    rocks.sort()

    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2

        count = 0
        last = rocks[0]
        for i in range(1, len(rocks)):
            gap = rocks[i] - last
            if gap < mid:
                count += 1
            elif i != len(rocks):
                last = rocks[i]
        
        if count > n:
            end = mid-1
        else:
            start = mid+1
            answer = mid

    return answer


if __name__ == '__main__':
    test_cases = [
        ((25, [2, 14, 11, 21, 17], 2), 4)
    ]
    for test_case in test_cases:
        distance, rocks, n = test_case[0]
        expected = test_case[1]
        answer = solution(distance, rocks, n)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
