# https://school.programmers.co.kr/learn/courses/30/lessons/150367
from collections import deque
def solution(numbers):
    """
    1. 이진수를 저장할 빈 문자열 생성
    2. 주어진 이진트리에 더미 노드 추가, 포화 이진트리로 만들기. 루트 노드는 그대로 유지
    3. 만들어진 포화 이진트리의 노드들을 가장 왼쪽부터 가장 오른쪽 노드까지, 순서대로 살펴봄.
        노드의 높이는 살펴보는 순서에 무관.
    4. 살펴본 노드가 더미면 문자열 뒤에 0 추가. 아니면 1 추가.
    5. 문자열에 저장된 이진수를 십진수로 변환
    리프노드가 아닌 노드는 자신의 왼쪽 서브트리보다 오른쪽에 있으며, 오른쪽 서브트리보다 왼쪽에 있다고 가정.
    수가 주어졌을 때, 하나의 이진트리로 해당 수를 표현할 수 있는지 알고싶음.
    이진트리로 만들고 싶은 수를 담은 1차원 배열 numbers가 주어짐.
    가능하면 1, 불가하면 0을 배열에 담아 return
    numbers 길이 1~1만, 원소 1~10^15
    """
    def is_possible(b_num):
        b_num = list(map(int, bin(b_num)[2:]))  # 이진수로 바꾸고 리스트에 숫자로 저장
        l_b = len(b_num)  # 현재 길이
        nodes, depth = 1, 0  # 현재 노드 수, 깊이
        while l_b > nodes:  # 이진수 길이보다 크거나 같은 2^n-1중 최소 찾기.
            depth += 1
            nodes = 2 ** depth - 1  # 현재 층수의 포화 이진트리 노드 갯수
        b_num = [0] * (nodes - l_b) + b_num  # 왼쪽에만 0 채워서 포화 이진트리 만들기. 지문엔 없는 규칙.
        l_b += (nodes - l_b)  # 길이 갱신
        if depth == 1 and not b_num[l_b//2]:  # 1층이고 루트노드가 더미면 0
            return 0
        childs = deque([l_b//2])  # 자식노드 기록할 배열
        dif = 2 ** (depth - 2) * 2  # 자식노드와의 인덱스 차이 시작 수치
        for i in range(depth - 1):
            parents = childs.copy()  # 부모 배열 갱신
            childs = deque()  # 자식노드 배열 초기화
            dif //= 2  # 각 층마다 dif는 절반이 된다.
            for p in parents:  # 부모 순회
                if not b_num[p] and (b_num[p - dif] or b_num[p + dif]):
                    return 0  # 부모가 더미고 자식이 더미가 아닌 경우 트리 생성 불가.
                childs.extend([p - dif, p + dif])  # 문제 없으면 자식노드 기록
        return 1  # 문제 없었으면 가능함.
    answer = []
    for num in numbers:
        if is_possible(num):  # 가능하면 1, 아니면 0
            answer.append(1)
        else:
            answer.append(0)
    return answer

inputdatas = [
    [95],
    [4, 58],  # 0, 1
    [7, 42, 5],
    [63, 111, 95]
]

"""
2023 카카오 공채 기출. Lv.3. 현 시점 제출 30명 정답률 14%
50분 첫 제출, 테케 1만 통과.
'주어진 이진트리'를 이진수로 변환하는 과정만 설명되어 있고 '주어진 이진트리'에 대한 조건이 적혀있지 않다.
'주어진 이진트리는 다음과 같습니다'에 나온 트리는 3층이기에 예시 케이스와 맞지 않으므로 트리가 매번 다를 것이다.
트리가 주어지지 않고 숫자가 주어진다. '루트 노드는 그대로 유지합니다'와 '주어진 이진트리'를 연결하면
일단 트리니 루트노드는 있을 것이고, 루트노드는 더미가 아니어야 한다는 것을 알 수 있다.
그런데 포화 이진트리로 만든다는 점에서 일단 depth는 '주어진 이진트리'에서 고정이란 것을 알 수 있다.
그러니 주어진 이진트리가 2층인데 3층까지 더미를 채울 수는 없다. 
그렇게 되면 어떤 이진수든 1 양쪽에 0으로 더미를 채워넣으면 이진트리가 되어버린다.
5-101을 이진트리로 만들 수 없다는 점에서 5에 대해 3층 이진트리가 주어지는건 불가하다는걸 알 수 있다.

예시 케이스와 예제들을 읽으며 내가 생각한 조건은 '주어진 이진트리'에서 더미가 더미의 부모가 되는 경우는 불가하다는 것이었다.
공채 당시에도 그렇게 해석했는데, 그렇게 해석하도록 의도된건지는 확신 못하겠다. 적어도 주어진 그림과 테케들은 그렇게 해석해도 모순이 없다.
하지만 그렇게 해석하고 풀면 테케를 하나밖에 통과 못하므로 다른 가능성 검토.

n층 포화 이진트리는 2^n-1개 노드를 가지므로, 
이진수의 길이보다 크거나 같은 2^n-1 중 
가장 깊이가 얕은 포화이진트리로 검사해야 한다고 가정해볼 수 있다.
작은 숫자들이 더 있다면 조건을 확정할 수 있겠지만 주어진 예시 케이스들로는 조건을 논리적으로 100% 확정할 수는 없다.
심지어 공채 당시와 현재 프로그래머스의 테케가 다르기에, 테케로 조건을 확정해서 푸는 것은 불가능하다.

해당 가정에 맞게 코드를 약간 수정하니 전부 통과.
주어진 숫자를 이진수로 변환한 뒤, 
오른쪽에만 더미 노드를 추가하거나 양쪽에 추가하는건 고려하지 않고,
왼쪽에만 추가한다고 가정하고 풀었다.
이것 또한 주어진 조건과 테스트 케이스로 논리적으로 도출할 수 없는 규칙이다. 

적당히 멍청해서 논리적 비약을 통해 우연히 출제자가 의도한 규칙에 도달하면 쉽게 풀고,
논리적으로 따지고들면 가능성 있는 규칙 조합을 순회하면서 경우의 수마다 풀이를 작성하고, 
통과되는가 확인해야 하니 시간을 엄청나게 낭비하게 되는 지문이라 스트레스 받는다.
"""

for t in inputdatas:
    print(solution(t))
