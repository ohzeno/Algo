# https://school.programmers.co.kr/learn/courses/30/lessons/150366
"""
표는 50x50이며 모든 셀이 비어 있음.
각 셀은 문자열 값을 가질 수 있고, 다른 셀과 변합될 수 있음.

1 ≤ commands의 길이 ≤ 1,000
commands의 각 원소는 아래 5가지 형태 중 하나입니다.
    "UPDATE r c value"    
        value는 셀에 입력할 내용, 알파벳 소문자와 숫자로 구성된 길이 1~10 사이인 문자열.
        r행 c열의 셀 값을 value로 변경.
        r, c는 선택할 셀의 위치, 1~50 사이의 정수.
    "UPDATE value1 value2"    
        값이 val1인 모든 셀의 값을 val2로 변경.
        value1은 선택할 셀의 값, value2는 셀에 입력할 내용, 알파벳 소문자와 숫자로 구성된 길이 1~10 사이인 문자열.
    "MERGE r1 c1 r2 c2"    
        r1행 c1열의 셀과 r2행 c2열의 셀을 합침.
        같은 셀이면 무시.
        인접하지 않으면 사이의 셀들은 영향받지 않음.
        한 셀만 값을 갖고있으면 병합된 셀은 그 값을 갖게 됨.
        두 셀 모두 값이 있으면 r1, c1 위치의 값을 갖게 됨.
        이후 r1c1, r2c2중 어느 위치를 선택해도 병합셀로 접근함.
        r1, c1, r2, c2는 선택할 셀의 위치, 1~50 사이의 정수.
    "UNMERGE r c"    
        r행 c열의 셀의 모든 병합을 해제.
        모든 셀은 프로그램 초기로 돌아감.
        값을 갖고있으면 rc셀이 그 값을 갖게 됨.
        r, c는 선택할 셀의 위치, 1~50 사이의 정수.
    "PRINT r c"    
        rc셀의 값을 출력. 값이 없으면 EMPTY 출력.
        r, c는 선택할 셀의 위치, 1~50 사이의 정수.
commands는 1개 이상의 "PRINT r c" 명령어를 포함.
"""


def solution(commands):
    def update1(datas):
        r, c = convert_idx(datas[:2])
        value = datas[2]
        gr, gc = gids[r][c]
        mat[gr][gc] = value

    def update2(datas):
        val1, val2 = datas
        for i in range(50):
            for j in range(50):
                if mat[i][j] == val1:
                    mat[i][j] = val2

    def merge(datas):
        r1, c1, r2, c2 = convert_idx(datas)
        gr1, gc1 = gids[r1][c1]
        gr2, gc2 = gids[r2][c2]
        # 같은 그룹이면 무시
        if (gr1, gc1) == (gr2, gc2):
            return
        # 둘다 비어있음 > val1값 그대로
        # val1만 비어있음 > val2값
        # val2만 비어있음 > val1값 그대로
        # 둘다 값이 있음 > val1값 그대로
        # 결론: val1이 비어있을 때만 바꿔주면 됨.
        if mat[gr1][gc1] == "EMPTY":
            mat[gr1][gc1] = mat[gr2][gc2]
        for i in range(50):
            for j in range(50):
                if gids[i][j] == (gr2, gc2):  # 병합셀 가리키도록 포인터 변경
                    gids[i][j] = (gr1, gc1)

    def unmerge(datas):
        r, c = convert_idx(datas)
        gr, gc = gids[r][c]
        val = mat[gr][gc]  # 병합셀 값 저장
        for i in range(50):
            for j in range(50):
                if gids[i][j] == (gr, gc):  # 병합셀 초기화
                    gids[i][j] = (i, j)
                    mat[i][j] = "EMPTY"
        mat[r][c] = val  # 값 계승

    def excel_print(datas):
        r, c = convert_idx(datas)
        gr, gc = gids[r][c]  # 병합셀 값 저장 좌표
        ans.append(mat[gr][gc])

    def convert_idx(li):
        return map(lambda x: int(x) - 1, li)

    ans = []
    mat = [["EMPTY" for _ in range(50)] for _ in range(50)]
    # 어느 셀에 값이 저장되는지 포인터를 기록하는 행렬.
    gids = [[(i, j) for j in range(50)] for i in range(50)]
    for command in commands:
        cmds = command.split()
        if cmds[0] == "UPDATE":
            if len(cmds) == 4:
                update1(cmds[1:])
            else:
                update2(cmds[1:])
        elif cmds[0] == "MERGE":
            merge(cmds[1:])
        elif cmds[0] == "UNMERGE":
            unmerge(cmds[1:])
        else:
            excel_print(cmds[1:])
    return ans


