# https://leetcode.com/problems/split-message-based-on-limit/
from typing import Optional, List

"""
constraints:
  • 1 <= message.length <= 10^4
  • message consists only of lowercase English letters and ' '.
  • 1 <= limit <= 10^4
"""


class Solution:
    def splitMessage(self, msg: str, limit: int) -> List[str]:
        # 주어진 b로 분할 가능한지 확인
        def can_split(n_b):
            # 모든 </b>의 길이
            tot = n_b * len(f"</{n_b}>")
            # 모든 a의 길이, 모든 메시지 문자 길이
            tot += acc_a + msg_len
            # 분할 가능 여부
            # 마지막 파트는 글자 수 모자라도 상관 없음.
            return tot <= n_b * limit

        msg_len = len(msg)
        n_b = acc_a = 1
        # 분할 가능한 파트 수 찾기
        while not can_split(n_b):
            # <b/b> 자체가 limit 초과.
            # b가 그렇게 커졌으면 당연히 더 커져도 초과임.
            if len(f'<{n_b}/{n_b}>') >= limit:
                return []
            n_b += 1
            # n_b가 늘었으니 마지막 a파트=늘어난 n_b 추가
            # n_b가 1부터 시작이니 <1/1>, <2/2>... <n_b/n_b>까지 <a/b>에서 a파트가 누적됨.
            acc_a += len(f'{n_b}')

        # 분할 수행
        parts = []
        idx = 0
        for i in range(1, n_b + 1):
            suf = f"<{i}/{n_b}>"
            take = limit - len(suf)
            part = msg[idx:idx + take]
            parts.append(f'{part}{suf}')
            idx += take
        return parts



inputdatas = [
    {"data": ["this is really a very awesome message", 9],
     "answer": ["thi<1/14>", "s i<2/14>", "s r<3/14>", "eal<4/14>", "ly <5/14>", "a v<6/14>", "ery<7/14>", " aw<8/14>",
                "eso<9/14>", "me<10/14>", " m<11/14>", "es<12/14>", "sa<13/14>", "ge<14/14>"]},
    {"data": ["short message", 15], "answer": ["short mess<1/2>", "age<2/2>"]},
    {"data": ["abbababbbaaa aabaa a", 8], "answer": ["abb<1/7>","aba<2/7>","bbb<3/7>","aaa<4/7>"," aa<5/7>","baa<6/7>"," a<7/7>"]},
    {"data": ["boxpn", 5], "answer": []},
]

"""
LeetCode Hard.
제출 38.8K, 정답률 42.9%
어렵다. b를 고정하면 좀 쉬워질거라 생각했고 hint에도 그 말이 적혀있지만
b를 고정해도 b가 1~9일 때, 10~99일 때, 100~999일 때, 
1000~9999일 때 변하는 a와 b의 길이를 추적하기 힘들다.
그리고 suffix를 고정해도 파트별로 넣는 문자 갯수를 바꿔야 하는데 이것도 까다롭다.
이진탐색 문제로 나와있지만 무작정 이진탐색 하면 틀린다. 
n_b가 7일 때 성공, 8~9일 때는 실패하지만 11일 때는 성공하는 등
선형성이 b의 단위 수에 따라 달라진다.
이러면 8~9가 실패하니 7을 탐색하지 않게 된다.
이진탐색을 제대로 사용한 유일한 풀이는 n_b 단위수부터 고정하고 진행한다.
이진탐색이라고 주장하는 대다수의 풀이는 사실 while문만 사용하고 포인터도 없으며 선형탐색을 했다.

선형탐색 자체에서도 시간초과할 부분이 많은데, n_b에 대해 쌓여가는 suffix길이 추적, 문자열 배분 등으로
파트를 나눌 수 있는지 확인하면 O(n^2)으로 시간초과가 나온다. early return을 사용해도 마찬가지.
a를 추적하는게 까다로운데, 직관적이지 않다. 본문에서 acc_a는 n_b를 이용해 누적해나가고 있다.
n_b가 늘어나면서 마지막 a파트만 추가되기에 가능한 풀이.

그렇게 해도 시간초과가 남는데, len(f'<{n_b}/{n_b}>') >= limit를 체크해주지 않으면
무의미한 탐색을 계속하기 때문. 
마지막 파트가 limit을 초과하면 정답이 없다는 결론이 나오므로 early return을 해줘야 한다.
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
