# https://school.programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    inter = {}  # 교집합용 딕셔너리
    union = {}  # 합집합용 딕셔너리
    strs = [str1, str2]  # 순회용 스트링 리스트
    lengths = [len(str1), len(str2)]  # 순회용 스트링 길이 리스트
    dics = [{}, {}]  # 2글자씩 분리하여 카운팅할 딕셔너리 리스트
    for i in range(2):
        str = strs[i]
        for j in range(lengths[i] - 1):
            # 2글자씩 가져와서 공백제거, 소문자로. 공백은 특수문자로 바꿔 아래에서 걸러지도록.
            tmp = str[j: j+2].replace(' ', '+').lower()
            if not tmp.isalpha():  # 알파벳만 모여있지 않으면 다음으로
                continue
            else:  # 알파벳만 있으면
                if tmp in dics[i]:  # 딕셔너리에 있으면 개수 추가
                    dics[i][tmp] += 1
                else:  # 없으면 신규등록
                    dics[i][tmp] = 1
    if len(dics[0]) == 0 and len(dics[1]) == 0:  # 둘 다 공집합이면 자카드 유사도 1
        return 65536

    for part in dics[0]:
        if part in dics[1]:  # A집합 원소가 B에도 있으면
            inter[part] = min(dics[0][part], dics[1][part])  # 적은 쪽을 교집합으로
            union[part] = max(dics[0][part], dics[1][part])  # 많은 쪽을 합집합으로
        else:  # B에 없으면 합집합에만 등록
            union[part] = dics[0][part]
    for part in dics[1]:  # B집합에서 A집합에 없는 원소 합집합에 추가
        if part not in union:
            union[part] = dics[1][part]
    len_inter = 0
    len_uni = 0
    # 교집합 원소 수, 합집합 원소 수 카운팅
    for data in inter:
        len_inter += inter[data]
    for data in union:
        len_uni += union[data]
    # 자카드 유사도 * 65535해서 정수부만 반환.
    return int(65536 * (len_inter/len_uni))

inputdatas = [
    ['FRANCE', 'french'],
    ['handshake', 'shake hands'],
    ['aa1+aa2', 'AAAA12'],
    ['E=M*C^2', 'e=m*c^2']
]

"""
2018 카카오 공채 기출. 35분 걸렸다. 예외 케이스들을 찾는 데에 시간이 좀 걸렸다.
문제 조건들을 한 번에 다 적용시키지 못하고 있다.
중복 허용 다중 집합때문에 set를 적용하지 않았는데 베스트 답변에선 set를 사용했다.
하지만 결국 set의 원소들을 다시 2글자 집합에서 일일이 카운팅해주며 시간낭비가 생긴다.
베스트 답변은 re, findall 등 자주 사용하지 않는 함수들을 사용했지만
아직 그런걸 연습할 단계가 아니라 생각하여 넘어간다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
