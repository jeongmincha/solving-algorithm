import string

def compress(msg):
    dic = dict()
    dic_idx = 1
    for c in list(string.ascii_uppercase):
        dic[c] = dic_idx
        dic_idx += 1

    index_numbers = []
    i = 0
    start = i
    end = i+1

    while end <= len(msg):
        w = msg[start:end]
        if w in dic:
            if end == len(msg):
                index_numbers.append(dic[w])
                break
            end += 1      

        if w not in dic:
            end -= 1
            w = msg[start:end]
            index_numbers.append(dic[w])
            dic[msg[start:end+1]] = dic_idx
            dic_idx += 1
            start = end
            end += 1

    return index_numbers

print(compress('KAKAO'))
print(compress('TOBEORNOTTOBEORTOBEORNOT'))
