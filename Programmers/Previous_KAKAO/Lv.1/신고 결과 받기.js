// https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=javascript

/*
constraints:
  • 2 ≤ id_list의 길이 ≤ 1,000
    ◦ 1 ≤ id_list의 원소 길이 ≤ 10
    ◦ id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
    ◦ id_list에는 같은 아이디가 중복해서 들어있지 않습니다.
  • 1 ≤ report의 길이 ≤ 200,000
    ◦ 3 ≤ report의 원소 길이 ≤ 21
    ◦ report의 원소는 "이용자id 신고한id"형태의 문자열입니다.
    ◦ 예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
    ◦ id는 알파벳 소문자로만 이루어져 있습니다.
    ◦ 이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
    ◦ 자기 자신을 신고하는 경우는 없습니다.
  • 1 ≤ k ≤ 200, k는 자연수입니다.
  • return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.
*/

function solution(id_list, report, k) {
    const user_d = {};
    for (const user of id_list) {
        user_d[user] = { mailed: 0, reported_by: [] };
    }
    for (const r of new Set(report)) {
        const [reporter, reported] = r.split(" ");
        user_d[reported].reported_by.push(reporter);
    }
    for (const user of Object.values(user_d)) {
        if (user.reported_by.length >= k) {
            for (const reporter of user.reported_by) {
                user_d[reporter].mailed += 1;
            }
        }
    }
    return id_list.map((user) => user_d[user].mailed);
}

const inputDatas = [
    {
        data: [
            ["muzi", "frodo", "apeach", "neo"],
            [
                "muzi frodo",
                "apeach frodo",
                "frodo neo",
                "muzi neo",
                "apeach muzi",
            ],
            2,
        ],
        answer: [2, 1, 1, 0],
    },
    {
        data: [
            ["con", "ryan"],
            ["ryan con", "ryan con", "ryan con", "ryan con"],
            3,
        ],
        answer: [0, 0],
    },
];

/*
2022 KAKAO BLIND RECRUITMENT
Lv.1. 현 시점 완료한 사람 34,278명, 정답률 39%
파이썬과 같은 로직. 딕셔너리 컴프리헨션이 없어서 좀 불편하다.
물론 Map과 map을 사용할 수 있지만 직관성이 떨어진다.
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
