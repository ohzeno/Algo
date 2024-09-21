# https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    fail_count = {}  # 스테이지별 실패 인원 기록용 딕셔너리
    for i in range(1, N+1):
        fail_count[i] = 0
    for stage in stages:
        if stage <= N:  # N보다 크면 모두 성공한 사례.
            fail_count[stage] += 1
    remain = len(stages)  # 유저 인원
    fails = []  # 임시로 [실패율, 스테이지 번호] 기록할 리스트.
    for i in range(1, N+1):
        if remain:  # remain이 0이면 모두 실패해서 나머지는 다 실패율 0으로 정의.
            tmp = fail_count[i]/remain  # 0 아니니 제로디비전x 실패율임.
            remain -= fail_count[i]  # 실패한 사람 제외하고 다음 스테이지로 넘어감.
            fails.append([tmp, i])  # 실패율, 스테이지 기록
        else:
            fails.append([0, i])  # 남은 유저 없으면 스테이지 실패율 0(문제 조건임)
    # fails의 실패율을 기준으로 내림차순 정렬 후
    # 스테이지 번호를 뽑아서 answer 리스트로 만들었음.
    answer = list(map(lambda x: x[1],
                      sorted(fails, reverse=True, key=lambda x: x[0])
                      ))
    return answer

inputdatas = [
    [5, [2, 1, 2, 6, 2, 4, 3, 3]],
    [4, [4, 4, 4, 4, 4]]
]

"""
2019 카카오 공채 기출. 아무리 졸며 풀었다지만 Lv.1인데 30분동안 못풀었다.
스테이지에 머무르는 사람이 '실패인원'이란 간단한 사실을 캐치하지 못했다.
처음에는 스테이지별 남은 인원, 성공한 인원 리스트를 순회로 업데이트 했다.
stage를 받아서 이전 스테이지까지 성공처리 하며 2중 for문이 사용됐다.
남은 인원, 성공한 인원 리스트를 이용해 성공율 리스트를 만들고
다시 실패율과 스테이지 번호가 들어간 리스트를 만들고
그걸 정렬하고 스테이지 번호를 뽑아 정답 리스트를 만들었었다.
그런 과정들 때문에 2개의 테스트 케이스에서 시간초과가 발생하여 92점 정도 나왔던 것 같다.
잠깐 자서 피로를 풀고 다시 풀어 통과했다.
베스트 답안도 살펴봤지만, O(n)의 count함수가 자주 사용되었다. 
2중 count는 2중 for문과 별로 다르지 않기에, 
count함수를 사용하는 방법을 따로 연습하지는 않기로 했다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
