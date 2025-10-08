# https://leetcode.com/problems/text-justification/
from typing import Optional, List

from numpy.f2py.crackfortran import word_pattern

"""
constraints:
  • 1 <= words.length <= 300
  • 1 <= words[i].length <= 20
  • words[i] consists of only English letters and symbols.
  • 1 <= maxWidth <= 100
  • words[i].length <= maxWidth
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        i = 0
        n = len(words)
        while i < n:
            line_words = []
            words_len = 0
            while i < n and words_len + len(line_words) + len(words[i]) <= maxWidth:
                line_words.append(words[i])
                words_len += len(words[i])
                i += 1
            # 마지막 라인 혹은 단어가 하나인 경우 왼쪽 정렬
            if i - 1 == n - 1 or len(line_words) == 1:
                justified_line = ' '.join(line_words).ljust(maxWidth)
            else:
                total_space = maxWidth - words_len
                gaps = len(line_words) - 1
                space_per_gap, extra_spaces = divmod(total_space, gaps)
                # 엑스트라 스페이스는 왼쪽부터 채운다
                for j in range(extra_spaces):
                    line_words[j] += ' '
                justified_line = (' ' * space_per_gap).join(line_words)
            answer.append(justified_line)
        return answer


inputdatas = [
    {"data": [["This", "is", "an", "example", "of", "text", "justification."], 16], "answer": [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]},
    {"data": [["What", "must", "be", "acknowledgment", "shall", "be"], 16], "answer": [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]},
    {"data": [
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
         "is", "everything", "else", "we", "do"], 20], "answer": [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]},
    {"data": [["Listen","to","many,","speak","to","a","few."], 6], "answer": [
        "Listen",
        "to    ",
        "many, ",
        "speak ",
        "to   a",
        "few.  ",
    ]}
]

"""
LeetCode Hard.
제출 1.2M, 정답률 49.3%
오랜만에 재밌는 시뮬레이션 문제였다.
문제 이해와 구현에 시간이 좀 걸리지만 Hard까진 아닌듯.
"""
import inspect

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = my_func(sol, *data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
