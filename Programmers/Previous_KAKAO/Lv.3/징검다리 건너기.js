// https://school.programmers.co.kr/learn/courses/30/lessons/64062?language=javascript

/*
constraints:

*/

function solution(stones, k) {
    if (k === 1) return Math.min(...stones);
    const lenStones = stones.length;
    if (lenStones === k) return Math.max(...stones);
    if (stones.every((v, i, arr) => i === 0 || arr[i - 1] >= v))
        return stones[lenStones - k];
    let minOfMax = 2e8;
    let i = -1;
    while (i < lenStones - k) {
        let [max_idx, maxStone] = [i + k, stones[i + k]];
        for (let j = k - 1; j > 0; j--) {
            if (maxStone < stones[i + j])
                [max_idx, maxStone] = [i + j, stones[i + j]];
        }
        if (maxStone === 1) return 1;
        minOfMax = Math.min(minOfMax, maxStone);
        i = max_idx;
    }
    return minOfMax;
}

const inputDatas = [
    { data: [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3], answer: 3 },
    { data: [[2, 2, 4, 3, 4, 1, 4, 3, 5, 1], 3], answer: 4 },
    { data: [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10], answer: 10 },
    { data: [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 3], answer: 3 },
    { data: [[2, 2, 2, 2, 2], 3], answer: 2 },
];

/*
2019 카카오 개발자 겨울 인턴십
Lv.3. 현 시점 완료한 사람 7,957명, 정답률 48%
파이썬과 같은 방식의 풀이.
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
