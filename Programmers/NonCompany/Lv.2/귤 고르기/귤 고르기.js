// https://school.programmers.co.kr/learn/courses/30/lessons/138476?language=javascript

/*
constraints:
  • 1 ≤ k ≤ tangerine의 길이 ≤ 100,000
  • 1 ≤ tangerine의 원소 ≤ 10,000,000
*/


function solution(k, tangerine) {
    const cntD = {};
    for (let size of tangerine)
        cntD[size] = (cntD[size] || 0) + 1;
    let tot = 0;
    let types = 0;
    for (let cnt of Object.values(cntD).sort((a, b) => b - a)) {
        tot += cnt;
        types += 1;
        if (tot >= k)
            return types;
    }
}


const inputDatas = [
    {data: [6, [1, 3, 2, 5, 4, 5, 2, 3]], answer: 3},
    {data: [4, [1, 3, 2, 5, 4, 5, 2, 3]], answer: 2},
    {data: [2, [1, 1, 1, 1, 2, 2, 2, 3]], answer: 1}
];

/*
연습문제
Lv.2. 현 시점 완료한 사람 24,562명, 정답률 72%
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = solution(...data);
    if (JSON.stringify(res) === JSON.stringify(answer)) {
        console.log("pass");
    } else {
        let summary = "fail";
        for (const [label, content] of [["expected:", answer], ["got:", res]]) {
            summary += `\n  ${label}\n`;
            summary += `    ${content}`;
            summary = summary.trimEnd();
        }
        console.log(summary);
    }
}
