# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""
1 <= time.length <= 6 * 10^4
1 <= time[i] <= 500
"""
from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        # dic = Counter(time)
        # keyli = list(dic.keys())
        # leng, cnt = len(keyli), 0
        # for i in range(leng):
        #     for j in range(i, leng):
        #         if (keyli[i] + keyli[j]) % 60 == 0:
        #             if keyli[i] == keyli[j]:
        #                 cnt += dic[keyli[i]] * (dic[keyli[i]] - 1) // 2
        #             else:
        #                 cnt += dic[keyli[i]] * dic[keyli[j]]
        # return cnt
        cntdic, ans = {}, 0
        """
        for문으로 순회하면 처음 t는 보수가 카운팅 된 적 없으니 0이다.
        나중에 보수가 나타나면 dic에서 발견할 수 있으므로 1쌍이 된다.
        즉, 1쌍이 되었을 때만 ans가 증가하므로, 미리 카운팅하지 않아도 한 번의 순회로 해결할 수 있다.
        """
        for t in time:
            na = t % 60
            ans += cntdic.get(60 - na if na else 0, 0)
            cntdic.setdefault(na, 0)
            cntdic[na] += 1
        return ans

inputdatas = [
    [30,20,150,100,40],
    [60,60,60],
]
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))

"""
LeetCode Medium. 
처음은 Counter와 keys를 사용해서 2중 for문으로 풀었다. 
runtime beats가 7.37%라 다른 풀이를 살펴봤다.
다른 풀이를 보니 시간을 60으로 나눈 나머지만 카운팅하며 보수의 갯수를 곱하는 형식을 취했다.
예를 들면 60으로 나눈 나머지가 20, 40이라면 둘을 합했을 때 60이 되므로 한 쌍이 된다.
나는 dict를 사용하여 디버깅이 편하도록 바꿨다.
"""
