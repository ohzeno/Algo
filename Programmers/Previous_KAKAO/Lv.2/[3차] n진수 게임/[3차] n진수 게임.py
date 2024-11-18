# https://school.programmers.co.kr/learn/courses/30/lessons/17687
"""
constraints:

"""


def solution(n, t, m, p):
    # n진법. 본인이 말할 t개 숫자 구해서 리턴. m명 참가. 본인 순서 p
    total = '0'
    hex_str = 'ABCDEF'
    for q in range(1, m * (t - 1) + p + 1):
        tmp = ''
        while q:
            q, r = divmod(q, n)
            tmp += hex_str[r - 10] if n > 10 and r >= 10 else str(r)
        total += tmp[::-1]
    return ''.join(total[p - 1:m * (t - 1) + p:m])


inputdatas = [
    {"data": [2, 4, 2, 1], "answer": "0111"},
    {"data": [16, 16, 2, 1], "answer": "02468ACE11111111"},
    {"data": [16, 16, 2, 2], "answer": "13579BDF01234567"}
]

"""
2018 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 13,696명, 정답률 61%
이전엔 31분 걸렸는데 이번엔 17분 걸렸다. 진법 변환 로직이 기억나지 않아 시간이 걸렸다.
"""

for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
