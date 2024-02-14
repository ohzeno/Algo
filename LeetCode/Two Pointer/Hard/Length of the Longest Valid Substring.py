# https://leetcode.com/problems/length-of-the-longest-valid-substring/
from typing import Optional, List

"""
word의 모든 부분문자열이 forbidden에 포함되지 않으면 유효하다고 한다.
word에서 가장 긴 유효한 부분문자열의 길이를 리턴하라.
부분 문자열은 연속된 문자열이며, 비어있을 수 있다.

constraints:
1 <= word.length <= 10^5
word consists only of lowercase English letters.
1 <= forbidden.length <= 10^5
1 <= forbidden[i].length <= 10
forbidden[i] consists only of lowercase English letters.
"""


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        fsizes = sorted(set(len(f) for f in forbidden))
        longest = ll = 0
        for rr in range(1, len(word)+1):  # 우포인터 움직이며 탐색
            for sz in fsizes:
                if rr - ll < sz:  # 최대 탐색 범위가 금지단어보다 짧으면 우포인터 이동
                    # sz는 오름차순이니 작은 것보다 작으면 더 큰 사이즈보다 당연히 작음.
                    break
                if word[rr-sz:rr] in forbidden:  # 금지단어가 있으면 좌포인터 이동
                    ll = rr - sz + 1
            longest = max(longest, rr - ll)
        return longest


inputdatas = [
    [["cbaaaabc", ["aaa", "cb"]], 4],
    [["leetcode", ["de", "le", "e"]], 4],
    [["aaaaaaaaaaaaaaa", ["bc"]], 15],
    [["aaaabaaacc", ["bcca", "aaa", "aabaa", "baaac"]], 4],
    [["acb", ["acb","caccc","baaab","baa"]], 2],
]

"""
LeetCode Hard.
제출 46K, 정답률 35.1%
투 포인터와 슬라이딩 윈도우 응용.
개인적으로 어려웠다.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
# for t in inputdatas:
#     print(my_func(*t))
for data, answer in inputdatas:
    res = my_func(*data)
    if res == answer:
        print("pass")
    else:
        print("fail\n", f"expected:{answer}\n", f"got:{res}\n")
