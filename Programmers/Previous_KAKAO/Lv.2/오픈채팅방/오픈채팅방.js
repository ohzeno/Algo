// https://school.programmers.co.kr/learn/courses/30/lessons/42888?language=javascript

/*
constraints:
  • record는 다음과 같은 문자열이 담긴 배열이며, 길이는 1 이상 100,000 이하이다.
  • 다음은 record에 담긴 문자열에 대한 설명이다.
    ◦ 모든 유저는 [유저 아이디]로 구분한다.
    ◦ [유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - "Enter [유저 아이디] [닉네임]" (ex. "Enter uid1234 Muzi")
    ◦ [유저 아이디] 사용자가 채팅방에서 퇴장 - "Leave [유저 아이디]" (ex. "Leave uid1234")
    ◦ [유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - "Change [유저 아이디] [닉네임]" (ex. "Change uid1234 Muzi")
    ◦ 첫 단어는 Enter, Leave, Change 중 하나이다.
    ◦ 각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
    ◦ 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
    ◦ 유저 아이디와 닉네임의 길이는 1 이상 10 이하이다.
    ◦ 채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.
*/

function solution(record) {
    const nick = {};
    const message = [];

    function logging(uid, order) {
        const action = order === "Enter" ? "들어왔" : "나갔";
        return `${nick[uid]}님이 ${action}습니다.`;
    }

    for (const rec of record) {
        const [order, uid, nickname] = rec.split(" ");
        if (nickname) nick[uid] = nickname;
        if (order !== "Change") message.push([uid, order]);
    }
    return message.map(([uid, order]) => logging(uid, order));
}

const inputDatas = [
    {
        data: [
            [
                "Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan",
            ],
        ],
        answer: [
            "Prodo님이 들어왔습니다.",
            "Ryan님이 들어왔습니다.",
            "Prodo님이 나갔습니다.",
            "Prodo님이 들어왔습니다.",
        ],
    },
];

/*
2019 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 33,273명, 정답률 58%
파이썬 풀이의 일괄처리 버전으로 풀었다.
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
