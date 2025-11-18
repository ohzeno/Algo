from Utils.boj_judge_utils import run_judge


inputdatas = [
    {"data": """1
500 0 0 500
1
0 0 0 0""", "answer": """1000"""},
    {"data": """0
0""", "answer": """0"""},
    {"data": """2
0 0 250 250
250 250 500 500
2
0 251 249 500
251 0 500 249""", "answer": """1000"""},
    {"data": """2
0 0 250 250
250 250 500 500
2
0 250 250 500
250 0 500 250""", "answer": """-1"""}
]

run_judge(inputdatas)
