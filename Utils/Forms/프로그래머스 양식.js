// https://school.programmers.co.kr/learn/courses/30/lessons/17682

/*
constraints:
*/

function solution() {
    return;
}


const inputDatas = [
    {data: [], answer: ""},
];

/*
2022 카카오 테크 인턴십 기출.
Lv.3. 현 시점 완료한 사람 1155명, 정답률 22%
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