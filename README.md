# Algo

[TOC]



BaekJoon, Programmers, LeetCode, SWEA 등에서 알고리즘, SQL 문제들을 풀어서 기록하고 있다. Python, JavaScript, SQL은 여기서 관리하고, Java는 [Algo_Java](https://github.com/ohzeno/Algo_Java) 레포에서 관리하고 있다.

사이트, 문제, 언어에 따라 [AlgoBoost](https://github.com/ohzeno/AlgoBoost) 확장프로그램에서 자동으로 양식을 만들고 클립보드에 복사해준다.

SQL의 경우 문제가 적어서 복습하는 경우가 많다. 너무 간단한 쿼리의 경우, 다시 풀어도 변화가 없는 경우가 있어 다시 커밋하지 않기로 한다.

<br>

## boj_judge

프로그래머스나 릿코드와 달리 백준은 테스트케이스가 여럿일 때 테스트가 힘들다.

채점기를 만들어서 한꺼번에 채점할 수 있도록 했다.

```python
import sys
# sys.stdin = open("input.txt")
def input():
    return sys.stdin.readline().rstrip()
```

풀이코드의 sys.stdin = open("input.txt")를 주석처리하고 사용한다.

```py
script = "i_pro.py"
```

boj_judge.py에서 스크립트의 경로를 지정한다. 나는 최상위 폴더의 i_pro.py에 풀이하기에 수정할 일이 거의 없다.

```py
inputdatas = [
    {
        "data": """2 1
5 10
100 100
11""",
        "answer": "10",
    },
    {
        "data": """3 2
1 65
5 23
2 99
10
2""",
        "answer": "164",
    },
]
```

백준의 테케를 복사해서 넣으면 정렬이 이상하게 보이지만 이건 아직 어쩔 수 없다. 여기서 정렬을 맞추면 데이터의 정렬이 이상해져서 입력에 문제가 생김. 그렇다고 테케를 복사해서 붙여넣을 때마다 줄바꿈을 \n으로 바꾸는 것은 비효율적이다.

이후 boj_judge_py.py(언어별로 파일명이 다르다.)를 실행하면 된다.

```cmd
pass
pass
```

테케 모두 통과할 경우.

```cmd
pass
fail
  expected:
    164
  got:
    163
```

틀릴 경우 정답과 내 풀이 출력값 비교

```cmd
pass
fail
  expected:
    164
  Error:
    Traceback (most recent call last):
      File "i_pro.py", line 36, in <module>
        max_price /= 0
    ZeroDivisionError: division by zero
```

풀이 코드에서 에러가 발생할 경우, 해당 코드의 에러만 가져와서 에러 위치와 내용을 출력하도록 처리했다.

<br>

## 제출용 코드 변환

### Algo

로컬과 사이트에 제출할 코드는 다르다. 특히 백준 제출시에는 풀이 코드에서 sys.stdin = open("input.txt")을 제거하지 않으면 오류가 발생한다.

```py
file_path = '../i_pro.py'
```

제출용 코드 변환/제출용 코드 변환.py에서 변환할 코드 경로를 입력. ~~나는 i_pro.py만 사용해서 수정할 일이 거의 없다.~~ js, java 문제풀이도 하게 되어 언어별 변환 파일을 따로 만들었다.

이후 실행하면 코드에서 주석을 비롯해 불필요한 부분을 제거하고 클립보드에 복사한다. 백준, 릿코드, 프로그래머스 모두 가능.

<br>

### SQL 스키마 변환

프로그래머스는 스키마를 제공하지 않지만 릿코드는 스키마를 제공해서 로컬에서 테스트할 수 있다. 하지만 스키마가 난잡해서 알아보기 힘들다. 

SQL/input.txt에 릿코드의 스키마를 붙여넣고 SQL/Schema_Conversion.py를 실행하면 알아보기 쉽게 변환된 쿼리가 클립보드에 복사된다.

해당 쿼리를 sql_pro.sql 위쪽에 붙여넣고 쿼리를 넣고 실행하면 로컬에서 db를 조회하고 테스트할 수 있다.

```sql
Create table If Not Exists Product (product_id int, product_name varchar(10), unit_price int)
Create table If Not Exists Sales (seller_id int, product_id int, buyer_id int, sale_date date, quantity int, price int)
Truncate table Product
insert into Product (product_id, product_name, unit_price) values ('1', 'S8', '1000')
insert into Product (product_id, product_name, unit_price) values ('2', 'G4', '800')
insert into Product (product_id, product_name, unit_price) values ('3', 'iPhone', '1400')
Truncate table Sales
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('1', '1', '1', '2019-01-21', '2', '2000')
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('1', '2', '2', '2019-02-17', '1', '800')
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('2', '2', '3', '2019-06-02', '1', '800')
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) values ('3', '3', '4', '2019-05-13', '2', '2800')
```

```sql
Create table If Not Exists Users;
Truncate table Users;
insert into Users;
```

리트코드의 스키마는 위와 같은 과정을 거치지만 이렇게 하면 이미 Users 테이블이 존재할 경우, 데이터만 제거된다.

그리고 새로 입력하려던 Users와 기존 Users의 스키마가 다를 경우 오류가 발생한다.

```sql
DROP TABLE IF EXISTS Users;
```

그래서 DROP TABLE IF EXISTS Users; 를 사용하여 기존 테이블이 존재할 경우 제거하고 새로운 테이블을 생성하도록 했다.

```sql
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Sales;
Create table Product (product_id int, product_name varchar(10), unit_price int);
Create table Sales (seller_id int, product_id int, buyer_id int, sale_date date, quantity int, price int);
insert into Product (product_id, product_name, unit_price)
values ('1', 'S8', '1000'),
       ('2', 'G4', '800'),
       ('3', 'iPhone', '1400');
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price)
values ('1', '1', '1', '2019-01-21', '2', '2000'),
       ('1', '2', '2', '2019-02-17', '1', '800'),
       ('2', '2', '3', '2019-06-02', '1', '800'),
       ('3', '3', '4', '2019-05-13', '2', '2800');
```

변환된 쿼리

<br>

## 양식

백준, 프로그래머스, 릿코드, 프로그래머스 sql, 릿코드 sql 양식을 따로 뒀다.

js양식은 로직이 같으니 여기서 다루지 않는다. java양식은 [Algo_Java](https://github.com/ohzeno/Algo_Java) 레포에 있고, 로직이 같으니 다루지 않는다.

평소에는 [AlgoBoost](https://github.com/ohzeno/AlgoBoost) 확장프로그램에서 양식을 자동으로 만들고 클립보드에 넣어주면 i_pro.py, i_pro.js, Main.java 등에 붙여넣고 풀고 있다.

 백준, 프로그래머스 양식은 특이사항이 없으므로 여기서 설명하지 않는다.

<br>

### 리트코드 양식

```py
import inspect
functions = [
    value for value in Solution.__dict__.values() if inspect.isfunction(value)
]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = my_func(sol, *data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
```

릿코드는 Solution함수 내부에 함수를 만들도록 되어있으므로 my_func에 Solution 내부 함수들을 가져와서 사용한다. 함수가 여럿이면 my_func에서 인덱싱 해줘야 하고, 인풋데이터가 릿코드식 트리구조인 경우, 트리를 만드는 등 따로 작업한다.

functions는 정의순서를 유지하기 위해 `__dict__`로 직접 참조하였다. my_func는 인스턴스 메서드 사용이지만 직접참조라 self가 자동 전달되지 않는다. 그래서 인스턴스를 생성해서 첫 인자로 넣어준다.

ex) [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan&id=level-1)

```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def build_binary_tree(datas: List[Optional[int]]):
    if not datas:
        return None
    root = TreeNode(datas[0])
    queue = deque([root])
    i = 1  # 인덱스 0은 이미 처리했으므로, 인덱스 1부터 시작
    l_datas = len(datas)
    while i < l_datas:
        cur_node = queue.popleft()
        for side in ["left", "right"]:  # 자식 추가
            if i < l_datas and datas[i] is not None:
                child = TreeNode(datas[i])
                setattr(cur_node, side, child)  # cur_node.side = child
                queue.append(child)
            i += 1
    return root

import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    tree = build_binary_tree(t)
    print(my_func(tree))
```

<br>

### 리트코드 SQL 양식

```sql
Create table If Not Exists Users;
Truncate table Users;
insert into Users;
```

리트코드의 스키마는 위와 같은 과정을 거치지만 이렇게 하면 이미 Users 테이블이 존재할 경우, 데이터만 제거된다.

그리고 새로 입력하려던 Users와 기존 Users의 스키마가 다를 경우 오류가 발생한다.

```sql
DROP TABLE IF EXISTS Users;
```

그래서 DROP TABLE IF EXISTS Users; 를 사용하여 기존 테이블이 존재할 경우 제거하고 새로운 테이블을 생성하도록 했다.

Schema_Conversion.py에서는 이런 내용을 고려하여 변환하도록 되어있다.
