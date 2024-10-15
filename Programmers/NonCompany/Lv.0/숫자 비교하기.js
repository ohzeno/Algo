// https://school.programmers.co.kr/learn/courses/30/lessons/120807?language=javascript

/*
constraints:
  • 0 ≤ num1 ≤ 10,000
  • 0 ≤ num2 ≤ 10,000
*/


function solution(num1, num2) {
    return num1 === num2 ? 1 : -1;
}


const inputDatas = [
    {data: [2, 3], answer: -1},
    {data: [11, 11], answer: 1},
    {data: [7, 99], answer: -1}
];

/*
코딩테스트 입문
Lv.0. 현 시점 완료한 사람 71,693명, 정답률 91%
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
