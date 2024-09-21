# https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""
"""

def solution(nums):
    half = len(nums) // 2
    cnt_of_type = len(set(nums))
    return min(cnt_of_type, half)


inputdatas = [
    {"data": [[3,1,2,3]], "answer": 2},
    {"data": [[3,3,3,2,2,4]], "answer": 3},
    {"data": [[3,3,3,2,2,2]], "answer": 2},
]

"""
해시
Lv.1. 현 시점 완료한 사람 52,053명, 정답률 65%
아침에 일어나자 마자 풀었는데, 졸려서 머리가 안돌아간다.
카운터로 딕셔너리를 만들고 키값 길이와 half에 따라 
답이 어떻게 되는지 머릿속에서 찾느라 시간이 좀 걸렸다.
물론 종류 수와 half를 비교해야 한다는 부분은 바로 떠올렸다.
cnt_of_type과 half의 대소에 따른 정답 조건을 찾는데 1분 넘게 쓴 것.

풀고 보니 카운터 value는 필요없어서 그냥 set를 쓰면 됐고,
조건식은 min으로 해결되는 문제였다.
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
