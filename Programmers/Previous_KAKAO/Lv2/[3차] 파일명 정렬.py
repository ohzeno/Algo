# https://school.programmers.co.kr/learn/courses/30/lessons/17686
def solution(files):
    """
    파일명은 영문자, 숫자, 공백, 마침표, 빼기로 이루어져 있다.
    HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
    NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자이다. 앞쪽에 0이 올 수 있다. 0~99999. 00000도 가능.
    TAIL은 나머지 부분이다. 숫자가 있을 수도 있고 아무 글자도 없을 수도 있다.
    1. HEAD 기준으로 사전 순으로 정렬. 대소문자 구분X
    2. HEAD가 같을 경우, NUMBER의 숫자 순으로 정렬. 숫자 앞 0은 무시.
    3. HEAD, NUMBER가 같을 경우, 원래 입력에 주어진 순서를 유지.
    중복된 파일명 없음.
    """
    tmp = []
    for i, f in enumerate(files):  # 3번 조건 위해 idx 사용
        leng = len(f)
        head = number = ''
        p = 0
        while not f[p].isdigit():  # number 무조건 포함이므로 p < leng 필요X
            head += f[p]
            p += 1
        # 5글자 제한. tail 필요없음.
        while len(number) < 5 and p < leng and f[p].isdigit():
            number += f[p]
            p += 1
        tmp.append((head.lower(), int(number), i))
    tmp.sort()
    answer = [files[idx] for h, n, idx in tmp]
    return answer

inputdatas = [
    ["O00321", "O49qcGPHuRLR5FEfoO00321"],
    ['foo9.txt', 'foo010bar020.zip', 'F-15'],
    ['test123456'],
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
]

"""
2018 카카오 공채 기출. Lv.2. 옮겨적기부터 채점까지 16분 소모했다.
더 깔끔한 방법이 있을 것 같아 다른 풀이들을 봤는데 죄다 re를 사용했길래 그냥 넘어갔다.

2차 시도. 괜히 포인터 안쓰고 for문 사용하다가 40분 썼다.
기존 풀이가 더 깔끔하다.
HEAD가 '숫자가 아닌 문자'라고 했는데 공백도 포함된다. 그 것 때문에 한참 헤맸다.
그리고 기존 풀이에서 number의 5글자 제한 조건을 안걸어놨다. 규칙에는 있는데 예외 케이스는 없었나봄. 제한조건 추가하고 list comprehension 추가했다.
여전히 re는 안썼다.
"""
for t in inputdatas:
    print(solution(t))
