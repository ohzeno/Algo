import clipboard
import sys
sys.stdin = open('input.txt', encoding='utf-8')
def input():
    return sys.stdin.readline().rstrip()

def conversion(lines):
    new_codes = []
    comm = False
    for line in lines:
        line = line.rstrip()
        if "\"\"\"" in line:  # 여러 줄 주석 토글
            comm = not comm
            continue
        if comm:  # 여러 줄 주석은 넘어감
            continue
        if line.startswith("inputdatas = ["):  # 릿코드, 프로그래머스 양식
            break
        if line == '' or line == '\n':  # 빈 줄
            continue
        if line.startswith("sys.stdin = open"):  # input.txt를 감싸는 따옴표 종류가 다를 수 있으니 open까지만.
            continue
        if line.lstrip().startswith('#'):
            continue
        if '#' in line:
            while '#' in line:
                ridx = line.rfind('#')
                if line[ridx-1:ridx+1] != "'#":
                    line = line[:line.rfind('#')].rstrip()
                else:
                    break
        line += '\n'
        new_codes.append(line)
    output = ''.join(new_codes)
    if output[-1] == '\n':
        output = output[:-1]
    return output

# 텍스트 파일에서 스키마 쿼리를 읽어 하나의 스트링으로 만듦.
input_code = [line for line in sys.stdin]
# 스키마 쿼리를 변환하고 클립보드에 복사함.
clipboard.copy(conversion(input_code))
