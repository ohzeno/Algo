# https://school.programmers.co.kr/learn/courses/30/lessons/42891
import heapq

def solution(food_times, k):
    # 음식양을 다 합쳐도 k보다 작거나 같으면 확인할 필요가 없다.
    # 시간 k일 때는 음식이 무조건 남아있지 않을테니 -1 반환.
    if sum(food_times) <= k:
        return -1
    length = len(food_times)  # 남은 접시 수
    q = []
    for i in range(length):
        food_time = food_times[i]
        heapq.heappush(q, (food_time, i + 1))  # 접시별 남은 음식 양과 접시번호 큐에 넣기
    t = 0  # 누적 시간
    eated = 0  # 순회로 '한 접시'에서 섭취한 음식량.
    # 현재 음식이 가장 적게 남은 접시를 순회로 먹어치울 수 있는가?
    while t + (q[0][0] - eated) * length <= k:
        # 음식양 중복이 있어도 괜찮다.
        # while문에 =이 있어 다음 음식도 처리하며, q[0][0]이 0일 것이기에 시간도 더해지지 않는다.
        t += (q[0][0] - eated) * length
        eated = q[0][0]
        heapq.heappop(q)
        length -= 1  # 중복은 알아서 처리될테니 한 접시씩 처리.
    # 남은 순서는 번호순으로 돌아야 하기에 접시 번호로 정렬
    q = sorted(q, key=lambda x: x[1])
    # 남은 접시 중 가장 음식량이 적은 접시를 다 먹어치우지 못할 수 있다.
    # 즉, 아직 순회를 돌 수 있으므로 % length를 해야한다.
    return q[(k - t) % length][1]

inputdatas = [
    [[3, 1, 2], 5]
]

"""
2019 카카오 공채 기출. 문제만 보고 난이도를 구분할 수는 없지만, 이런 문제는 뒤로 미루는게 좋을 듯 하다.
최소 시간만큼 전체에서 빼버리는 걸 한 번 하는 것 까진 생각했지만 계속 할 생각은 못해서 틀렸다.
호텔 방 배정처럼 next_food 딕셔너리를 만들어서 시간을 줄이려 해봤으나 시간초과 이전에 그냥 틀렸다.
아직 해당 풀이의 오류는 모르겠지만 다른 풀이가 시간을 압도적으로 줄여주기에 넘어간다.
idx로 순회하는 것보다 (전체 공제를 위해 남은 음식양 순으로 정렬된) 우선순위 큐를 사용하는게 시간이 절약됐다.
map으로 큐 안의 모든 시간을 공제해봤지만 효율성 테스트에서 시간초과가 떴다.
매번 순회돌며 공제하는 시간을 줄이기 위해 eated를 따로 둬 첫 원소에 대해서만 계산해준다.
공제 후 남은 시간은 순회를 돌만큼이 아니라 생각해서 한 번 더 틀렸었다.
베스트 답변보다 현재 풀이가 더 알아보기 쉬운 듯 하다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
