# https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math
def solution(fees, records):
    # 기본시간 fees[0]분 fees[1]원
    # 이후 fees[2]분 fees[3]원
    # 입차 후 출차 기록 없으면 23:59 출차로 간주
    # 초과 시간이 단위 시간으로 나누어떨어지지 않으면 올림.
    # 차량 번호가 작은 자동차부터 배열에 담아서 return
    def time_min(data):  # 시간을 분으로 변환해서 return
        hour, minute = data.split(':')
        hour = int(hour) * 60
        minute = int(minute)
        return hour + minute

    def charge(time):  # 누적시간 받아서 요금 반환
        cost = fees[1]  # 기본 비용
        if time > fees[0]:  # 기본시간 초과하면
            time -= fees[0]  # 남은 시간
            cost += math.ceil(time / fees[2]) * fees[3]  # 올림처리하고 비용 추가
        return cost

    car_in = {}  # 입차시간 기록
    car_acc = {}  # 누적 시간 기록
    car_status = {}  # 주차상태인가 아닌가
    costs = []  # 비용, 차번호 넣을 배열
    for record in records:
        time, car, inout = record.split()
        time = time_min(time)
        if inout == 'IN':  # 입차
            car_status[car] = 1  # 주차 상태 반영
            car_in[car] = time  # 입차 시간 갱신
        else:  # 출차
            if car in car_acc:  # 이미 기록 있으면 누적시간 갱신
                car_acc[car] += time - car_in[car]
            else:  # 기록 없으면 누적시간 생성
                car_acc[car] = time - car_in[car]
            car_status[car] = 0  # 출차 상태 반영
    for car in car_in:  # 모든 차량은 입차기록 있음
        if car_status[car]:  # 주차상태면
            if car in car_acc:  # 기록 있으면 누적시간 갱신
                car_acc[car] += time_min('23:59') - car_in[car]
            else:  # 기록 없으면 누적시간 생성
                car_acc[car] = time_min('23:59') - car_in[car]
        costs.append((charge(car_acc[car]), car))  # 비용, 차번호
    # 차번호 기준 정렬한 배열에서 비용만 뽑아서 list처리.
    costs = list(map(lambda x: x[0], sorted(costs, key=lambda x: x[1])))
    return costs

inputdatas = [
    [[180, 5000, 10, 600],
     ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]],
    [[120, 0, 60, 591],
     ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]],
    [[1, 461, 1, 10],
     ["00:00 1234 IN"]]
]

"""
2022 카카오 공채 기출. Lv.2. 데이터 옮겨 적는데만 7분 50초 걸렸다. 43분 소요.
간단한 문제인데 조건을 잘못 이해해 예외케이스를 처리하지 않아 시간이 걸렸다.
차량이 두 번 이상 주차할 수 있고, 각 케이스의 시간을 합산해서 처리해야한다는 점을 나중에 알게 됐다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
