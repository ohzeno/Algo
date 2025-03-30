# https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""
constraints:

"""


from collections import OrderedDict

def solution(cacheSize, cities):
    hit, miss = 1, 5
    if cacheSize == 0:
        return len(cities) * miss
    time = 0
    cache = OrderedDict()
    cache_len = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            time += hit
            cache.move_to_end(city)
        else:
            time += miss
            if cache_len == cacheSize:
                # last=True로 설정하면 popitem()이 가장 최근에 조회된 데이터를 제거
                cache.popitem(last=False)
                cache_len -= 1
            cache[city] = None
            cache_len += 1
    return time


inputdatas = [
    {"data": [3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]], "answer": 50},
    {"data": [3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]], "answer": 21},
    {"data": [2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]], "answer": 60},
    {"data": [5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]], "answer": 52},
    {"data": [2, ["Jeju", "Pangyo", "NewYork", "newyork"]], "answer": 16},
    {"data": [0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]], "answer": 25}
]


"""
2018 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 22,024명, 정답률 65%
이전에 풀었을 때는 문제에서 lru캐시를 사용하라고 하면서 lru캐시 개념을 설명 
안해줘서 상당히 고생했었다. 이번엔 OrderedDict를 사용해봤다.
dict도 3.7부터 순서가 보장되니 dict로 풀어도 된다.
set도 순서가 보장되니 set으로 풀어도 되지만 
자료구조 관점으로는 set은 순서가 없는 집합이라서 오해가 생길 수 있다.
3회차. 상수 안쓰고 풀었는데 지금 보니 2회차 풀이가 실수는 적을 것 같다.
"""

for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
