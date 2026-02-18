// https://school.programmers.co.kr/learn/courses/30/lessons/12924?language=javascript

/*
constraints:
  • n은 10,000 이하의 자연수 입니다.
*/


function solution(n) {
    let cnt = 0;
    let m = 1;
    while (true) {
        let val = 2 * n / m - m + 1;
        if (val < 2) break;
        if (!(val % 2))
            cnt += 1;
        m += 1;
    }
    return cnt;
}


const inputDatas = [
    {data: [15], answer: 4}
];

/*
연습문제
Lv.2. 현 시점 완료한 사람 36,296명, 정답률 76%
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
