# https://school.programmers.co.kr/learn/courses/30/lessons/81303
"""
constraints:
  • 5 ≤ n ≤ 1,000,000
  • 0 ≤ k < n
  • 1 ≤ cmd의 원소 개수 ≤ 200,000
    ◦ cmd의 각 원소는 "U X", "D X", "C", "Z" 중 하나입니다.
    ◦ X는 1 이상 300,000 이하인 자연수이며 0으로 시작하지 않습니다.
    ◦ X가 나타내는 자연수에 ',' 는 주어지지 않습니다. 예를 들어 123,456의 경우 123456으로 주어집니다.
    ◦ cmd에 등장하는 모든 X들의 값을 합친 결과가 1,000,000 이하인 경우만 입력으로 주어집니다.
    ◦ 표의 모든 행을 제거하여, 행이 하나도 남지 않는 경우는 입력으로 주어지지 않습니다.
    ◦ 본문에서 각 행이 제거되고 복구되는 과정을 보다 자연스럽게 보이기 위해 "이름" 열을 사용하였으나, "이름"열의 내용이 실제 문제를 푸는 과정에 필요하지는 않습니다. "이름"열에는 서로 다른 이름들이 중복없이 채워져 있다고 가정하고 문제를 해결해 주세요.
  • 표의 범위를 벗어나는 이동은 입력으로 주어지지 않습니다.
  • 원래대로 복구할 행이 없을 때(즉, 삭제된 행이 없을 때) "Z"가 명령어로 주어지는 경우는 없습니다.
  • 정답은 표의 0행부터 n - 1행까지에 해당되는 O, X를 순서대로 이어붙인 문자열 형태로 return 해주세요.
"""


def solution(n, k, cmd):
    def move(steps):
        nonlocal selected
        for _ in range(abs(steps)):
            if steps > 0:
                selected = selected["next"]
            else:
                selected = selected["prev"]

    def delete():
        nonlocal selected
        deleted.append(selected)
        alive[selected["idx"]] = "X"
        if selected["prev"]:
            selected["prev"]["next"] = selected["next"]
        if selected["next"]:
            selected["next"]["prev"] = selected["prev"]
            selected = selected["next"]
        else:
            selected = selected["prev"]

    def restore():
        nonlocal selected
        node = deleted.pop()
        alive[node["idx"]] = "O"
        if node["prev"]:
            node["prev"]["next"] = node
        if node["next"]:
            node["next"]["prev"] = node

    table = [{} for _ in range(n)]  # [{}] * n로 하면 같은 객체를 참조하게 된다.
    for i in range(n):
        """
        table[i] = {} 형식으로 초기화하면 새로 객체를 할당하기 때문에
        prev, next 할당에 오류가 생긴다.
        """
        table[i]["idx"] = i
        table[i]["prev"] = table[i-1] if i else None
        table[i]["next"] = table[i+1] if i < n-1 else None
    alive = ["O"] * n
    selected = table[k]
    deleted = []
    for order in cmd:
        if order[0] == "U":
            move(-int(order[2:]))
        elif order[0] == "D":
            move(int(order[2:]))
        elif order[0] == "C":
            delete()
        else:
            restore()
    return "".join(alive)


inputdatas = [
    {"data": [6, 4, ["C","U 1","C","Z","U 2","C"]], "answer": "OOXOXO"},
    {"data": [8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]], "answer": "OOOOXOOO"},
    {"data": [8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]], "answer": "OOXOXOOO"}
]


"""
2021 카카오 채용연계형 인턴십
Lv.3. 현 시점 완료한 사람 5,176명, 정답률 38%
이전엔 1시간 걸려서 리스트 작성, 80분으로 딕셔너리 풀이 작성. 이후에도 오류 수정 시간 추가.
이번엔 27분만에 클래스로 해결했다.
클래스 풀이가 느려서 딕셔너리로 개선해봤다. 
설계 과정에서 참조 문제를 고민하느라 구현에 20분 정도 걸렸다.
클래스 풀이나 이전 딕셔너리 풀이보다 빠르다.
"""

for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
