# https://school.programmers.co.kr/learn/courses/30/lessons/17686
def solution(files):
    # 파일명은 숫자 공백 마침표 마이너스 부호로만 이루어짐.
    # 영문자로 시작, 숫자 하나 이상 포함.
    # HEAD, NUMBER, TAIL 세 부분.
    # HEAD는 숫자 아님. 최소 한 글자.
    # NUMBER는 1~5글자 숫자. 0~99999 사이 숫자. 00000, 0101 도 가능.
    # TAIL은 나머지. 아무 글자도 없을 수도 있음.
    # 1. HEAD순 사전 순 정렬. 대소문자 구분X.
    # 2. HEAD가 같으면 NUMBER 숫자순. 9 < 10 < 0011 < 012 < 13 < 014. 앞의 0은 무시. 012, 12는 같은 값으로 처리
    # 3. HEAD, NUMBER가 같으면 원래 입력 순서 유지.
    # 중복은 없으나 대소문자, 숫자 앞의 0 차이는 있을 수 있음.
    answer = []
    datas = []
    for idx, file in enumerate(files):  # 3번 조건 위해 idx 사용
        head = num = ''
        st = 0
        leng = len(file)
        while not file[st].isdigit():  # 숫자 무조건 하나 포함이므로 st < leng 필요X
            head += file[st]
            st += 1
        while st < leng and file[st].isdigit():  # tail은 필요없음.
            num += file[st]
            st += 1
        datas.append([head.lower(), int(num), idx])  # head는 대소문자 구분x, num은 앞쪽 0 무시.
    datas.sort()  # 원소 순서대로 알아서 정렬됨.
    for data in datas:  # 정렬된 데이터 받아와서 idx로 원본 저장.
        answer.append(files[data[2]])
    return answer

inputdatas = [
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
]

"""
2018 카카오 공채 기출. Lv.2. 옮겨적기부터 채점까지 16분 소모했다.
더 깔끔한 방법이 있을 것 같아 다른 풀이들을 봤는데 죄다 re를 사용했길래 그냥 넘어갔다.
"""
for t in inputdatas:
    print(solution(t))
