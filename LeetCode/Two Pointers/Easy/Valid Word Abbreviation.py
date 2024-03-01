# https://leetcode.com/problems/valid-word-abbreviation/
from typing import Optional, List
"""
인접하지 않고 비어있지 않은 부분 문자열을 부분 문자열의 길이로 대체할 수 있다.
길이는 0으로 시작하면 안된다.
'substitution'은 다음과 같이 축약될 수 있다.
's10n' (s -ubstitutio- n)
'sub4u4' (sub -stit- u -tion-)
'12' (-substitution-)
'substitution' (no abbreviation)
다음은 유효하지 않다.
's55n' ('s -ubsti- -tutio- n', 대체된 문자열이 인접하다.)
's0ubstitution' (빈 문자열 대체)

문자열과 축약어가 주어졌을 때 해당 축약어로 축약이 가능한지 리턴하라.

constraints:
1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ll = rr = 0
        while ll < len(word) and rr < len(abbr):
            if abbr[rr].isdigit():
                if abbr[rr] == '0':
                    return False
                num = ''
                while rr < len(abbr) and abbr[rr].isdigit():
                    num += abbr[rr]
                    rr += 1
                ll += int(num)
            else:
                if word[ll] != abbr[rr]:
                    return False
                ll += 1
                rr += 1
        return ll == len(word) and rr == len(abbr)

inputdatas = [
    [['internationalization', 'i12iz4n'], True],
    [['apple', 'a2e'], False],
]

"""
LeetCode Easy.
제출 463.9K, 정답률 35.5%
투포인터를 Easy로 분류해놨는데 이게 맞나 싶다. 정답률도 낮다.
abbr에서 숫자와 알파벳을 분리해서 처리하는게 좀 귀찮다.
정규표현식을 사용해도 된다.
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
        print('pass')
    else:
        print('fail\n', f'expected:{answer}\n', f'got:{res}\n')
