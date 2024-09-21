# https://school.programmers.co.kr/learn/courses/30/lessons/64064
def solution(user_id, banned_id):
    # 유저id 중복없음
    # 밴id 순서 달라도 같은 쌍으로 취급.
    ban_dic = {banned: [] for banned in banned_id}  # 밴 목록별 대응 유저 기록
    for user in user_id:  # 유저 순회
        for banned in banned_id:  # 밴목록 순회
            if len(banned) == len(user):  # id길이 같은 경우만 체크
                for i in range(len(user)):  # 글자 순회
                    if banned[i] == '*':  # *이면 체크 필요없음
                        continue
                    elif user[i] == banned[i]:  # * 아니고 일치하면 다음으로
                        continue
                    else:  # *도 아니고 서로 다르면 끝내고 다음 밴목록으로
                        break
                else:  # break 안됐으면 밴목록임.
                    if user not in ban_dic[banned]:  # 중복 아니면 추가
                        ban_dic[banned].append(user)
    ans = []  # 정답 배열.
    # set에 리스트를 넣을 수는 없고 다른 형태로 가공해서 넣긴 귀찮아서 리스트를 사용했다.
    def dfs(datas, cnt):
        if cnt == len(banned_id):  # 밴목록 순회 끝났으면
            if len(set(datas)) < len(banned_id):  # id 자체 중복있으면 제외
                return
            datas = sorted(datas)  # 중복없으면 정렬로 순서 관계 없게 만듦
            if datas not in ans:  # 배열 자체 중복 없으면 정답케이스 추가
                ans.append(datas)
            return
        for ban in ban_dic[banned_id[cnt]]:  # 순회 안끝났으면 밴id 순회
            dfs(datas + [ban], cnt + 1)  # 현 케이스에 id 추가해주고 다음 밴목록 순회하도록
    dfs([], 0)
    return len(ans)  # 정답케이스 개수 반환

inputdatas = [
    [["frodo", "fradi", "crodo", "abc123", "frodoc"],
     ["fr*d*", "abc1**"]],
    [["frodo", "fradi", "crodo", "abc123", "frodoc"],
     ["*rodo", "*rodo", "******"]],
    [["frodo", "fradi", "crodo", "abc123", "frodoc"],
     ["fr*d*", "*rodo", "******", "******"]]
]

"""
2019 카카오 개발자 겨울 인턴십 기출. 데이터 옮겨적는데만 4분 30초 걸렸다. Lv.3 문제. 
힌트 찾아본 시간 포함 50분쯤 걸렸다.
한 15분 풀다가 생각나는 방법들은 효율성체크 없어도 시간초과 나겠다 싶어서 다른 사람의 풀이방식을 훑어봤다.
다 읽진 않았고 '유저를 밴목록과 대조한다'는 아이디어만 얻고 다시 풀었다.
기존에 시간초과가 날 것 같다고 생각한 이유는 처음에 시간효율성 체크가 없는 것을 보고
일단 브루트포스를 해보자 해서
밴목록에서 *을 a~z, 0~9로 바꿔가며 유저목록과 일일이 대조하려 했었다.
36^7이라는 미친 시간소모가 나올 수 있어서(8글자인 경우는 대조없이 길이 같은 모든 유저와 대응처리)
글자별로 노드 만드는 문자열탐색 방식을 사용해야 하나 생각했었다.
단순히 유저쪽을 갖고와서 대조해보면 *을 36이 아니라 1의 시간으로 처리할 수 있다.
창의적으로 풀려다가 시간초과로 망친 적이 많아서, 
일단 문제에서 주어진 대로 브루트포스부터 해보는 습관이 생겼었다.
오히려 한 방법에 집중하는 것으로 망친 케이스다. 실전에서 이랬으면 40분 이상 쓰고 못풀고 넘어갔을수도.
찾아본 풀이는 permutations 라이브러리를 사용했으나 지금 연습할 함수는 아니라 판단하여 넘어간다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
