// https://school.programmers.co.kr/learn/courses/30/lessons/77485?language=javascript

/*
constraints:
  • rows는 2 이상 100 이하인 자연수입니다.
  • columns는 2 이상 100 이하인 자연수입니다.
  • 처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
    ◦ 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
  • queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
  • queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
    ◦ x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
    ◦ 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
    ◦ 모든 회전은 순서대로 이루어집니다.
    ◦ 예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.
*/

function solution(rows, columns, queries) {
    function rotateEdges(x1, y1, x2, y2) {
        const toRotate = [];
        [x1, y1, x2, y2] = [x1, y1, x2, y2].map((e) => e - 1);
        toRotate.push(...mat[x1].slice(y1, y2 + 1));
        for (let r = x1 + 1; r <= x2; r++) toRotate.push(mat[r][y2]);
        toRotate.push(...mat[x2].slice(y1, y2).reverse());
        for (let r = x2 - 1; r > x1; r--) toRotate.push(mat[r][y1]);
        toRotate.unshift(toRotate.pop());
        let minNum = Math.min(...toRotate);
        for (let c = y1; c <= y2; c++) mat[x1][c] = toRotate.shift();
        for (let r = x1 + 1; r <= x2; r++) mat[r][y2] = toRotate.shift();
        for (let c = y2 - 1; c >= y1; c--) mat[x2][c] = toRotate.shift();
        for (let r = x2 - 1; r > x1; r--) mat[r][y1] = toRotate.shift();
        return minNum;
    }

    const mat = Array.from({ length: rows }, (_, r) =>
        Array.from({ length: columns }, (_, c) => r * columns + c + 1),
    );
    return queries.map((query) => rotateEdges(...query));
}

const inputDatas = [
    {
        data: [
            6,
            6,
            [
                [2, 2, 5, 4],
                [3, 3, 6, 6],
                [5, 1, 6, 3],
            ],
        ],
        answer: [8, 10, 25],
    },
    {
        data: [
            3,
            3,
            [
                [1, 1, 2, 2],
                [1, 2, 2, 3],
                [2, 1, 3, 2],
                [2, 2, 3, 3],
            ],
        ],
        answer: [1, 1, 5, 3],
    },
    { data: [100, 97, [[1, 1, 100, 97]]], answer: [1] },
];

/*
2021 Dev-Matching: 웹 백엔드 개발자(상반기)
Lv.2. 현 시점 완료한 사람 12,846명, 정답률 48%
파이썬과 같은 로직.
*/

for (let i = 0; i < inputDatas.length; i++) {
    const { data, answer } = inputDatas[i];
    const res = solution(...data);
    if (JSON.stringify(res) === JSON.stringify(answer)) {
        console.log("pass");
    } else {
        let summary = "fail";
        for (const [label, content] of [
            ["expected:", answer],
            ["got:", res],
        ]) {
            summary += `\n  ${label}\n`;
            summary += `    ${content}`;
            summary = summary.trimEnd();
        }
        console.log(summary);
    }
}
