def solution(msg):
    import string

    answer = []
    word_dict = {}
    for idx, alphabet in enumerate(string.ascii_uppercase):
        word_dict[alphabet] = idx+1

    N = len(msg)
    start, end = 0, 0
    while True:
        end += 1
        if end == N:
            answer.append(word_dict[msg[start:]])
            break
        next_word = msg[start:end+1]
        if next_word not in word_dict:
            word_dict[next_word] = len(word_dict) + 1
            answer.append(word_dict[msg[start:end]])
            start = end
        
    return answer


if __name__ == '__main__':
    test_cases = [
        ("KAKAO",  [11,1,27,15])
    ]
    for test_case in test_cases:
        msg, expected = test_case
        answer = solution(msg)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
