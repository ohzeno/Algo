// https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=javascript

/*
constraints:
  • lottos는 길이 6인 정수 배열입니다.
  • lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
    ◦ 0은 알아볼 수 없는 숫자를 의미합니다.
    ◦ 0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
    ◦ lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
  • win_nums은 길이 6인 정수 배열입니다.
  • win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
    ◦ win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
    ◦ win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다.
*/

function solution(lottos, win_nums) {
    const winNums = new Set(win_nums);
    const matches = lottos.filter((e) => winNums.has(e)).length;
    const ans = [matches + lottos.filter((e) => e === 0).length, matches];
    for (const [i, v] of ans.entries()) {
        ans[i] = v < 2 ? 6 : 7 - v;
    }
    return ans;
}

const inputDatas = [
    {
        data: [
            [44, 1, 0, 0, 31, 25],
            [31, 10, 45, 1, 6, 19],
        ],
        answer: [3, 5],
    },
    {
        data: [
            [0, 0, 0, 0, 0, 0],
            [38, 19, 20, 40, 15, 25],
        ],
        answer: [1, 6],
    },
    {
        data: [
            [45, 4, 35, 20, 3, 9],
            [20, 9, 3, 45, 4, 35],
        ],
        answer: [1, 1],
    },
];

/*
2021 Dev-Matching: 웹 백엔드 개발자(상반기)
Lv.1. 현 시점 완료한 사람 45,743명, 정답률 59%
파이썬과 달리 Intersection 연산이 없어서 filter를 사용할 수 밖에 없었다.
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
