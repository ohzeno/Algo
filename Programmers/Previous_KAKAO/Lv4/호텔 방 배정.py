# https://programmers.co.kr/learn/courses/30/lessons/64063
def solution(k, room_number):
    next_room = {}
    for number in room_number:
        visited = [number]
        while number in next_room:
            number = next_room[number]
            visited.append(number)
        for v in visited:
            next_room[v] = number + 1
    return list(next_room.keys())
"""
2019 카카오 겨울 인턴십 기출
리스트만을 이용한 풀이에선 시간초과.
in 연산이 O(1)인 딕셔너리 이용으로 시간줄이기.
딕셔너리 첫 풀이 효율성테스트 1개만 통과.
딕셔너리 첫 풀이에서는 next_room[number] += 1를 매 순간 해줬다.
1 3 4를 방문하고 최종 4가 배정되었다면 1에는 3이 할당된채로 다음 배정을 실시한다.
그래서 고객이 1을 요청하면 다시 3을 방문하고 5를 가게 되면서 리스트와 비슷하게 
하나하나 순회하는 시간을 사용한다(인덱싱 +1로 한단계 건너뜀).
반면 정답 풀이는 visited를 사용하여 1 3 4에 최종적으로 number+1을 할당하기 때문에
다시 1 요청이 들어오면 3을 거치지 않고 바로 5로 간다.
"""
# 딕셔너리 첫 풀이
def solution1(k, room_number):
    next_room = {}
    for number in room_number:
        while number in next_room:
            next_room[number] += 1
            number = next_room[number] - 1
        next_room[number] = number + 1
    return list(next_room.keys())

inputdatas = [
    (10, [1,3,4,1,3,1]),
]
for inputdata in inputdatas:
    print(solution(inputdata[0], inputdata[1]))
