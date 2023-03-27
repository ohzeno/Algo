# https://www.acmicpc.net/problem/1003
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
주어진 피보나치 함수에서 0과 1이 각각 몇 번 호출되는지 구하는 프로그램을 작성하시오.
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
"""
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        print(f'{a} {b}')


"""
현 시점 실버3. 제출 184584, 정답률 32.216%
dp로 각 항을 기록하는 리스트를 만들려고 했는데, 더 쉬운 방법이 있어서 이용했다.
"""