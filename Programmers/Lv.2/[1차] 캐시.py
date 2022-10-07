# https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:  # 캐시 0이면 다 miss이므로 바로 소모시간 계산해서 반환
        return len(cities) * 5
    time = 0
    cache = deque()
    length = 0  # 매번 len 사용하지 않도록 길이변수 따로 사용
    for city in cities:
        city = city.lower()  # 대소문자 구분 안한다는 문구를 제대로 체크하지 못해서 틀렸었다.
        for i in range(length):  # in을 쓰면 제거하기 곤란함. 그냥 순회돌면서 체크.
            now = cache[i]
            if city == now:  # 캐시에 저장된 데이터면 hit 시간 더해주고
                time += 1
                del cache[i]  # 빼내서
                cache.append(now)  # 가장 최신 조회 위치로 옮겨줌.
                break  # 찾았으면 뒤에거 확인하지 말고 넘겨야함. 이미 배열 수정해서 그대로 순회돌면 오류. 처음에 그래서 틀림.
        else:  # 캐시에 없으면 일단 추가하고 miss 시간 더해줌.
            cache.append(city)
            time += 5
            if length == cacheSize:  # 이미 캐시사이즈 가득찼으면
                cache.popleft()  # 가장 오래 전 조회된 데이터 제거
            else:  # 캐시 비어있으면 그냥 사이즈 갱신
                length += 1
    return time

inputdatas = [
    [3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
    [3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]],
    [2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
    [5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
    [2, ["Jeju", "Pangyo", "NewYork", "newyork"]],
    [0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
]
"""
2018 카카오 공채 기출. 세팅 제외 30분 소요. 배경지식 부족으로 인한 시행착오.
다른 문제와 달리 함수 진행과정을 알려주지 않아서 당황했다. LRU 알고리즘을 직접 찾아봐야 했다. 배경지식 필요...
LRU 알고리즘은 캐시 사이즈를 초과하게 되면 현존 데이터 중 가장 예전에 조회된 데이터부터 삭제하는 것이다.
단어 직역하면 최소한 최근에 사용된. 시간 범주 안에서 방향성을 의미하는 '최근'에 수량 관련 단어인 '최소'가 붙어서 이해할 수 없었다.
least recently가 '가장 최근에'라고 한다. 
~~most recently를 안쓴다고...? 누가 만들었는지 모르겠는데 단어 조합이 괴랄한게 일상용어는 아닌듯...~~
유지하다 라는 동사를 생각하지 못하고 삭제에 집중해서 '가장 최근에 조회된 데이터'를 
삭제할 리는 없는데 왜 저런 이름일까...라고 생각했는데 '가장 최근에 조회된 데이터'만 유지한다고 생각하면 말이 된다.
처음 풀 때 알고리즘을 잘못 이해하여 '가장 이전에 입력된 데이터'를 제거해서 정확도 75/100이 됐었다. 
(조회가 아니라 입력 최신순을 생각함.)
그 때문에 deque를 썼었는데 지금 보면 그냥 리스트 써도 될 것 같다.
cache hit, cache miss는 그냥 문맥 상 의미가 파악됐다.

베스트 답안은 maxlen을 사용해서 popleft 과정을 제거해줬다.
for문 안돌고 in을 사용한 후 index 대신 deque의 remove를 이용해서 제거 후 다시 추가했다.
deque의 remove가 O(n)인데 in 연산 이후 한번 더 순회돌면 시간 효율성이 낮아질 듯 해서 굳이 연습해보진 않았다.
시간 효율성을 따지는 문제는 아니었지만 효율성을 따지는 풀이가 습관이 되는게 좋을거라 판단했다.
지금 실력에는 저런 트릭키한 부분들 익힐 시간에 다른 문제를 풀어보는게 나을 것이다.
"""

for inputdata in inputdatas:
    print(solution(inputdata[0], inputdata[1]))
