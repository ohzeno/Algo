// https://school.programmers.co.kr/learn/courses/30/lessons/12938?language=javascript

/*
constraints:
  • 최고의 집합은 로 return 해주세요.
  • 만약 최고의 집합이 존재하지 않는 경우에 에 -1 을 채워서 return 해주세요.
  • 자연수의 개수 n은 1 이상 10,000 이하의 자연수입니다.
  • 모든 원소들의 합 s는 1 이상, 100,000,000 이하의 자연수입니다.
*/


function solution(n, s) {
    if (n > s) return [-1];
    const answer = new Array(n).fill(Math.floor(s / n));
    const length = answer.length;
    for (let i = 1; i < s % n+1; i++) {
        answer[length - i]++;
    }
    return answer;
}


const inputDatas = [
    {data: [2, 9], answer: [4, 5]},
    {data: [2, 1], answer: [-1]},
    {data: [2, 8], answer: [4, 4]}
];

/*
연습문제
Lv.3. 현 시점 완료한 사람 14,380명, 정답률 58%
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
