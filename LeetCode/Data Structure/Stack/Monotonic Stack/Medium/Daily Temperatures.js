// https://leetcode.com/problems/daily-temperatures/

/*
constraints:
  • 1 <= temperatures.length <= 10^5
  • 30 <= temperatures[i] <= 100
*/

/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
    const n = temperatures.length;
    const answer = Array(n).fill(0);
    const stack = [];
    for (let i = n - 1; i >= 0; i--) {
        const curTemp = temperatures[i];
        while (stack.length && stack[stack.length - 1][0] <= curTemp) {
            stack.pop();
        }
        if (stack.length) {
            answer[i] = stack[stack.length - 1][1] - i;
        }
        stack.push([curTemp, i]);
    }
    return answer;
};

const inputDatas = [
    {
        data: [[73, 74, 75, 71, 69, 72, 76, 73]],
        answer: [1, 1, 4, 2, 1, 1, 0, 0],
    },
    { data: [[30, 40, 50, 60]], answer: [1, 1, 1, 0] },
    { data: [[30, 60, 90]], answer: [1, 1, 0] },
];

/*
LeetCode Medium.
제출 2.3M, 정답률 68.1%
*/

for (let i = 0; i < inputDatas.length; i++) {
    const { data, answer } = inputDatas[i];
    const res = dailyTemperatures(...data);
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
