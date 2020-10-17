# Problem: https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    d = {}
    sum_hash = 0

    for person in participant:
        hash_value = hash(person)
        d[hash_value] = person
        sum_hash += hash_value
    
    for person in completion:
        hash_value = hash(person)
        sum_hash -= hash_value
    
    return d[sum_hash]


if __name__ == '__main__':
    test_cases = [
        ((['leo', 'kiki', 'eden'], ['eden', 'kiki']), 'leo'),
        ((['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']), 'vinko'),
        ((['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']), 'mislav')
    ]

    for test_case in test_cases:
        participant, completion = test_case[0]
        expected = test_case[1]
        answer = solution(participant, completion)
        print('My answer: ', answer)
        print('Expected: ', expected)
        assert answer == expected