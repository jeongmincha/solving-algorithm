# Problem: https://programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    import heapq
    answer = 0
    heap = [e for e in scoville]
    heapq.heapify(heap)
    
    while heap[0] < K:
        if len(heap) > 1:
            first, second = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, first + second * 2)
        else:
            answer = -1
            break
        answer += 1

    return answer


if __name__ == '__main__':
    test_cases = [
        (([1,2,3,9,10,12], 7), 2)
    ]

    for test_case in test_cases:
        scoville, K = test_case[0]
        expected = test_case[1]
        answer = solution(scoville, K)
        print('My answer: ', answer)
        print('Expected:  ', expected)
        assert answer == expected