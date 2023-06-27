# https://www.acmicpc.net/problem/3440
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
OR(1): 파이썬 or
AND(&): 파이썬 and
XOR(=): 1이 홀수개 들어올 때 True
동일한 게이트를 두 번 통과하는 사이클은 존재하지 않음.
그림은 다음 문자들로 구성된 최대 200행의 문자열.
" ": 빈 칸. 문자의 위치를 위해 사용됨.
"-": 왼쪽 오른쪽을 연결.
"|": 위 아래를 연결.
"+": 선 연결 혹은 커브. 사방의 문자 연결 가능. 더하기 아래 -가 있으면 연결로 간주하지 않음.
"x": 연결 없이 두 줄 교차. 위-아래, 좌-우를 연결. 두 쌍은 서로 연결되지 않음.
"=": 입력 또는 출력 포트. 좌우 문자 연결. 적어도 한 쪽은 포트임. 왼쪽에 포트는 값 소스. 
    오른쪽 포트는 값 소비자임.
"o": 왼쪽에 게이트, 오른쪽에 포트. 특정 게이트 출력 부정.
"#": 직사각형 게이트. 왼쪽 면은 입력 포트, 오른쪽은 출력 포트 연결 가능. 
    두 게이트는 서로의 측면에 닿지 않음. 인접한 두 #은 동일한 게이트의 일부임.
    크기는 양방향으로 항상 최소 3자. 정확히 한 예외를 제외하고 모든 내부 문자는 비어있음.
    비어있지 않은 단일 문자는 게이트 유형을 나타냄(게이트 영역 외부와 다른 의미를 가질 수 있음).
    "1"("1"), 앰퍼샌드("&"), 등호("=").
이진수: 회로의 입력값. 항상 등호인 오른쪽 문자에 연결됨.
알파벳 대문자: 회로의 명명된 출력. 항상 등호인 왼쪽에 연결을 허용함. 
    각 문자는 최대 한 번 나타나며, 이는 회로 출력의 수가 0~26임을 의미함.
각 그림은 "*"(적어도 하나 이상)으로 구성된 행으로 끝남. 마지막 그림 다음에는 이런 행이 둘 이어짐.
그림을 스캔하고 모든 회로의 출력을 계산하고 알파벳 순으로 출력하라.
각 행은 출력 이름 = 이진값이 출력되어야 한다.
각 테스트 케이스 뒤에 빈 줄을 하나씩 출력하라.
"""
def read_circuit() -> (int, int, list[list[str]]):
    mat, lens = [], []
    h = max_c = 0
    while True:
        row = input()
        if row == '':  # 빈 줄 쓸모없음
            continue
        if row[0] == '*':
            break
        lens.append(len(row))  # 아래에서 len을 어차피 사용해야 하니 미리 저장해둔다.
        max_c = max(max_c, lens[-1])
        h += 1
        mat.append(list(row))
    for i in range(h):
        mat[i] += [' '] * (max_c - lens[i])  # 저장된 길이 사용해서 패딩.
    return h, max_c, mat

def find_type(top: int, bott: int, ll: int, rr: int) -> str:
    for r in range(top + 1, bott):
        for c in range(ll + 1, rr):
            if mat[r][c] != ' ':  # 게이트 안쪽에 종류 문자가 있음.
                return mat[r][c]

def find_boundary(r: int, c: int) -> tuple:
    top = bott = r
    ll = rr = c
    # 게이트 우변에 닿아 시작하므로 rr은 따로 탐색할 필요 없다.
    while top - 1 >= 0 and mat[top - 1][c] == '#':  # 다음이 #인동안 위로
        top -= 1
    while ll - 1 >= 0 and mat[top][ll - 1] == '#':  # 다음이 #인동안 왼쪽으로
        ll -= 1
    while bott + 1 < h and mat[bott + 1][c] == '#':  # 다음이 #인동안 아래로
        bott += 1
    return top, bott, ll, rr

def process(r: int, c: int, dir: int) -> int:
    """
    :param dir: 이동방향.
        -1: 위,
        0: 왼쪽
        1: 아래,
    :return: 연산값
    """
    if mat[r][c] in '01':  # 소스 도달
        return int(mat[r][c])
    elif mat[r][c] in '-=':  # -, = 모두 왼쪽에 더 있음.
        return process(r, c - 1, 0)
    elif mat[r][c] == '|':  # |는 위아래로만 이동 가능
        return process(r + dir, c, dir)
    elif mat[r][c] == 'o':  # o는 negation
        return +(not process(r, c - 1, 0))
    elif mat[r][c] == 'x':  # x는 교차. 가던대로 가면 됨.
        if dir:  # 위아래로 가던 중
            return process(r + dir, c, dir)
        return process(r, c - 1, 0)  # 왼쪽으로 가던 중
    elif mat[r][c] == '#':
        top, bott, ll, rr = find_boundary(r, c)  # 경계 찾기
        gate = find_type(top, bott, ll, rr)  # 게이트 타입 찾기
        in_vals = [
            process(i, ll - 1, 0)  # 포트 입력값
            for i in range(top, bott + 1)  # 게이트 좌변 탐색
            if ll - 1 >= 0 and mat[i][ll - 1] == '='  # 왼쪽에 입력 있으면
        ]
        if gate == '1':  # or 게이트
            out = 1 if any(in_vals) else 0
        elif gate == '&':  # and 게이트
            out = 1 if all(in_vals) else 0
        elif gate == '=':  # xor 게이트
            out = sum(in_vals) % 2  # 홀수면 1(True), 짝수면 0(False)
        for i in range(top, bott+1):  # 연산 끝난 게이트 우변을 연산값으로 바꿈.
            mat[i][c] = str(out)  # 게이트 출력이 여럿이거나 여러 알파벳에 연결될 수 있음.
        return out  # 게이트 출력값
    elif mat[r][c] == '+':  # +는 모든 방향 가능.
        # 왼쪽으로 가다가 위아래로 갈라지는 +는 없기 때문에 전부 elif로 연결한다.
        # 왼쪽이 없는 경우 위아래로만 갈라진다.
        # 그리고 역주행이 아닌 경우 길이 단절되는 케이스는 없으니 조건 걸어줄 필요 없다.
        if c - 1 >= 0 and mat[r][c - 1] not in ' |':  # 길 단절 아니면 왼쪽이 최우선.
            return process(r, c - 1, 0)  # 어느 방향에서 왔어도 왼쪽 가능
        elif dir != 1:  # 아래로 가고있었으면 위로 못감.
            return process(r - 1, c, -1)
        elif dir != -1:  # 위로 가고있었으면 아래로 못감.
            return process(r + 1, c, 1)

def solve() -> None:
    vars = {}
    for r in range(h):
        for c in range(w):
            if 'A' <= mat[r][c] <= 'Z':  # 출력 기록
                vars[mat[r][c]] = process(r, c - 1, 0)
    for var in sorted(vars):  # 알파벳 순으로 출력
        print(f'{var}={vars[var]}')
    print()

while True:
    h, w, mat = read_circuit()
    if not mat:  # *이 두 줄 연속 나오면 mat이 비어있다.
        break
    solve()

"""
현 시점 다이아4. 제출 128, 정답률 17.969%
숏코딩 모든 언어 1위, 맞힌 사람 python 1위.

