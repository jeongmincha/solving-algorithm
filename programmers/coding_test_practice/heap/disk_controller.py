# Problem: https://programmers.co.kr/learn/courses/30/lessons/42627

def solution(jobs):
    answer = 0
    elapse_time = 0
    N = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])

    while len(jobs) > 0:
        finished = False

        for i in range(len(jobs)):
            if jobs[i][0] <= elapse_time:
                elapse_time += jobs[i][1]
                answer += elapse_time - jobs[i][0]
                jobs.pop(i)
                finished = True
                break

        if not finished:
            elapse_time += 1

    return int(answer / N)


if __name__ == '__main__':
    test_cases = [
        ([[0,3], [1,9],[2,6]], 9)
    ]
    for test_case in test_cases:
        jobs, expected = test_case
        answer = solution(jobs)
        print('My answer: ', answer)
        print('Expected:  ', expected)
        assert answer == expected
