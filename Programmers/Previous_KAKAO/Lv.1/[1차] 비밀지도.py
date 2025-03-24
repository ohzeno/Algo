# https://school.programmers.co.kr/learn/courses/30/lessons/17681
"""
constraints:

"""


def solution(n, arr1, arr2):
    return [bin(i|j)[2:].zfill(n).replace('1', '#').replace('0', ' ') for i, j in zip(arr1, arr2)]


inputdatas = [
    {"data": [5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]], "answer": ["#####", "# # #", "### #", "#  ##", "#####"]},
    {"data": [6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]],
     "answer": ["######", "###  #", "##  ##", " #### ", " #####", "### # "]},
]

"""
2018 KAKAO BLIND RECRUITMENT
Lv.1. 현 시점 완료한 사람 38,408명, 정답률 70%
예전엔 14분 넘겼었고, 이번엔 4분 좀 넘겼다.
그냥 내버려둘까 하다가 비트연산을 사용해서 다시 풀었다.
3회차는 처음부터 bit연산 사용했는데 5분 넘겼다.
알고리즘 푼지 오래돼서 그럴수도.
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
