# https://school.programmers.co.kr/learn/courses/30/lessons/43163
"""
constraints:
  • 각 단어는 알파벳 소문자로만 이루어져 있습니다.
  • 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
  • words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
  • begin과 target은 같지 않습니다.
  • 변환할 수 없는 경우에는 0를 return 합니다.
"""
from collections import deque

def solution(begin, target, words):
    """
    시작문자가 다를 수 있어서 kmp는 안될듯.
    무식하게 하면
    set(words)에 target 없으면 0
    바꾸지 않은 각 문자에 대해 bfs.
    startswith, endswith로 일치여부 확인.
    """
    if target not in words:
        return 0
    visited = {begin}
    q = deque([(begin, 0)])
    while q:
        cur_word, changed = q.popleft()
        if cur_word == target:
            return changed
        for word in words:
            if word in visited:
                continue
            diff_cnt = sum(a != b for a, b in zip(cur_word, word))
            if diff_cnt == 1:
                visited.add(word)
                q.append((word, changed+1))
    return 0  # 테케에 없지만 문제 로직상 target이 있지만 도달할 수 없는 경우가 있을 수 있음.


inputdatas = [
    {"data": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "answer": 4},
    {"data": ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], "answer": 0}
]


"""
깊이/너비 우선 탐색(DFS/BFS)
Lv.3. 현 시점 완료한 사람 37,330명, 정답률 62%
처음엔 무식하게 pre, post를 슬라이싱해서 startswith, endswith로 비교했다.
이후 다른 글자 수 비교로 개선했다.
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
