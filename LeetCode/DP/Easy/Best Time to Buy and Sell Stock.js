// https://leetcode.com/problems/count-number-of-nice-subarrays/

/*
constraints:
*/


/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    const leng = prices.length;
    const dp = Array(leng).fill(0)
    for (let i = 1; i < leng; i++) {
        dp[i] = Math.max(dp[i-1] + prices[i] - prices[i-1], 0);
    }
    return Math.max(...dp);
};


const inputDatas = [
    {data: [[7,1,5,3,6,4]], answer: 5},
    {data: [[7,6,4,3,1]], answer: 0},
];

/*
LeetCode Easy.
제출 9.8M, 정답률 54.2%
dp[i]는 i번째 날까지 얻을 수 있는 최대 이익.
Math.max의 첫 인자는 i-1 최대이익에 i번째 날 이익을 더한 값,
두번째 인자는 0으로 둬서 마이너스 대비(안사는 경우)
i-1만 체크하기 때문에 이전에 한번 사고 판 수익을 참조해서 두번 이상 사고파는 경우는 생기지 않음.
파이썬 풀이를 그대로 사용했다. dp연습중.
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = maxProfit(...data);
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