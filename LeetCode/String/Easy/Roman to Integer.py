# https://leetcode.com/problems/roman-to-integer/
"""
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        symb = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        # res, leng = 0, len(s)
        # for i in range(leng):
        #     if i > 0 and symb[s[i]] > symb[s[i-1]]:
        #         res += symb[s[i]] - symb[s[i-1]]
        #     elif i < leng - 1 and symb[s[i]] < symb[s[i+1]]:
        #         continue
        #     else:
        #         res += symb[s[i]]
        # return res
        s = s.replace("IV", "IIII").replace("IX", "VIIII") \
            .replace("XL", "XXXX").replace("XC", "LXXXX") \
            .replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(symb.get, s))


inputdatas = [
    "III",
    "LVIII",
    "MCMXCIV",
]

"""
LeetCode Easy. 처음엔 10분이나 써서 for문으로 풀었다. 다른 풀이를 보다보니 while을 사용할 수도 있다.
베스트 풀이를 보니, replace를 사용했다.
백준과 swea에서 비슷한 문제를 replace로 풀었었는데 오래돼서 감이 떨어졌다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))