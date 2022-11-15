# https://school.programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    # 규칙에 맞지 않은 케이스는
    # 비슷하고 규칙에 맞는 아이디를 추천해주기
    # 길이는 3~15자.
    # 알파벳 소문자, 숫자, -, _, .만 사용할 수 있음.
    # 마침표는 처음과 끝에 사용X, 연속 사용X
    # print(ord('a'))  # 97
    # print(ord('z'))  # 122
    allowed = [chr(i) for i in range(97, 123)]
    allowed += [str(i) for i in range(10)]
    allowed += ['-', '_', '.']
    # 1. 소문자로 변경
    new_id = new_id.lower()
    # 2. 규정 문자 외 제거
    for s in set(new_id):
        if not s in allowed:
            new_id = new_id.replace(s, '')
    # 3. 마침표 둘 이상인 부분 마침표 하나로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4. 마침표가 처음이나 끝이라면 제거
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5. 빈 문자열이면 a로 변경
    if not new_id:
        new_id = 'a'
    # 6. 16자 이상이면 첫 15개만 남김. 제거 후 마침표가 끝에 위치하면 제거
    elif len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7. 길이가 2자 이하면 마지막 문자를 연장
    leng = len(new_id)
    if leng < 3:
        new_id += new_id[-1] * (3 - leng)
    return new_id

inputdatas = [
    "...!@BaT#*..y.abcdefghijklm",
    "z-+.^.",
    "=.=",
    "123_.def",
    "abcdefghijklmn.p",
]

"""
2021 카카오 공채 기출. Lv.1. 옮겨적기부터 채점까지 20분 걸렸다.
모범 답안을 보니 정규식을 사용한 경우도 있고, 나와 유사하게 풀이한 경우도 있다.
후자는 allowed 대신 s.isalpha()와 s.isdigit()을 사용한 부분이 참고할 만했다.
"""
for t in inputdatas:
    print(solution(t))
