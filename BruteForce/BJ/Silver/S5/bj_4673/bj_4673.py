# https://www.acmicpc.net/problem/4673
# 중복 생성자 제거 위해 세트 사용
a = set()
i = 1
# 1만 이하의 셀프넘버는 생성자가 없음
# d(n)은 생성자보다 항상 크거나 같다.
# 1만까지 체크하면 1만 이하의 생성자가 있는 수. 즉, d(n)을 모두 찾을 수 있음
while i <= 10000:
    # 자리마다 더하기 위해 스트링으로 변환
    b = str(i)
    r = i
    # 자기 자신에 각 자리 숫자 더하기
    for j in range(len(b)):
        r += int(b[j])
    # 만들어진 d(n)을 세트에 넣고 i 증가
    a.add(r)
    i += 1
# 1만보다 작거나 같은 셀프넘버를 찾기 위해
# 1만까지 다 넣은 세트 생성
c = set(i for i in range(1, 10001))
# 1만까지의 수에서 생성자를 자 빼버리고 리스트로 만들어 오름차순으로 정렬한다.
res = sorted(list(c - a))
for re in res:
    print(re)



