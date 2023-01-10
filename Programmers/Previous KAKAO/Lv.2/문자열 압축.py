# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    """
    ababc면 2글자 단위 2abc로 압축 가능
    abcabcded면 3글자 2abcded로
    이런식으로 1개 이상 단위로 압축해서 가장 짧은 것 길이를 return
    """
    min_len = len(s)
    for unit in range(len(s)//2, 0, -1):  # 큰 단위부터
        tmp_s = s  # 임시 문자열
        i = 0
        while i < len(tmp_s) - 2 * unit + 1:  # 유닛단위 2개 남은 시점까지만 테스트. 2개 없으면 압축도 없으니
            pre = tmp_s[i:i + unit]  # 앞쪽 문자열
            count = 1  # 문자열 반복 횟수
            for j in range(i + unit, len(tmp_s) - unit + 1, unit):  # pre 다음부터 유닛단위로 체크
                if pre != tmp_s[j:j + unit]:  # 다른 문자열 나오면 중단
                    break
                count += 1  # 같은 문자열이면 횟수 증가
            if count > 1:  # 중복 문자열 있으면
                tmp_s = tmp_s.replace(pre * count, f'{count}{pre}', 1)  # 첫 반복 문자열 묶음만 교체
                i += len(str(count)) + len(pre)  # 교체된 문자열 다음으로
            else:
                i += unit  # 다음 유닛으로
        if len(tmp_s) < min_len:  # 최소 길이 갱신
            min_len = len(tmp_s)
    return min_len  # 최소 길이 리턴

inputdatas = [
    'aababa',  # 5
    'xxxxxxxxxxyyy',  # 5
    'aaaaaaaaaabbbbbbbbbb',  # 6
    'aaaaa',  # 2
    'aaaaaaaaaa',  # 3
    'werwerwsdgsdfsdfsdf',  # 15
    "aabbaccc",  # 7
    "ababcdcdababcdcd",  # 9
    "abcabcdede",  # 8
    "abcabcabcabcdededededede",  # 14
    "xababcdcdababcdcd"  # 17
]

"""
2020 카카오 공채 기출. Lv.2. 현 시점 25704명 제출, 정답률 41%
43분 첫 제출. 52점.
조건에 '제일 앞부터 정해진 길이만큼 잘라야 한다'가 없지만, 입출력 예시 5번에서 해당 조건을 언급한다.
47분 개선 후 제출. 60점.
'제일 앞부터 정해진 길이만큼 잘라야 한다'가 단축된 부분 제외하고도 길이단위로 슬라이딩 하며 살펴야 한다.
abab acd efef라면 중간 acd가 3이라 단축X 2ab ac de fe f로 살펴야한다.
51분 개선 후 제출. 82점.
aa bc bc라면 aa2bc가 되어야 하는데, 첫 aa가 단축이 불가하면 검사를 중단했었다.
67분 개선 후 제출. 통과.

조건 설명이 부족하여 이해가 힘든 문제였다. 
lv.2지만 문제 이해 못하면 이 문제에 1시간 이상 쓰고 결국 못풀고 코테 망할듯.
나는 혹시 모를 시간초과를 고려하여 index를 사용하여 문자열에 접근하며 실시간으로 문자열을 갱신했다.
다른 풀이들을 보니 매 unit마다 unit단위로 단어를 분할한 리스트를 순회하며 작업했다.
분할해놓으면 디버깅이 편하다는 것 외에 딱히 장점이 없을 듯 하여 풀이를 시도해보진 않았다.
"""

for t in inputdatas:
    print(solution(t))
