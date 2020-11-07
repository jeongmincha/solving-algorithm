# Problem: https://programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    import heapq

    def heappop_min(h):
        heapq.heapify(h)
        return heapq.heappop(h)
    
    def heappop_max(h):
        heapq._heapify_max(h)
        return heapq.heappop(h)

    h = []
    for operation in operations:
        op, num = operation.split(" ")
        if op == "I":
            h.append(int(num))
        elif len(h) > 0:
            if num == "-1":
                heappop_min(h)
            else:
                heappop_max(h)

    if len(h) == 0:
        return [0, 0]
    if len(h) == 1:
        return [h[0], h[0]]
    else:
        mx = heappop_max(h)
        mn = heappop_min(h)
        return [mx, mn]


if __name__ == '__main__':
    test_cases = [
        (["I 16", "D 1"], [0,0]),
        (["I 7", "I 5", "I -5", "D -1"], [7,5]),
        (["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"], [0,0]),
        (["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"], [333,-45])
    ]
    for test_case in test_cases:
        operations, expected = test_case
        answer = solution(operations)
        print('My answer: ', answer)
        print('Expected:  ', expected)
        assert answer == expected
