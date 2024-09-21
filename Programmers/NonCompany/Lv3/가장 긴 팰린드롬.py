# https://school.programmers.co.kr/learn/courses/30/lessons/12904
"""
constraints:
  • 문자열 s의 길이 : 2,500 이하의 자연수
  • 문자열 s는 알파벳 소문자로만 구성
"""


def solution(s):
    def expand(ll, rr):
        max_l = 1
        while 0 <= ll and rr < len_s and s[ll] == s[rr]:
            max_l = rr - ll + 1  # 밖에서 계산하면 범위 벗어난 것도 계산됨
            ll -= 1
            rr += 1
        return max_l
    len_s = len(s)
    arr = []
    for i in range(len_s):
        arr.extend([expand(i, i), expand(i, i + 1)])
    return max(arr)



inputdatas = [
    {"data": ["abcdcba"], "answer": 7},
    {"data": ["abacde"], "answer": 3}
]


"""
연습문제
Lv.3. 현 시점 완료한 사람 7,993명, 정답률 43%
풀고 나서 더 좋은 코드 있나 베스트 풀이들 살펴봤는데 죄다 엉망이다. 
O(n^3)이거나, 코드가 엄청나게 길거나, 코드가 한줄이거나.
한줄도 직관적이고 효율적이면 상관없는데 대부분 더럽고 비효율적이다.
그나마도 시간효율성 통과 못하는 옛날 풀이들이 많다.
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
