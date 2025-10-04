from Utils.boj_judge_util import *


inputdatas = [
    {"data": """25
17
31
0""", "answer": """25
25 12 18 15 16 17
25 38 31"""}
]

script_path = "../i_pro.py"

for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    output, error = get_result(script_path, data)
    output = output.rstrip()  # 개행문자 제거
    if output == ans:  # 정답과 출력값이 같으면 pass
        print("pass")
    else:  # 다르면 fail과 정답, 출력값 출력
        summary = "fail"
        print(f"\nInput: {data}")
        for label, content in [("expected:", ans), ("got:", output), ("Error:", error)]:
            if label == "Error:" and not content:
                continue
            summary += f"\n  {label}\n"
            for line in content.splitlines():
                summary += f"    {line}\n"
            summary = summary.rstrip()
        print(summary)
