// https://school.programmers.co.kr/learn/courses/30/lessons/17687?language=javascript

/*
constraints:

*/


function solution(n, t, m, p) {
    let total = '0'
    const hex_str = 'ABCDEF'
    for (let i = 1; i < m * (t-1) + p + 1; i++) {
        let tmp = ''
        let q = i
        while (q) {
            const r = q % n
            q = Math.floor(q / n)
            tmp = ((n > 10 && r >= 10) ? hex_str[r - 10] : String(r)) + tmp
        }
        total += tmp
    }
    return Array.from({ length: t}, (_, i) => total[p-1 + i * m]).join('');
}


const inputDatas = [
    {data: [2, 4, 2, 1], answer: "0111"},
    {data: [16, 16, 2, 1], answer: "02468ACE11111111"},
    {data: [16, 16, 2, 2], answer: "13579BDF01234567"}
];

/*
2018 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 13,701명, 정답률 61%
파이썬 풀이와 같은 로직.
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
