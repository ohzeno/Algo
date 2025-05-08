# https://leetcode.com/problems/integer-to-english-words/
from typing import Optional, List

"""
constraints:
  • 0 <= num <= 2^31 - 1
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one(num):
            switcher = {
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine"
            }
            return switcher[num]

        def two_less_20(num):
            switcher = {
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen"
            }
            return switcher[num]

        def ten(num):
            switcher = {
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety"
            }
            return switcher[num]

        def three(num):
            hundred = None
            if num >= 100:
                hundred = one(num // 100) + " Hundred"
            ten_num = num % 100
            if ten_num == 0:
                ten_str = None
            elif ten_num < 10:
                ten_str = one(ten_num)
            elif ten_num < 20:
                ten_str = two_less_20(ten_num)
            else:
                ten_str = ten(ten_num // 10)
                if ten_num % 10 != 0:
                    ten_str += ' ' + one(ten_num % 10)
            if hundred and ten_str:
                return hundred + ' ' + ten_str
            elif hundred:
                return hundred
            else:
                return ten_str

        billion = num // (10 ** 9)
        million = (num // (10 ** 6)) % (10 ** 3)
        thousand = (num // (10 ** 3)) % (10 ** 3)
        hundred = num % (10 ** 3)
        res = ""
        if billion:
            res += three(billion) + " Billion"
        if million:
            if res:
                res += " "
            res += three(million) + " Million"
        if thousand:
            if res:
                res += " "
            res += three(thousand) + " Thousand"
        if hundred:
            if res:
                res += " "
            res += three(hundred)
        return res.strip()


inputdatas = [
    {"data": [123], "answer": "One Hundred Twenty Three"},
    {"data": [12345], "answer": "Twelve Thousand Three Hundred Forty Five"},
    {"data": [1234567], "answer": "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"},
    {"data": [100], "answer": "One Hundred"},
]

"""
LeetCode Hard.
제출 1.6M, 정답률 34.3%
노가다 구현 문제. 
실행 결과 제대로 안보여주는 프로그래머스 코테에선 엣지케이스 처리할 시간 없어서 틀릴듯.
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
