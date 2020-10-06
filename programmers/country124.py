def solution(n):
    answer = ""
    
    while n > 0:
        reminder = int(n % 3)
        n = int(n / 3)
        
        if reminder == 0:
            n -= 1
            reminder = 4
        
        answer = str(reminder) + answer
    
    return answer


if __name__ == '__main__':
    list_n = [1,2,3,4]
    list_expected = ['1', '2', '4', '11']
    assert len(list_n) == len(list_expected)
    for i in range(len(list_n)):
        print('[Test Case #{:02d}]'.format(i))
        expected = list_expected[i]
        answer = solution(list_n[i])
        print('{}, {}'.format(expected, answer))
        assert solution(list_n[i]) == list_expected[i]
