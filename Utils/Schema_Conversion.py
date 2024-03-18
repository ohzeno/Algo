import clipboard
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def conversion(input_sql):
    lines = input_sql.split('\n')
    insert_statements = {}
    drops = []
    creates = []
    for line in lines:
        if line.startswith("Create table If Not Exists"):
            drops.append(f"DROP TABLE IF EXISTS {line.split(' ')[5]};")
            creates.append(line.replace(" If Not Exists", "") + ';')
        elif line.startswith("Truncate table"):
            continue
        elif line.startswith("insert into"):
            table = line.split(' ')[2]
            columns = line[line.find("(") - 1:line.find(")") + 1].strip()
            values = line[line.rfind("("):].strip()
            insert_statements.setdefault(
                table,
                {
                    'columns': columns,
                    'values': []
                }
            )['values'].append(values)
    inserts = []
    for table, statement in insert_statements.items():
        inserts.append(
            f"insert into {table} {statement['columns']}\n"
            f"values {statement['values'][0]},\n"
        )
        for value in statement['values'][1:]:
            inserts.append(f"       {value},\n")
        inserts[-1] = inserts[-1][:-2] + ';\n'  # 콤마 제거하고 ;붙임
    output = "\n".join(drops + creates) \
             + "\n" + "".join(inserts)
    output = output[:-1]  # 마지막 개행문자 제거
    return output

# 텍스트 파일에서 스키마 쿼리를 읽어 하나의 스트링으로 만듦.
input_query = ""
while True:
    line = input()
    if not line:
        break
    input_query += line + "\n"
# 스키마 쿼리를 변환하고 클립보드에 복사함.
clipboard.copy(conversion(input_query))
