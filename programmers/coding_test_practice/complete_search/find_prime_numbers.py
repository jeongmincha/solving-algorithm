# Problem: https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

import math

def permutation(arr, r):
    if r == 1:
        return [[e] for e in arr]
    
    N = len(arr)
    ret = []
    for i in range(N):
        temp = permutation(arr[:i] + arr[i+1:], r-1)
        temp = [[arr[i]] + e for e in temp]
        ret += temp
    
    return ret


def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0

    N = len(numbers)
    nums = []
    for i in range(1, N+1):
        perms = permutation(numbers, i)
        perms = [int(''.join(e)) for e in perms]
        nums += perms

    nums = set(nums)
    for num in list(nums):
        if is_prime(num):
            answer += 1

    return answer


if __name__ == '__main__':
    test_cases = [
        ("17", 3),
        ("011", 2)
    ]
    for test_case in test_cases:
        numbers, expected = test_case
        answer = solution(numbers)
        print('My answer: ', answer)
        print('Expected:  ', expected)
        assert answer == expected