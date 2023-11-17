# https://leetcode.com/problems/bulls-and-cows/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        # sdic, gdic = {}, {}
        # for s, g in zip(secret, guess):
        #     if s == g:
        #         bulls += 1
        #     else:
        #         sdic[s] = sdic.get(s, 0) + 1
        #         gdic[g] = gdic.get(g, 0) + 1
        # for k in sdic:
        #     cows += min(sdic[k], gdic.get(k, 0))
        # return f"{bulls}A{cows}B"
        digits = {str(i): 0 for i in range(10)}  # get을 매번 사용하니 runtime이 느린 듯 해서 미리 키값 만들어둠.
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                """
                s값이 음수면 guess에서 나온 적 있다는 뜻. g값이 양수면 secret에서 나온 적 있다는 뜻.
                int로 인해 괄호 안의 조건이 참이면 1이 더해진다.
                digits[g]가 양수라면 cows에 이미 1이 더해졌기에 사용했다는 의미로 -1을 해주는 것이 된다.
                digits[s]가 음수인 경우도 이미 cows에 반영되었기에 +1을 해서 g의 숫자를 하나 이미 사용했다는 뜻이 된다.
                """
                cows += int(digits[s] < 0) + int(digits[g] > 0)
                digits[s] += 1  # secret의 숫자는 +1
                digits[g] -= 1  # guess의 숫자는 -1
        return f"{bulls}A{cows}B"

inputdatas = [
    ["1807", "7810"],
    ["1123", "0111"],
    ["0765860239", "5736153483"],
]

"""
LeetCode Medium.
20분쯤 썼다. 어려워서 20분을 쓴건 아니다.
무식한 풀이 방법은 바로 떠오르는데, 그걸 더 깔끔하게 만들 수 없을까 생각하다가 20분을 썼다.
초기 풀이는 한 번의 순회로 끝냈지만 코드가 더러웠다.
그래서 두 번의 순회를 사용하며 훨씬 깔끔한 풀이를 만들었다.
이후 시간을 더 들여서 한 번의 순회로 해결하는 코드를 만들었다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t[0], t[1]))
