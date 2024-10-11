// https://school.programmers.co.kr/learn/courses/30/lessons/17682?language=javascript

/*
constraints:

*/


function solution(dartResult) {
    const bonus2exp = {"S": 1, "D": 2, "T": 3};
    const points = new Array(3).fill(0);
    let cur_point = 0;
    for (const c of dartResult) {
        if (!isNaN(c)) {
            cur_point = cur_point * 10 + parseInt(c);
        } else if (c in bonus2exp) {
            points.push(cur_point ** bonus2exp[c]);
            cur_point = 0;
        } else if (c === "*") {
            const lastTwo = points.slice(-2).map(x => x * 2);
            points.splice(-2, 2, ...lastTwo);
        } else if (c === "#") {
            points[points.length - 1] *= -1;
        }
    }
    return points.reduce((a, b) => a + b);
}


const inputDatas = [
    {data: ["1S2D*3T"], answer: 37},
    {data: ["1D2S#10S"], answer: 9},
    {data: ["1D2S0T"], answer: 3},
    {data: ["1S*2T*3S"], answer: 23},
    {data: ["1D#2S*3S"], answer: 5},
    {data: ["1T2D3D#"], answer: -4},
    {data: ["1D2S3T*"], answer: 59}
];

/*
2018 KAKAO BLIND RECRUITMENT
Lv.1. 현 시점 완료한 사람 28,567명, 정답률 59%
파이썬과 같은 방식으로 풀었다.
정규식 사용 풀이를 제외한 다른 js 풀이들은 엄청나게 긴 풀이들 뿐이다.
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
