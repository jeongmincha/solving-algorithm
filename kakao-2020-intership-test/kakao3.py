#-*- coding: utf-8 -*-

def solution(gems):
    set_gems = set(gems)
    answer = [1, len(gems)]
    counter = {gems[0]: 1}
    left_idx, right_idx = 0, 0

    while left_idx <= right_idx < len(gems):
        if len(counter) == len(set_gems):
            if right_idx - left_idx < answer[1] - answer[0]:
                answer = [left_idx+1, right_idx+1]
            if gems[left_idx] in counter:
                if counter[gems[left_idx]] == 1:
                    del counter[gems[left_idx]]
                else:
                    counter[gems[left_idx]] -= 1
            left_idx +=1
        else:
            right_idx += 1
            if right_idx == len(gems):
                break
            if gems[right_idx] in counter:
                counter[gems[right_idx]] += 1
            else:
                counter[gems[right_idx]] = 1

    return answer


def test_solution(gems, answer):
    result = solution(gems)
    print("gems: {}".format(gems))
    print("result: {}".format(result))
    assert result == answer


if __name__ == "__main__":
    gems = [
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
        ["AA", "AB", "AC", "AA", "AC"],
        ["XYZ", "XYZ", "XYZ"],
        ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    ]
    answers = [
        [3, 7],
        [1, 3],
        [1, 1],
        [1, 5]
    ]
    assert len(gems) == len(answers)

    for case_idx in range(len(gems)):
        test_solution(gems[case_idx], answers[case_idx])
