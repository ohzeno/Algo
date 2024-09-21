# https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    """
    S D T 각 1 2 3제곱. 점수마다 존재함
    * 현, 이전 점수 2배로 (첫 시도에 나오면 현 점수만 2배)
    * 중첩 가능. 중첩은 4배
    # 현 점수 마이너스. *과 중첩되면 -2배
    *과 #은 점수마다 둘 중 하나만 존재하거나 존재X
    점수|보너스|옵션 3세트 들어옴.
    점수는 0~10
    """
    points = [0] * 3  # 각 회차 포인트 저장할 배열
    orders = []  # 각 회차 명령어 기록할 배열
    bef_idx = 0  # 파싱용 이전 인덱스
    while len(orders) < 3:  # 명령어 셋 채울 때까지 반복
        tmp = dartResult[bef_idx:bef_idx + 3]  # 일단 3자리 가져와서
        if tmp[-1].isdigit():  # 마지막 자리가 숫자면 다음 명령이니까
            orders.append(tmp[:2])  # 2자리까지만 저장
            bef_idx += 2  # 인덱스 2자리 옮기기
        else:  # 마지막 자리가 숫자 아니면 옵션이니까
            orders.append(tmp)  # 세자리 다 저장
            bef_idx += 3  # 인덱스 3자리 옮기기
    for i in range(3):  # 명령 불러오기. i 써야해서 일부러 order in orders 안씀.
        order = orders[i]  # 각 회차 명령
        point = order[0]  # 첫 자리 포인트
        bonus = order[1]  # 두번째 자리 웬만하면 보너스
        exp = 1  # 지수는 초기값 1
        if bonus.isdigit():  # 두번째 자리가 숫자면 10점이니
            point = order[:2]  # 포인트 10
            bonus = order[2]  # 보너스는 세번째 자리
        if bonus == 'D':  # S는 수정 불필요. D와 T만 지수 수정
            exp = 2
        elif bonus == 'T':
            exp = 3
        points[i] = int(point) ** exp  # 이번 회차 포인트 반영
        if order[-1] in '*#':  # 마지막 자리 옵션 있으면
            opt = order[-1]
            if opt == '*':  # *이면 일단 현 점수 2배
                points[i] *= 2
                if i != 0:  # 첫 회차 아니면 이전 회차 점수도 2배
                    points[i - 1] *= 2
            else:  # #이면 이번 회차 마이너스
                points[i] *= -1
    return sum(points)  # 다 더하면 최종점수


# 파싱 편하게 개선. 길이는 별로 안변함.
def solution2(dartResult):
    points = [0] * 3  # 포인트 저장할 배열
    orders = []  # 명령어 저장할 배열
    dartResult = dartResult.replace('10', 't')  # 10을 한자리로 처리하기 위해 t로 교체.
    new_str = dartResult[0]  # 파싱 편하게 수정할 문자열
    for i in range(1, len(dartResult)):  # 첫 자리는 이미 넣었으니 넘기기
        # 이전 문자열이 알파벳이고 현 문자열이 점수면(이전 문자열이 t라면 후자가 성립 안해서 ㄱㅊ)
        # 현 문자열부터 다음 명령이고, 이전 문자열에 옵션 없으니 임의옵션으로 ! 추가
        if new_str[-1].isalpha() and (dartResult[i].isdigit() or dartResult[i] == 't'):
            new_str += '!' + dartResult[i]
        else:  # 다른 경우는 그대로 복사
            new_str += dartResult[i]
    if new_str[-1].isalpha():  # 마지막 자리 알파벳이면 옵션 추가
        new_str += '!'
    for i in range(3):  # 새 문자열 3자리씩 파싱해서 orders에 추가
        orders.append(new_str[i*3: i*3 + 3])
    for i in range(3):  # 명령 순회
        order = orders[i]
        if order[0] == 't':  # t는 10점
            p = 10
        else:  # 첫 자리는 점수
            p = int(order[0])
        exp = 1  # S는 지수 수정 불필요
        # idx 1은 무조건 보너스. DT 지수 수정
        if order[1] == 'D':
            exp = 2
        elif order[1] == 'T':
            exp = 3
        points[i] = p ** exp  # 포인트 반영
        # 마지막 자리 옵션 #*만 체크.
        if order[2] == '#':  # #인 경우 마이너스
            points[i] *= -1
        elif order[2] == '*':  # *이면 2배
            points[i] *= 2
            if i != 0:  # 첫 명령 아닌 경우 이전 점수도 2배
                points[i - 1] *= 2
    return sum(points)  # 합산하여 리턴


inputdatas = [
    '1S2D*3T', '1D2S#10S',
    '1D2S0T', '1S*2T*3S',
    '1D#2S*3S', '1T2D3D#',
    '1D2S3T*'
]

"""
2018 카카오 공채 기출. Lv.1인데 35분이나 걸렸다.
각 회차의 문자열로 나누는 과정을 생각해내는데 시간이 좀 걸렸다.
파싱이 끝나면 별 문제는 없다.
베스트 답안들을 살펴봤는데, re.compile을 이용해 정규표현식을 이용하는 방법이 있었다.
익숙해지면 상당히 편하겠지만 지금 연습할 부분은 아니라 넘겼다.
다른 답안은 10을 k로 replace하는게 상당히 인상깊었다. 
숫자가 1~2자리라 파싱이 귀찮아지는 과정을 해결할 수 있는 좋은 방법이다.
해당 방법을 이용해 답안을 개선해봤지만 길이는 딱히 안달라졌다.
파싱때 헷갈릴 이유가 없어졌지만 명령어들을 수정하는 과정이 길다.
"""
for t in inputdatas:
    print(solution2(t))
