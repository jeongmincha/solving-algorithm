def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    cities = [e.lower() for e in cities]
    
    answer = 0
    cache = []
    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
    
    return answer


if __name__ == '__main__':
    testcases = [
        ((3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]), 50),
        ((3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]), 21),
    ]
    for input, answer in testcases:
        print("Solution: ", solution(*input))
        print("Expected Answer: ", answer)
        print()