dfs는 자신있었지만 이 문제는 고생했다.
처음엔 회로를 스캔하며 소스, 게이트(bfs로 경계, 네거티브 출력 기록), 
출력을 모두 기록해두고 게이트의 입력들을 채운 후 게이트 출력을 채우고 
알파벳의 출력을 기록했다.
그 상태에서는 아무리 최적화해도 시간초과가 발생했다.
알파벳에서부터 순회를 하는 방법도 생각했는데, 게이트에 도달한 후
입력값들을 종합하는 과정을 어떻게 할 지 생각나지 않았었다.
위상정렬 태그가 붙어있어서 게이트, 소스, 출력을 그래프로 만들어볼까 생각도 했지만
결국 각 요소들을 찾고 연결하려면 dfs를 돌려야 했다. 
현재는 각 연결 도로는 dfs 한번씩만 돌리므로 
추가로 위상정렬을 사용하면 오히려 시간이 증가할 수도 있다고 생각했다.

코드를 통째로 리팩토링 하여 통과했다.
알파벳에서 출발하여 게이트에 도달하면 상-좌-하로 움직여서 경계값을 구했다.
이전에는 이 아이디어를 생각해내지 못했었다.
또한 게이트의 입력값을 기록할 리스트를 만들어두고 
입력포트마다 dfs를 돌려 값을 종합했다.
이 아이디어도 생각해내지 못했었다.
그리고 xor 연산의 경우 이전에는 매번 ^=를 반복했는데
입력값 합의 홀/짝으로 간단히 해결되는 문제였다.
이것도 생각해내지 못했었다.

이 방법에서는 게이트를 따로 저장해두지 않아서 
연산된 게이트의 출력값을 저장할 방법이 필요했다.
게이트의 출력 라인은 하나지만, 그 라인이 오른쪽으로 가면서 갈라져 
여러 게이트/알파벳에 연결될 수 있기 때문이다.
그러면 거쳐온 라인을 제외한 다른 라인에서도 현재 게이트로 다시 접근할 수 있다는 뜻이다.
그리고 논리회로 이론과는 어긋나는 것 같지만 게이트에 출력이 하나만 있다는 조건이 없다.
dmoj에서도 지적하고 있는 부분인데, 하나의 게이트에 출력 포트가 여럿 있을 수 있다.
이미 처리된 게이트의 우변을 출력값으로 바꿔두면 다른 라인에서 접근했을 때 재연산을 막을 수 있다.

하나 이상한 점은...방문한 게이트의 우변을 전부 출력값으로 바꿔두고,
#=를 만났을 때 #이 방문한 곳이면 에러를 일으키게 제출했더니 에러가 발생했다.
방문한 게이트 우변 #은 전부 전부 출력값으로 바뀌었을 테니 #=문에서 다시 만날 수 없고
방문하지 않은 게이트면 에러가 발생하지 않아야 하는데...

다이아 치고는 테스트 케이스에 대한 정보가 적고, 
조건 설정이 많이 허술한 편이라 원리를 완벽히 해명할 수가 없었다.

그와 별개로 코드 가독성 향상을 위한 리팩토링을 많이 진행했다.
@cache, cache_clear()도 사용해봤지만 같은 위치와 인자로 
process가 호출될 일이 잘 없어서 오히려 느려졌다. 그냥 우변 값 저장만으로 캐싱하는게 빨랐다.
"""