from Utils.boj_judge_utils import run_judge


inputdatas = [
    {"data": """1 7
f0.F..1""", "answer": """7"""},
    {"data": """5 5
....1
#1###
.1.#0
....A
.1.#.""", "answer": """-1"""},
    {"data": """7 8
a#c#eF.1
.#.#.#..
.#B#D###
0....F.1
C#E#A###
.#.#.#..
d#f#bF.1""", "answer": """55"""},
    {"data": """3 4
1..0
###.
1...""", "answer": """3"""},
    {"data": """3 5
..0..
.###.
..1.A""", "answer": """6"""},
    {"data": """4 5
0....
.#B#A
.#.#.
b#a#1""", "answer": """19"""},
    {"data": """1 11
c.0.C.C.C.1""", "answer": """12"""},
    {"data": """3 6
###...
#0A.1a
###...""", "answer": """-1"""}
]

run_judge(inputdatas)
