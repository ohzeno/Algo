import io
import sys
import traceback
from contextlib import redirect_stdout, redirect_stderr
import subprocess
import re


def get_result(script_path, input_data: str) -> tuple[str, str]:
    if script_path.endswith('.py'):
        return process_py_code(script_path, input_data)
    elif script_path.endswith('.js'):
        return process_js_code(script_path, input_data)


def process_py_code(script_path, input_data: str) -> tuple[str, str]:
    # 입력 스트림을 StringIO 객체로 변경
    sys.stdin = io.StringIO(input_data)
    # 출력과 에러 캡처를 위한 StringIO 객체 생성
    output = io.StringIO()
    errors = io.StringIO()

    with open(script_path, encoding="utf-8") as f:
        code_str = f.read()

    # sys.stdin = open('input.txt') 패턴을 찾아서 주석처리
    code_str = re.sub(r"sys\.stdin\s*=\s*open\(['\"]input\.txt['\"].*?\)",
                      lambda m: '# ' + m.group(0), code_str)

    code = compile(code_str, script_path, "exec")
    # 표준 출력을 output으로 변경 후 스크립트 실행
    with redirect_stdout(output), redirect_stderr(errors):
        try:
            exec(code, {"__name__": "__main__"})
        except Exception as e:
            # 예외 발생 시 traceback 정보를 에러스트림에 출력
            tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
            # 채점기가 아닌 풀이 코드의 에러만 출력
            filtered_tb_lines = [
                line for line in tb_lines if "boj_judge.py" not in line
            ]
            errors.writelines(filtered_tb_lines)
    # 출력값, 에러값을 문자열로 변환
    return output.getvalue(), errors.getvalue()


def process_js_code(script_path, input_data: str) -> tuple[str, str]:
    with open(script_path, encoding="utf-8") as f:
        code_str = f.read()

    # input_data를 JavaScript 배열 형태로 변환
    lines_array = str(input_data.split('\n'))

    # lines 변수 할당 부분을 배열로 대체
    code_str = re.sub(
        r'realCodeLines = .*?\.split\("\\n"\);',
        f'realCodeLines = {lines_array};',
        code_str
    )

    try:
        result = subprocess.run(
            ['node', '-e', code_str],
            text=True,
            capture_output=True,
            timeout=5
        )
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)