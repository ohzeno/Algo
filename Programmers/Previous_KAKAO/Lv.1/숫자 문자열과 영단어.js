// https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=javascript

/*
constraints:
  • 1 ≤ s의 길이 ≤ 50
  • s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
  • return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.
*/


function solution(s) {
    const numDict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    };
    let newS = '';
    let tmp = '';
    for (let c of s) {
        if ("0" <= c && c <= "9") {
            newS += c;
        } else {
            tmp += c;
            if (tmp in numDict) {
                newS += numDict[tmp];
                tmp = '';
            }
        }
    }
    return parseInt(newS);
}


const inputDatas = [
    {data: ["one4seveneight"], answer: 1478},
    {data: ["23four5six7"], answer: 234567},
    {data: ["2three45sixseven"], answer: 234567},
    {data: ["123"], answer: 123}
];

/*
2021 카카오 채용연계형 인턴십
Lv.1. 현 시점 완료한 사람 50,920명, 정답률 72%
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
