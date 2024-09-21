# https://school.programmers.co.kr/learn/courses/30/lessons/140108
"""
- 첫 글자 x
- 왼쪽에서부터 읽어나가며 x, x가 아닌 글자가 나온 횟수를 센다.
  처음으로 두 횟수가 같아지는 순간 지금까지 읽은 문자열을 분리한다.
- 남은 부분이 없을 때까지 이를 반복한다.
- 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없으면, 역시 지금까지 읽은 문자열을 분리한다.
분해한 문자열 개수를 return하라.
"""

def solution(s):
    ans = 0
    cnt = 0
    x = ''
    for c in s:
        if not x:
            x = c
        cnt += 1 if c == x else -1
        if cnt == 0:
            ans += 1
            x = ''
    return ans + 1 if cnt else ans


inputdatas = [
    {"data": ["banana"], "answer": 3},
    {"data": ["abracadabra"], "answer": 6},
    {"data": ["aaabbaccccabba"], "answer": 3},
]

"""
연습문제
Lv.1. 현 시점 완료한 사람 15,401명, 정답률 57%
레벨 1치고는 상당히 어렵다. 물론, 시간제약을 생각하지 않고 무식하게 리스트로 풀면 쉬운데
인덱싱 사용하면 생각보다 까다로웠다.
풀이가 더러워서 for문으로 개선했다.
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
