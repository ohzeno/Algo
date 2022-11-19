# https://school.programmers.co.kr/learn/courses/30/lessons/17687
def solution(n, t, m, p):
    # n진법 t개 숫자 미리 구하기. m명 참가. 본인 순서 p
    # n은 2~16 t는 1~1000 m은 2~100
    # 본인이 말해야 하는 숫자 t개를 공백없이 나열한 문자열.
    # 10~15는 A~F로 표시
    over = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }  # 10 이상 알파벳
    total = '0'  # 0은 항상 들어감.
    i = 1  # 0은 처리했으니 1부터 체크
    ed = m * (t - 1) + p  # p번째 수 t개 말할 때 필요한 최종 글자수
    while len(total) < ed:  # ed 넘어가면 체크 불필요.
        tmp = ''  # i를 n진수로 변환할 변수
        mog = i  # 첫 몫은 i 그대로 넣고 while 진입.
        while mog:  # 몫이 0되면 변환 끝남.
            nam = mog % n
            mog //= n
            if n > 10 and nam >= 10:  # 11진수 이상, 나머지 10 이상은 over에서 알파벳 가져오기
                tmp = str(over[nam]) + tmp
            else:
                tmp = str(nam) + tmp
        total += tmp  # 변환된 문자열 total에 이어붙이기
        i += 1  # i 올려서 계속
    answer = ''
    for i in range(t):  # 문자열에서 p번째 순서 t개 뽑아내기
        answer += total[i * m + p - 1]
    return answer

inputdatas = [
    [2, 4, 2, 1],
    [16, 16, 2, 1],
    [16, 16, 2, 2],
]

"""
2018 카카오 공채 기출. Lv.2. 옮겨적기부터 채점까지 31분 걸렸다.
규칙이 혼란스러워 시간을 좀 낭비했다. 첫 예시에서 10 이상은 한 자리씩 끊어 말한다고 했다.
나중에는 10 이상은 알파벳 대문자로 표기하라고 했다.
구체적인 설명은 없지만 추론해보면 n진수일 경우 n 이상은 끊어 표기한다.
첫 예시는 10진수라 10부터 끊어 말한 것이다.
그러므로 알파벳을 활용하는 것은 11진수 부터다. 실제로 그렇게 가정하고 풀이하니 통과했다.
"""
for t in inputdatas:
    print(solution(t[0], t[1], t[2], t[3]))
