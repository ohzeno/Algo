# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    # 채팅방 나간 후 새 닉으로 들어오거나 채팅방에서 닉 변경.
    # 변경될 경우 기존 메시지 닉네임 전부 변경.
    # 최종 메시지 목록 배열로 return
    # record는 1 ~10만 길이
    # 각 단어는 알파벳, 숫자로만 이루어져 있다.
    # 대문자, 소문자 구분함.
    # 유저 아이디, 닉네임 1~10길이
    # 잘못된 입력 X
    ans = []  # 기록 보관할 배열
    user_dic = {}  # uid별로 현재 닉네임, 메시지 위치 JSON으로 기록할 딕셔너리.
    def order(data):
        data = data.split()
        command = data[0]
        uid = data[1]
        if len(data) == 3:  # 3개면 닉네임도 같이 들어온거다.
            nickname = data[2]
        if command == 'Enter':  # 입장.
            ans.append(f"{nickname}님이 들어왔습니다.")
            # uid가 이미 기록돼있고, 닉네임이 변경되었을 경우 로그 갱신
            if uid in user_dic and user_dic[uid]['nickname'] != nickname:
                change_log(uid, nickname)
            logging(uid, nickname)  # 유저데이터 기록/갱신
        elif command == "Leave":  # 퇴장
            # 퇴장은 nickname이 따로 안들어오므로 유저데이터에서 가져온다.
            nickname = user_dic[uid]['nickname']
            ans.append(f"{nickname}님이 나갔습니다.")
            logging(uid, nickname)  # 유저데이터 기록
        elif command == "Change":  # 닉네임 변경. 로그 갱신
            change_log(uid, nickname)

    def logging(uid, nickname):  # 유저데이터 기록/갱신 함수
        if uid in user_dic:  # 이미 데이터 있으면 메시지 위치 추가
            user_dic[uid]['idxs'].append(len(ans) - 1)
        else:  # 데이터 없으면 닉네임, 메시지 위치 기록
            user_dic[uid] = {
                'nickname': nickname,
                'idxs': [len(ans) - 1]
            }

    def change_log(uid, nickname):  # 기존 로그 갱신하는 함수
        for i in user_dic[uid]['idxs']:  # 메시지 위치들 순회하며 새 닉네임으로 변경
            ans[i] = ans[i].replace(user_dic[uid]['nickname'], nickname)
        user_dic[uid]['nickname'] = nickname  # 유저데이터의 닉네임도 새 닉네임으로 변경

    for rec in record:  # 각 명령마다 수행
        order(rec)
    return ans

inputdatas = [
    ["Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",]
]

"""
2019 카카오 공채 기출. Lv.2. 옮겨적기부터 채점까지 31분 걸렸다.
데이터가 리스트면서 단수형이라 좀 헷갈렸다. 구현에 시간이 걸릴 뿐 어렵진 않은 문제.
베스트 풀이를 보니 어차피 최종닉네임으로 기록 되므로 uid별 최종 닉네임을 기록한 후에 로그를 생성했다.
내 풀이는 명령이 들어올 때마다 로그를 생성하고, 실시간 갱신하도록 되어있다.
api를 사용하며 json 데이터를 자주 받다보니 그 관점에서 코드를 작성했다.
문제풀이 관점에선 베스트 풀이가 좋고, 실제 개발 관점에선 내 코드가 좋다.
"""
for t in inputdatas:
    print(solution(t))
