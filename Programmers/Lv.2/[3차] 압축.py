# https://school.programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    dic = {chr(i): i - 64 for i in range(65, 91)}  # A부터 Z까지 미리 기록
    last = 26  # 현재 dic의 마지막 인덱스.
    ans = []  # 인덱스 기록할 리스트
    i = 0  # 현재 볼 글자 위치
    done = 0  # 종료코드
    while not done:
        ap = 1  # 글자 인덱싱 위한 확장 정도
        while True:
            tmp = msg[i: i + ap]  # 현재 체크할 문자열
            if tmp in dic:  # 딕셔너리에 있다면
                if not tmp == msg[i:]:  # 마지막 문자열이 아니라면 연장
                    ap += 1
                else:  # 마지막 문자열이면 그대로 정답 기록하고 종료
                    ans.append(dic[tmp])
                    done = 1
                    break
            elif tmp not in dic:  # 딕셔너리에 없으면
                ans.append(dic[tmp[:-1]])  # 이전 문자열 인덱스 기록
                last += 1
                dic[tmp] = last  # 딕셔너리에 추가
                break
        i = i + ap - 1  # 추가한 마지막 문자열부터 새로 인덱싱
    return ans

inputdatas = [
    "KAKAO",
    "TOBEORNOTTOBEORTOBEORNOT",
    "ABABABABABABABAB"
]

"""
2018 카카오 블라인드 채용 기출. Lv.2. 옮겨적기, 읽기, 채점 포함 28분 걸렸다.
규칙을 이해하는데 시간이 좀 걸렸다.
"""
for t in inputdatas:
    print(solution(t))
