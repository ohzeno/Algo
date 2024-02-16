# https://school.programmers.co.kr/learn/courses/15008/lessons/121685
"""
각 완두콩은 자가수분으로 4개의 후손을 남긴다.
Rr은 RR, Rr, Rr, rr을 낳는다.
완두콩의 세대와 해당 세대에서 몇 번째 개체인지를 알면 형질을 바로 계산하는 프로그램을 작성하라.
쿼리 갯수 1~5
쿼리는 [n 세대, p 번째 개체]로 이루어진다.
1 <= n <= 16, 1 <= p <= 4**(n-1)
"""
def get_genom(n, p):
    if n == 1:
        return "Rr"
    parent = get_genom(n - 1, p // 4)  # 한 세대 위 부모
    if parent == 'Rr':
        return ["RR", "Rr", "Rr", "rr"][p % 4]
    return parent

def solution(queries):
    # 1을 빼줘야 몫, 나머지 연산으로 그룹을 추정하기 편하다.
    return [get_genom(n, p - 1) for n, p in queries]

inputdatas = [
    [[[3, 5]], ["RR"]],
    [[[3, 2], [3, 3], [3, 5]], ["RR", "RR", "RR"]],
    [[[3, 8], [2, 2]], ['rr', 'Rr']],
    [[[3, 1], [2, 3], [3, 9]], ["RR", "Rr", "RR"]],
    [[[4, 26]], ["Rr"]],
]

"""
[PCCP 모의고사 #1] 3번 - 유전법칙
레벨 2라는 사람도 있고 레벨4 이상이라는 사람도 있다.
몫과 나머지라는 아이디어는 바로 떠올랐는데, 
그걸 적용하는 데에 시간이 오래 걸렸다.
적어도 레벨 3 이상으로 느껴진다.
"""

# for t in inputdatas:
#     print(solution(*t))
for data, ans in inputdatas:
    res = solution(data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")