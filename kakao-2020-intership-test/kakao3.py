#-*- coding: utf-8 -*-

def solution(gems):
    answer = [0, 0]

    set_gems = set(gems)
    counter = {}
    set_counter = set()
    
    length = 100000

    min_end = 0

    counter = {}
    set_counter = set()

    for start in range(len(gems)):
        found_path = False

        for end in range(start, len(gems)):
            current_gem = gems[end]
            if current_gem not in counter.keys():
                counter[current_gem] = 1
                set_counter.add(current_gem)
            else:
                counter[current_gem] += 1
            
            if len(set_counter) == len(set_gems):
                if end-start < length:
                    length = end-start
                    answer[0] = start+1
                    answer[1] = end+1
                
                found_path = True
                min_end = end
                break
        
        if not found_path:
            break

        if gems[start] in counter.keys():
            if counter[gems[start]] == 1:
                del counter[gems[start]]
                set_counter.remove(gems[start])
            else:
                counter[gems[start]] -= 1
        
        if gems[min_end] in counter.keys():
            if counter[gems[min_end]] == 1:
                del counter[gems[min_end]]
                set_counter.remove(gems[min_end])
            else:
                counter[gems[min_end]] -= 1

    return answer


if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print("gems: {}".format(gems))
    print("answer: {}".format(solution(gems)))

    gems = ["AA", "AB", "AC", "AA", "AC"]
    print("gems: {}".format(gems))
    print("answer: {}".format(solution(gems)))

    gems = ["XYZ", "XYZ", "XYZ"]
    print("gems: {}".format(gems))
    print("answer: {}".format(solution(gems)))

    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print("gems: {}".format(gems))
    print("answer: {}".format(solution(gems)))
