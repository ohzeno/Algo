# https://school.programmers.co.kr/learn/courses/30/lessons/12977
"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 갯수를 리턴.
3 <= len(nums) <= 50
1 <= nums[i] <= 1000
중복 없음
"""
from itertools import combinations


def solution(nums):
    def is_prime(n):
        if n in is_prime_d:
            return is_prime_d[n]
        for i in range(2, int(n**0.5) + 1):
            if not n % i:
                is_prime_d[n] = False
                return False
        is_prime_d[n] = True
        return True

    is_prime_d = {0: False, 1: False}
    cnt = 0
    for case in combinations(nums, 3):
        if is_prime(sum(case)):
            cnt += 1
    return cnt


inputdatas = [
    [1, 2, 3, 4],
    [1, 2, 7, 6, 4],
]

"""
Summer/Winter Coding(~2018) 기출. 
Lv.1. 현 시점 완료한 사람 31,704명, 정답률 61%
처음에는 3개를 더해야하니 이걸 어떻게 체크해야 했는데
조건을 보니 nums가 길지 않아서 combinations를 사용할 생각을 했다.
7분 걸려서 최적화 풀이를 만들었다. 그런데 굳이 최적화가 필요없는 문제였다.
nums의 원소가 1000까지라 소수판별을 매번 하면 느릴 것 같아서 
딕셔너리에 판별 결과를 저장했다.
프로그래머스는 @cache를 사용할 수 없어서 딕셔너리를 사용했다.
set를 사용할까 생각도 했는데 
소수 set와 소수가 아닌 set를 따로 두면 별 차이가 없을거라 딕셔너리를 썼다.
사실 효율성 테스트가 없기도 하고 직접 제출해보니 캐싱 없어도 통과되긴 한다.
"""

for t in inputdatas:
    print(solution(t))
