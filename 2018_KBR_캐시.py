def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            answer += 5
            if cache and cacheSize <= len(cache):
                cache.pop(0)
        if cacheSize > 0:
            cache.append(city)
    return answer