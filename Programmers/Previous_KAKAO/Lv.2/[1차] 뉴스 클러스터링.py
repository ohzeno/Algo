# https://school.programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    """
    J(A, B)는 두 집합의 교집합 크기를 합집합 크기로 나눈 값.
    둘 모두 공집합인 경우 J(A, B) = 1
    중복 허용하는 집합에 대해서도 정의 가능.
    문자열 ABC라면 AB, BC로 두 글자 씩 끊어서 다중집합 만들 것.
    영문자로 된 글자 쌍만 유효. 대문자, 소문자는 같은 원소로 취급.
    자카드 유사도 계산 후 65536을 곱하고 정수부만 출력
    """
    strs = [str1.lower(), str2.lower()]  # 순회용 스트링
    lengs = [len(str1), len(str2)]  # 스트링 길이
    sets = [set(), set()]  # 집합
    dics = [{}, {}]  # 딕셔너리
    for i in range(2):
        for j in range(lengs[i] - 1):
            tmp = strs[i][j:j + 2]
            if tmp.isalpha():  # 영문자로 된 글자 쌍만 유효
                sets[i].add(tmp)  # 집합에 추가
                dics[i].setdefault(tmp, 0)
                dics[i][tmp] += 1  # 딕셔너리에 추가
    if not sets[0] and not sets[1]:  # 둘 다 공집합이면 자카드 유사도 1
        return 65536
    inter = sets[0] & sets[1]
    union = sets[0] | sets[1]
    inter_sum = union_sum = 0  # 교집합 원소 수, 합집합 원소 수
    for i in inter:  # 적은 쪽을 교집합으로
        inter_sum += min(dics[0][i], dics[1][i])
    for j in union:  # 많은 쪽을 합집합으로
        union_sum += max(dics[0].get(j, 0), dics[1].get(j, 0))
    return int(inter_sum / union_sum * 65536)  # 자카드 유사도 * 65535해서 정수부만 반환.

inputdatas = [
    ["FRANCE", "french"],
    ["handshake", "shake hands"],
    ["aa1+aa2", "AAAA12"],
    ["E=M*C^2", "e=m*c^2"]
]

"""
2018 카카오 공채 기출. Lv.2. 35분 걸렸다. 예외 케이스들을 찾는 데에 시간이 좀 걸렸다.
문제 조건들을 한 번에 다 적용시키지 못하고 있다.
중복 허용 다중 집합때문에 set를 적용하지 않았는데 베스트 답변에선 set를 사용했다.
하지만 결국 set의 원소들을 다시 2글자 집합에서 일일이 카운팅해주며 시간낭비가 생긴다.
베스트 답변은 re, findall 등 자주 사용하지 않는 함수들을 사용했지만
아직 그런걸 연습할 단계가 아니라 생각하여 넘어간다.

2차시도.
이전보다 훨씬 간결하게 만들었다. get에 default값 설정이 있다는걸 몰라서 시간을 좀 썼다.
25분 소모. 여전히 re, findall을 연습할 단계가 아니라 생각한다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
