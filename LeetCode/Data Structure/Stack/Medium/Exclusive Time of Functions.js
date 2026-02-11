// https://leetcode.com/problems/exclusive-time-of-functions/

/*
constraints:
  • 1 <= n <= 100
  • 2 <= logs.length <= 500
  • 0 <= function_id < n
  • 0 <= timestamp <= 10^9
  • No two start events will happen at the same timestamp.
  • No two end events will happen at the same timestamp.
  • Each function has an "end" log for each "start" log.
*/


/**
 * @param {number} n
 * @param {string[]} logs
 * @return {number[]}
 */
var exclusiveTime = function(n, logs) {
    const stack = [];
    const exc_time = new Array(n).fill(0);
    for (const log of logs) {
        let [idx, typ, time] = log.split(":");
        [idx, time] = [idx, time].map(Number);
        if (typ === "start") {
            if (stack.length) {
                const [p_idx, p_st] = stack[stack.length - 1];
                const duration = time - p_st;
                exc_time[p_idx] += duration;
            }
            stack.push([idx, time]);
        } else {
            const [p_idx, p_st] = stack.pop();
            const duration = time + 1 - p_st;
            exc_time[p_idx] += duration;
            const arrayIdx = stack.length - 1;
            if (stack.length)
                stack[arrayIdx] = [stack[arrayIdx][0], time + 1];
        }
    }
    return exc_time;
};


const inputDatas = [
    {data: [2, ["0:start:0","1:start:2","1:end:5","0:end:6"]], answer: [3,4]},
    {data: [1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]], answer: [8]},
    {data: [2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]], answer: [7,1]}
];

/*
LeetCode Medium.
제출 507.6K, 정답률 66.1%
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = exclusiveTime(...data);
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
