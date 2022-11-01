# https://school.programmers.co.kr/learn/courses/30/lessons/67258
from heapq import heappush
def solution(gems):
    # 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
    # 가장 짧은 구간이 여럿이면 시작 진열대 번호가 가장 작은 구간 리턴.
    # gems 배열 10만 이하
    # 첫 gem은 1번 진열대.
    # gems 원소는 1~10 길이의 알파벳 대문자.
    display = {}
    for i, gem in enumerate(gems):
        if gem in display:
            heappush(display[gem], i)
        else:
            display[gem] = [i]

    def bsearch(ll, hh, data):
        if data[0] > hh or data[-1] < ll:
            return False
        start = 0
        end = len(data) - 1
        while start <= end:
            mid = (start + end) // 2
            if ll <= data[mid] <= hh:
                return True
            elif data[mid] < ll:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def check(i, j):
        for gem in display:
            if not bsearch(i, j, display[gem]):
                return False
        else:
            return True

    ans = {}
    num_type = len(display)
    max_len = len(gems)
    shortest = max_len
    for i in range(max_len - num_type + 1):
        for j in range(max_len - 1, i - 1, -1):
            if num_type - 1 <= j - i <= shortest:
                if check(i, j):
                    shortest = j - i
                    if j - i in ans:
                        heappush(ans[j - i], [i + 1, j + 1])
                    else:
                        ans[j - i] = [[i + 1, j + 1]]
    tmp_list = ans[min(ans.keys())]
    return [tmp_list[0][0], tmp_list[0][1]]

inputdatas = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
]

"""
2020 카카오 인턴십 기출. Lv.3
35분 정도에 첫 로직을 완성했고 런타임에러가 많았다.
이전에 런타임 에러는 인덱싱 관련 오타였기에 이번에도 범위체크를 했고,
두 곳의 range에서 실수를 고쳤다. 이번에는 시간초과가 많았다.
처음에는 sorting을 여러 차례 했고, 보석 종류 수 이상의 길이를 가진 모든 idx 조합을 테스트했다. 
시간을 줄이기 위해 각 보석들의 위치 인덱스를 따로 set로 저장하여 순회했으나
나중에 눈치챈건데, 
진열대 전부에 보석이 있으므로 결국 set에 모든 인덱스가 들어가서 의미가 없었다.
check 함수가 filter를 사용하던게 시간을 잡아먹나 해서 이진탐색을 사용하기 위해
각 보석의 인덱스를 heapq를 사용해 정렬을 유지하고
이진탐색을 사용했다. 최소, 최대 인덱스를 먼저 확인 후 범위를 벗어나면 return하여 시간을 줄였다.
최초에 최소길이를 크게 할당하고 i, j 조합을 만들었다.
j - i가 보석 종류 수 이상이고, 최소 길이 이하인 경우에만 체크해줬고
모든 보석이 있다면 최소길이를 갱신해주고
ans 딕셔너리에 길이별로 범위를 기록해줬다.
그 후 가장 짧은 길이의 범위들이 담긴 리스트만 갖고와서
첫 원소(heapq로 시작 진열대 번호가 최소인 원소가 가장 앞으로 오도록 함)에서 범위를 뽑아 리턴했다.
나름 시간을 꽤 줄인 것 같은데 85분을 사용하고도 정확성 테스트에서도 테스트케이스 하나가 시간초과가 났다.
while Trying
"""

for t in inputdatas:
    print(solution(t))
