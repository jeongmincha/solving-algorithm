# Problem: https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []

    album_sum = {}
    album_list = {}

    for genre in set(genres):
        album_sum[genre] = 0
        album_list[genre] = []

    for index in range(len(plays)):
        genre, play = genres[index], plays[index]

        album_sum[genre] += play
        album_list[genre].append((index, play))
    
    for genre, _ in sorted(album_sum.items(), key=lambda x: x[1], reverse=True):
        for index, _ in sorted(album_list[genre], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(index)

    return answer


if __name__ == '__main__':
    test_cases = [
        ((["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]), [4,1,3,0])
    ]

    for test_case in test_cases:
        genres, plays = test_case[0]
        expected = test_case[1]
        answer = solution(genres, plays)

        print('My answer: ', answer)
        print('Expected : ', expected)
        assert answer == expected
