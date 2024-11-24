// https://school.programmers.co.kr/learn/courses/30/lessons/64065?language=javascript

/*
constraints:

*/

function solution(s) {
    let datas = s
        .slice(2, -2)
        .split("},{")
        .map((x) => new Set(x.split(",").map(Number)))
        .sort((a, b) => a.size - b.size);
    const ans = [];
    let pre = new Set();
    for (const data of datas) {
        ans.push([...data].find((x) => !pre.has(x)));
        pre = data;
    }
    return ans;
}

const inputDatas = [
    { data: ["{{2},{2,1},{2,1,3},{2,1,3,4}}"], answer: [2, 1, 3, 4] },
    { data: ["{{1,2,3},{2,1},{1,2,4,3},{2}}"], answer: [2, 1, 3, 4] },
    { data: ["{{20,111},{111}}"], answer: [111, 20] },
    { data: ["{{123}}"], answer: [123] },
    { data: ["{{4,2,3},{3},{2,3,4,1},{2,3}}"], answer: [3, 2, 4, 1] },
];

/*
2019 카카오 개발자 겨울 인턴십
Lv.2. 현 시점 완료한 사람 23,396명, 정답률 64%
파이썬과 비슷하게 풀었다.
js도 마찬가지로 Set 삽입순서가 유지되는 점을 이용할 수 있지만,
오해를 막기 위해 그러지 않았다.
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
