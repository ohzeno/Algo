# https://leetcode.com/problems/subarray-sums-divisible-by-k/
from typing import Optional, List
"""
constraints:
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
2 <= k <= 10^4
"""
from itertools import accumulate
from collections import Counter
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # # remains = {0: 1}
        # remains = [1] + [0] * (k-1)
        # acc = cnt = 0
        # for num in nums:
        #     acc = (acc + num) % k
        #     cnt += remains[acc]
        #     # cnt += remains.get(acc, 0)
        #     # remains.setdefault(acc, 0)
        #     remains[acc] += 1
        # return cnt
        prefixSum = accumulate(nums, initial=0)
        remains = Counter(map(lambda x: x%k, prefixSum))
        caseCnt = map(lambda v: v*(v-1)//2, remains.values())
        return sum(caseCnt)

inputdatas = [
    [[4,5,0,-2,-3,1], 5],
    [[5], 9],
    [[0, 0, 0], 2],
    [[4, 4, 4], 4]
]

"""
LeetCode Medium.
Medium답지 않게 어려운 문제.
prefix sum으로 sum연산을 최적화하더라도
O(n^2)의 시간복잡도를 가지는데, 그러면 시간초과가 발생한다.

수학적 접근으로 풀어야 한다.
prefixSum[i] = A*k + Ri라고 표현하면
perfixSum[j] = B*k + Rj라고 표현할 수 있다.
subarray(i+1~j)의 합은 prefixSum[j] - prefixSum[i]이므로
prefixSum[j] - prefixSum[i] = (B-A)*k + (Rj-Ri)이다.

k로 나누어떨어지려면 (Rj - Ri) = C * k여야 한다.
0 <= Ri, Rj <= k - 1이므로
C*k는 k 이상이 될 수 없다. 따라서 C는 0이다.
즉, Ri = Rj이어야 한다.
-----------------------------------------------------------------
Editorial이나 Solutions의 일반적인 풀이는 for문과 remains 딕셔너리나 배열을 사용한다.
for문 내에서 acc는 항상 Rj이며
remains[acc]는 이전까지 Rj가 나온 횟수이므로 Ri=Rj인 경우의 수가 된다.
그래서 cnt에 더해준 후 현재 케이스를 +1 해서 Rj가 나온 횟수를 업데이트 해준다.

remains[0] = 1로 초기화해주는 이유는
subarray(i+1~j)의 합은 prefixSum[j] - prefixSum[i]이므로
prefixSum[j] - prefixSum[i] = (B-A)*k + (Rj-Ri)이다.
Ri = Rj
이 과정에서 i+1~j만 고려했기 때문이다. i~j를 고려해야 한다.
하지만 i번째 원소를 포함하려면 prefixSum[j] - prefixSum[i-1]을 해야 하는데
i가 0일 경우 i-1때문에 두번째 항이 prefixSum[-1]이 되어버린다.
따라서 prefixSum을 [0] + nums로 초기화해주면 
prefixSum[j] - prefixSum[i-1]을 고려할 수 있게 된다.

nums를 순회하며 Ri가 0인 첫 케이스에서 remains[0]이 0이면 cnt에 횟수를 더할 수 없기 때문이다.
Ri가 0인 두 번째 케이스에서 2를 더해주게 되는데,
[0, 0, 0]을 생각해보면
첫 0에서 (0)밖에 없으니 1이 더해지고         cnt += 1, remains[0] = 1 -> 2
두 번째 0에서 (0, 1), (1) +2             cnt += 2, remains[0] = 2 -> 3
세 번째 0에서 (0, 2), (1, 2), (2) +3    cnt += 3, remains[0] = 3 -> 4
이런 식으로 케이스가 모두 고려된다.

이런 과정때문에 솔루션이 저렇게 되긴 하는데
Ri = Rj를 도출하는 과정까지 도달하는 것도 비현실적이고, 
remains[0] = 1을 해야 하는 이유를 제대로 이해하고 더해주는 사람도 없을 것이다.
릿코드 댓글들의 반응도 나와 같지만
짧은 인터뷰나 코테에서 이걸 푸는 사람이 있을까?
심지어 Editorial에서는 remains[0] = 1을 해야 하는 이유를 설명하지 않고 있다.
-----------------------------------------------------------------
Ri = Rj이어야 하므로 R별 갯수를 구하고, 조합을 사용하면 된다.

itertools.accumulate를 처음 써봤는데 상당히 유용하다.
아이디어는 내가 생각해냈지만 initial=0은 위 내용에서 알게됐다.
initial=0을 해준 이유는 위의 내용과 같다.
caseCnt의 values가 각 나머지가 출현한 횟수인데
그 중에서 2개를 뽑으면 subarray의 시작과 끝이 정해진다.
고로 vC2 = v! / ((v-2)! * 2!) = v*(v-1)/2가 된다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(*t))
