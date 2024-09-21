# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations
def solution(relation):
    """
    RDB에서 릴레이션의 튜플을 유일하게 식별할 수 있는 속성 또는 속성의 집합 중,
    다음 두 성질을 만족하는 것을 후보키라고 한다.
        - 유일성: 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
        - 최소성: 유일성을 가진 키를 구성하는 속성 중 하나라도 제외하는 경우
            유일성이 깨지는 것을 의미함. 즉, 릴레이션의 모든 튜플을 유일하게
            식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
    릴레이션은 2차원 배열.
    컬럼 길이는 1~8, 각 컬러은 릴레이션의 속성.
    로우 길이는 1~20. 각 로우는 릴레이션의 튜플
    릴레이션의 모든 문자열 길이는 1~8, 알파벳 소문자, 숫자로만 이루어짐.
    모든 튜플은 유일하게 식별 가능. 중복튜플X
    인적사항이 주어졌을 때, 후보 키의 최대 개수를 리턴.
    """
    l_r, l_c = len(relation), len(relation[0])
    cols = [i for i in range(l_c)]  # 칼럼들
    candies = []  # 후보키 저장할 배열
    for n in range(1, l_c + 1):  # 몇 개의 컬럼을 선택할 것인가? 최소성을 위해 1부터 시작.
        for case in combinations(cols, n):  # 조합 순회
            # 기존 후보키가 현재 케이스의 부분집합이면 케이스 최소성X
            if any([pre < set(case) for pre in candies]):
                continue
            is_uiq = set()  # 유일성 확인용
            for r in relation:  # 행 순회하며 해당 열 데이터들 튜플로 넣기
                is_uiq.add(tuple([r[idx] for idx in case]))
            if len(is_uiq) == l_r:  # 총 행 수와 set 길이가 같으면 유일하게 식별한 것.
                candies.append(set(case))  # 후보키에 추가.
    return len(candies)  # 후보키 갯수 리턴

inputdatas = [
    [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"],
    ],
    [["ab", "c"], ["a", "bc"], ["x", "yz"], ["x", "c"]],  # 1
    [
        ['a',1,'aaa','c','ng'],
        ['b',1,'bbb','c','g'],
        ['c',1,'aaa','d','ng'],
        ['d',2,'bbb','d','ng']
    ]  # 3. (0), (2, 3), (1, 3, 4)가 되어야함.
]

"""
2019 카카오 공채 기출. Lv.2. 현 시점  완료 7790명  정답률 39%
셀 수가 최대 160이라 브루트포스 사용했다.
28분 첫 제출. 정확성 46.4점.
후보키에 대해 잘 몰라서 틀렸다.
급하게 생각하느라 최소성에 대해서 미리 후보키에 포함되었던 컬럼은 다른 후보키에 포함될 수 없다 생각했다.
즉, (2, 3)이 후보키라면 (3, 4)는 후보키가 될 수 없다고 생각했는데, 3이 단독으로 후보키였던게 아니라서 최소성을 만족한다.
checked 배열로 처리해주던걸 그냥 케이스 째로 set로 기록하고, 부분집합 연산으로 최소성을 확인하도록 바꿨다.
37분 수정안 제출, 통과.

2차 시도. 20분 걸려서 풀었다. subset을 사용했지만 copy를 두 번이나 사용했다.
기존 풀이보다 느리다. 더 빨리 풀었다는 점 제외하면 퇴보했다.
기존 풀이 일부 개선하고 채택. 등호 부분집합 체크 까먹고 있었음.
"""

for t in inputdatas:
    print(solution(t))
