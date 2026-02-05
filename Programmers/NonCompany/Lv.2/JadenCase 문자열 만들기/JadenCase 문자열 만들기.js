// https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=javascript

/*
constraints:

*/


function solution(s) {
    var ss = s.split(" ");
    var res = [];
    for (var word of ss) {
        if (word.length === 0) {
            res.push(word);
            continue;
        }
        word = word[0].toUpperCase() + word.slice(1).toLowerCase();
        res.push(word);
    }
    return res.join(" ");
}


const inputDatas = [
    {data: ["3people unFollowed me"], answer: "3people Unfollowed Me"},
    {data: ["for the last week"], answer: "For The Last Week"}
];

/*
연습문제
Lv.2. 현 시점 완료한 사람 44,487명, 정답률 80%
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