inputdatas = [
    [
        [
            "UPDATE 1 1 menu",
            "UPDATE 1 2 category",
            "UPDATE 2 1 bibimbap",
            "UPDATE 2 2 korean",
            "UPDATE 2 3 rice",
            "UPDATE 3 1 ramyeon",
            "UPDATE 3 2 korean",
            "UPDATE 3 3 noodle",
            "UPDATE 3 4 instant",
            "UPDATE 4 1 pasta",
            "UPDATE 4 2 italian",
            "UPDATE 4 3 noodle",
            "MERGE 1 2 1 3",
            "MERGE 1 3 1 4",
            "UPDATE korean hansik",
            "UPDATE 1 3 group",
            "UNMERGE 1 4",
            "PRINT 1 3",
            "PRINT 1 4",
        ],
        ["EMPTY", "group"],
    ],
    [
        [
            "UPDATE 1 1 a",
            "UPDATE 1 2 b",
            "UPDATE 2 1 c",
            "UPDATE 2 2 d",
            "MERGE 1 1 1 2",
            "MERGE 2 2 2 1",
            "MERGE 2 1 1 1",
            "PRINT 1 1",
            "UNMERGE 2 2",
            "PRINT 1 1",
        ],
        ["d", "EMPTY"],
    ],
    [
        [
            "UPDATE 1 1 apple",
            "MERGE 1 1 2 2",
            "MERGE 2 2 3 3",
            "UNMERGE 1 1",
            "UNMERGE 2 2",
            "PRINT 1 1",
            "PRINT 2 2",
            "PRINT 3 3",
        ],
        ["apple", "EMPTY", "EMPTY"],
    ],
    [
        [
            "MERGE 1 1 2 2",
            "MERGE 1 1 3 3",
            "UPDATE 3 3 A",
            "PRINT 1 1",
            "PRINT 2 2",
            "PRINT 3 3",
        ],
        ["A", "A", "A"],
    ],
    [
        [
            "UPDATE 1 1 A",
            "UPDATE 2 2 B",
            "UPDATE 3 3 C",
            "UPDATE 4 4 D",
            "MERGE 1 1 2 2",
            "MERGE 3 3 4 4",
            "MERGE 1 1 3 3",
            "UNMERGE 1 1",
            "PRINT 1 1",
            "PRINT 2 2",
            "PRINT 3 3",
            "PRINT 4 4",
        ],
        ["A", "EMPTY", "EMPTY", "EMPTY"],
    ],
    [["UPDATE 1 1 value", "PRINT 1 1"], ["value"]],
    [["UPDATE 1 1 value", "PRINT 1 2"], ["EMPTY"]],
    [["UPDATE 1 1 value", "MERGE 1 1 1 2", "PRINT 1 2"], ["value"]],
    [["UPDATE 1 1 value", "MERGE 1 1 1 2", "PRINT 1 1"], ["value"]],
    [["UPDATE 1 1 value", "MERGE 1 1 1 2", "PRINT 2 1"], ["EMPTY"]],
    [["UPDATE 1 1 value", "MERGE 1 1 1 3", "PRINT 1 3"], ["value"]],
    [["UPDATE 1 1 value", "MERGE 1 1 1 3", "PRINT 1 2"], ["EMPTY"]],
    [["UPDATE 1 1 value", "MERGE 1 1 1 2", "UPDATE value test", "PRINT 1 1"], ["test"]],
    [["UPDATE 1 1 value", "MERGE 1 1 1 2", "UPDATE value test", "PRINT 1 2"], ["test"]],
    [
        ["UPDATE 1 1 value", "MERGE 1 1 1 2", "UPDATE value test", "PRINT 2 2"],
        ["EMPTY"],
    ],
    [
        [
            "UPDATE 1 1 value",
            "MERGE 1 1 1 2",
            "UPDATE value test",
            "UNMERGE 1 1",
            "PRINT 1 2",
        ],
        ["EMPTY"],
    ],
    [
        [
            "UPDATE 1 1 value",
            "MERGE 1 1 1 2",
            "UPDATE value test",
            "UNMERGE 1 1",
            "PRINT 1 1",
        ],
        ["test"],
    ],
    [["UPDATE 1 1 value", "UPDATE 1 2 test", "MERGE 1 1 1 2", "PRINT 1 1"], ["value"]],
    [["UPDATE 1 1 value", "UPDATE 1 2 test", "MERGE 1 1 1 2", "PRINT 1 2"], ["value"]],
    [["UPDATE 1 1 value", "UPDATE 1 2 test", "MERGE 1 2 1 1", "PRINT 1 2"], ["test"]],
    [["UPDATE 1 1 value", "UPDATE 1 2 test", "MERGE 1 2 1 1", "PRINT 1 1"], ["test"]],
    [
        [
            "UPDATE 1 1 value",
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UNMERGE 1 1",
            "PRINT 1 1",
        ],
        ["test"],
    ],
    [
        [
            "UPDATE 1 1 value",
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UNMERGE 1 2",
            "PRINT 1 1",
        ],
        ["EMPTY"],
    ],
    [["UPDATE 1 2 test", "MERGE 1 2 1 1", "UNMERGE 1 2", "PRINT 1 1"], ["EMPTY"]],
    [["UPDATE 1 2 test", "MERGE 1 2 1 1", "UNMERGE 1 2", "PRINT 1 2"], ["test"]],
    [
        [
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UPDATE 1 2 test2",
            "UNMERGE 1 2",
            "PRINT 1 2",
        ],
        ["test2"],
    ],
    [
        [
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UPDATE 2 2 test2",
            "UNMERGE 1 2",
            "PRINT 1 2",
        ],
        ["test"],
    ],
    [
        [
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UPDATE 2 2 test2",
            "MERGE 2 2 2 1",
            "UNMERGE 1 2",
            "PRINT 2 2",
        ],
        ["test2"],
    ],
    [
        [
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UPDATE 2 2 test2",
            "MERGE 2 2 2 1",
            "MERGE 2 1 1 1",
            "PRINT 2 2",
        ],
        ["test2"],
    ],
    [
        [
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UPDATE 2 2 test2",
            "MERGE 2 2 2 1",
            "MERGE 2 1 1 1",
            "UNMERGE 1 2",
            "PRINT 1 2",
        ],
        ["test2"],
    ],
    [
        [
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UPDATE 2 2 test2",
            "MERGE 2 2 2 1",
            "MERGE 2 1 1 1",
            "UNMERGE 1 2",
            "PRINT 1 1",
        ],
        ["EMPTY"],
    ],
    [
        [
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UPDATE 2 2 test2",
            "MERGE 2 2 2 1",
            "MERGE 2 1 1 1",
            "UNMERGE 1 2",
            "PRINT 2 1",
        ],
        ["EMPTY"],
    ],
    [
        [
            "UPDATE 1 2 test",
            "MERGE 1 2 1 1",
            "UPDATE 2 2 test2",
            "MERGE 2 2 2 1",
            "MERGE 2 1 1 1",
            "UNMERGE 1 2",
            "PRINT 2 2",
        ],
        ["EMPTY"],
    ],
]

"""
2023 KAKAO BLIND RECRUITMENT 기출. 
Lv.3. 현 시점 완료한 사람 1,321명, 정답률 24%
이게 Lv.3...?
포인터를 이용한 그룹화. 다시 보니 코테 당시에 병합을 엑셀 병합으로 잘못 이해하고 있었다.
문제의 병합은 a1, c1을 병합하면 그 사이 셀들은 병합되지 않는다.
"""

for data, ans in inputdatas:
    res = solution(data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")
