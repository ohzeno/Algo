// https://school.programmers.co.kr/learn/courses/30/lessons/81303?language=javascript

/*
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
*/

function solution(n, k, cmd) {
    function move(steps) {
        for (let i = 0; i < Math.abs(steps); i++) {
            if (steps > 0) selected = selected.next;
            else selected = selected.prev;
        }
    }

    function remove() {
        deleted.push(selected);
        alive[selected.idx] = "X";
        if (selected.prev) selected.prev.next = selected.next;
        if (selected.next) {
            selected.next.prev = selected.prev;
            selected = selected.next;
        } else {
            selected = selected.prev;
        }
    }

    function restore() {
        const node = deleted.pop();
        alive[node.idx] = "O";
        if (node.prev) node.prev.next = node;
        if (node.next) node.next.prev = node;
    }

    const table = Array.from({ length: n }, (_, idx) => ({
        idx,
        prev: null,
        next: null,
    }));
    for (let i = 0; i < n; i++) {
        if (i > 0) table[i].prev = table[i - 1];
        if (i < n - 1) table[i].next = table[i + 1];
    }
    const alive = Array(n).fill("O");
    let selected = table[k];
    const deleted = [];
    for (const order of cmd) {
        if (order[0] === "U") move(-parseInt(order.slice(2)));
        else if (order[0] === "D") move(parseInt(order.slice(2)));
        else if (order === "C") remove();
        else restore();
    }
    return alive.join("");
}

const inputDatas = [
    { data: [6, 4, ["C", "U 1", "C", "Z", "U 2", "C"]], answer: "OOXOXO" },
    {
        data: [8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]],
        answer: "OOOOXOOO",
    },
    {
        data: [
            8,
            2,
            ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"],
        ],
        answer: "OOXOXOOO",
    },
];

/*
2021 카카오 채용연계형 인턴십
Lv.3. 현 시점 완료한 사람 5,181명, 정답률 38%
파이썬 dict 풀이대로 풀었다.
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
