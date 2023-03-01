# https://www.acmicpc.net/problem/7568
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
몸무게 x, 키 y라면 덩치는 (x, y)로 표현.
a가 b보다 몸무게와 키 모두 크다면 a는 b보다 덩치가 크다.
n명 집단에서 각 사람의 덩치 등수는 자신보다 더 큰 덩치의 사람 수로 정해진다.
학생 n명의 몸무게, 키가 주어졌을 때 각 사람의 덩치 등수를 계산하여 출력하라.
"""

n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]
ans = []
for p1 in datas:
    count = 0
    for p2 in datas:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            count += 1
    ans.append(count + 1)
print(*ans)


"""
현 시점 실버5. 제출 84102, 정답률 55.819%
처음엔 딕셔너리에 순서대로 데이터를 기록하고, 
sort로 정렬한 리스트에서 해당 인원의 데이터가 나오기 전까지
순회하며 비교하여 count를 계산할까 했다. 
하지만 n이 최대 50이라 n^2은 감당 가능할지도 모르기에 일단 브루트포스로 풀어보았고, 통과했다.
"""