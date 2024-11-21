// https://school.programmers.co.kr/learn/courses/30/lessons/17677?language=javascript

/*
constraints:

*/

function solution(str1, str2) {
    function isAlpha(s) {
        for (let i = 0; i < s.length; i++) {
            if (!("a" <= s[i] && s[i] <= "z")) return false;
        }
        return true;
    }

    function str2d(s) {
        const d = {};
        for (let i = 0; i < s.length - 1; i++) {
            const part = s.slice(i, i+2).toLowerCase();
            if (isAlpha(part)) {
                d[part] = d[part] ? d[part] + 1 : 1;
            }
        }
        return d;
    }

    const [d1, d2] = [str1, str2].map(str2d);
    const [set1, set2] = [d1, d2].map((d) => new Set(Object.keys(d)));
    const interCnt = [...set1]
        .filter((e) => set2.has(e))
        .reduce((cnt, part) => cnt + Math.min(d1[part], d2[part]), 0);
    const unionCnt = [...new Set([...set1, ...set2])].reduce(
        (cnt, part) => cnt + Math.max(d1[part] || 0, d2[part] || 0),
        0,
    );
    return unionCnt ? Math.floor((interCnt / unionCnt) * 65536) : 65536;
}

inputDatas = [
    { data: ["FRANCE", "french"], answer: 16384 },
    { data: ["handshake", "shake hands"], answer: 65536 },
    { data: ["aa1+aa2", "AAAA12"], answer: 43690 },
    { data: ["E=M*C^2", "e=m*c^2"], answer: 65536 },
];

/*
2018 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 19,844명, 정답률 62%
최대한 파이썬과 비슷한 풀이로 풀어봤다. isalpha에 대응되는 함수가 없어서 직접 만들어야 했다.
Set and, or 연산 없는게 많이 불편하다.
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
