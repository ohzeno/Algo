// https://school.programmers.co.kr/learn/courses/30/lessons/17683?language=javascript

/*
constraints:

*/


function solution(m, musicinfos) {
    function removeSharp(melody) {
        for (let i = 'A'.charCodeAt(0); i <= 'G'.charCodeAt(0); i++) {
            const char = String.fromCharCode(i);
            melody = melody.replaceAll(char + "#", char.toLowerCase());
        }
        return melody;
    }

    function timeToMin(time) {
        const [h, m] = time.split(":").map(Number);
        return h * 60 + m;
    }

    function getOnAirMelody(onAirTime, melody) {
        return melody.repeat(Math.floor(onAirTime / melody.length) + 1).slice(0, onAirTime);
    }

    m = removeSharp(m);
    const matches = [];
    for (const [idx, musicinfo] of musicinfos.entries()) {
        const [st, ed, title, melody] = musicinfo.split(",");
        const onAirTime = timeToMin(ed) - timeToMin(st);
        if (onAirTime === 0) continue;
        const onAirMelody = getOnAirMelody(onAirTime, removeSharp(melody));
        if (onAirMelody.includes(m)) {
            matches.push([-onAirTime, idx, title]);
        }
    }
    matches.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    return matches.length ? matches[0][2] : "(None)";
}


const inputDatas = [
    {data: ["ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]], answer: "HELLO"},
    {data: ["CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]], answer: "FOO"},
    {data: ["ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]], answer: "WORLD"}
];

/*
2018 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 9,759명, 정답률 49%
파이썬이랑 같은 방식으로 해결했다.
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
