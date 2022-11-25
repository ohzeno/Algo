# https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    # 각 유저는 한 번에 한 명 신고 가능
    # 신고 횟수 제한X
    # 한 유저를 여러 번 신고해도 1회로 처리됨
    # k번 이상 신고된 유저는 게시판 이용 정지.
    # 신고한 모든 유저에게 정지 사실을 메일로 발송
    # 유저가 신고한 모든 내용 취합 후 마지막에 한꺼번에 게시판 이용 정지 시키면서 메일 발송
    answer = []
    user_dic = {
        user: {
            'report': [], 'reported': 0, 'mailed': 0
        } for user in id_list
    }
    for r in report:
        reporter, reported = r.split()
        # 이미 신고한 유저가 아니라면 기록
        if reported not in user_dic[reporter]['report']:
            user_dic[reporter]['report'].append(reported)
            user_dic[reported]['reported'] += 1
    for user in id_list:  # 유저 순회
        # 유저가 신고한 대상들 순회
        for r in user_dic[user]['report']:
            # 신고당한 횟수가 k번 이상이면 신고자에게 메일 추가
            if user_dic[r]['reported'] >= k:
                user_dic[user]['mailed'] += 1
        # 최종 메일 개수 정답배열에 추가
        answer.append(user_dic[user]['mailed'])
    return answer

inputdatas = [
    [["muzi", "frodo", "apeach", "neo"],
     ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
     2],
    [["con", "ryan"],
     ["ryan con", "ryan con", "ryan con", "ryan con"],
     3]
]

"""
2022 카카오 공채 기출. Lv.1. 옮겨적기부터 채점까지 18분 걸렸다.
정확성 테스트에 10초 시간제한이 걸린 특이한 문제.
그냥 생각나는대로 구현하면 정답이다.
베스트 풀이를 보니 set를 이용해 중복신고를 제거했다.
조건을 다시 생각해보면 같은 신고자가 같은 신고대상을 신고한 것이 무효이니 set을 사용하면 편하다.
"""
for t in inputdatas:
    print(solution(t[0], t[1], t[2]))
