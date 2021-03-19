def solution(n, words):
    answer = [0, 0]

    # Use it as a hash-table for O(1) search
    visited = {}

    idx = 0
    last = ""
    for idx, word in enumerate(words):
        is_visited = word in visited
        is_not_word_chained = len(last) > 0 and word[0] != last[-1]

        if is_visited or is_not_word_chained:
            answer = [idx % n + 1, idx // n + 1]
            return answer

        visited[word] = True
        last = word

    return answer


if __name__ == '__main__':
    test_cases = [
        ((3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]), [3,3]),
        ((5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]), [0,0]),
        ((2, ["hello", "one", "even", "never", "now", "world", "draw"]), [1,3])
    ]
    for test_case in test_cases:
        n, words = test_case[0]
        expected = test_case[1]
        answer = solution(n, words)
        print('Solution: ', answer)
        print('Expected: ', expected)
        assert answer == expected
