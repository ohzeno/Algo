# https://www.acmicpc.net/problem/1019
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
지민이는 전체 페이지의 수가 N인 책이 하나 있다. 첫 페이지는 1 페이지이고, 마지막 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.
1 ≤ N ≤ 1e9
0~9까지의 숫자가 몇 번 나오는지 공백으로 구분하여 출력한다.
"""


def count_digits(n):
    cnts = [0] * 10
    factor = 1
    # ex) n=12345, factor=100, left=12, cur=3, right=45
    while factor <= n:  # 각 반복에서 factor의 자리 수 숫자만 집계한다.
        right = n % factor  # 현재 자리수 오른쪽 ex) 12345 -> 45
        cur = (n // factor) % 10  # 현재 자리수 ex) 12345 -> 3
        left = n // (factor * 10)  # 현재 자리수 왼쪽 ex) 12345 -> 12
        """
        step 1. left가 0보다 클 경우, 새로 생겨난 factor 자리 숫자 집계
        
        def I(left, cur, right):
            # 엄밀한 함수는 아니니 대충 예시와 비교하며 파악하길 바란다.
            return int(f'{max(left, 0)}
                         {max(cur, 0)}
                         {max(right, 0)}')라고 두면
        
        left가 0보다 클 경우
        I(0*len(left), 0, 0) ~ 
        I(left-1, 9, 9*len(right))의 factor 자리 숫자가 추가된다.
        ex) 00000~11999의 100의 자리 수 집계.
        이는 00000~00999를 한 세트로, 11000~11999까지 left세트 존재한다.
        각 세트에서 0~9 각 숫자는 factor번 등장한다. 00100~00199: 100의 자리 1 100번
        0의 경우는 00000~00999의 첫 세트에서 00000~00099 부분인데, 
        백의 자리 0은 실제로는 존재하지 않으므로 첫 세트를 제외한 left-1세트로 집계한다.
        """
        if left > 0:
            cnts[0] += (left - 1) * factor
            for i in range(1, 10):
                cnts[i] += left * factor
        """
        step 2. cur가 1 이상일 경우, cur 이전 단위까지의 수 집계
        cur가 1 이상일 경우
        I(left, 0, 0*len(right)) ~
        I(left, cur-1, 9*len(right))의 factor 자리 숫자가 추가된다.
        ex) 12000~12299의 100의 자리 수 집계
        12000~12099 100의 자리 0 factor번
        ~12200~12299 100의 자리 2 factor번
        """
        # left가 0이면 00000~00099는 백의 자리 수가 존재하지 않음.
        numbers = range(cur) if left > 0 else range(1, cur)
        for i in numbers:
            cnts[i] += factor
        """
        step 3. int(f'{left}{cur}') * factor부터 n까지의 cur 집계
        ex) 12300~12345의 백의 자리 수 처리.
        이는 12399까지 가지 않으니 따로 처리해주는 것.
        right가 45이나, 12300을 포함해야하므로 +1
        """
        cnts[cur] += right + 1
        factor *= 10  # 다음 자리수로 이동
    return cnts


n = int(input())
print(*count_digits(n))


"""
현 시점 플래 5. 제출 18232. 정답률 42.742 %
쉬워보이는데 엄청 애먹었다. 2일동안 이 문제만 붙들고 있었다.
정답률이 높은 이유는 블로그 풀이가 있기 때문.
내 풀이는 블로그 풀이가 아니다.
좀 조잡할 수 있지만 예제를 곁들여 주석을 자세하게 적어놨으니 
나중에 봐도 이해할 수 있을 거라고 생각한다.
"""
