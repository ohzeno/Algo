// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

/*
constraints:
*/

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    const n = prices.length;
    const dp = Array(n)
        .fill()
        .map(() => Array(2).fill(0));
    dp[0][0] = 0;
    dp[0][1] = -prices[0];
    for (let i = 1; i < n; i++) {
        dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
        dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
    }
    return dp[n - 1][0];
};

const inputDatas = [
    { data: [[7, 1, 5, 3, 6, 4]], answer: 7 },
    { data: [[1, 2, 3, 4, 5]], answer: 4 },
    { data: [[7, 6, 4, 3, 1]], answer: 0 },
    { data: [[1, 3, 2, 1, 4]], answer: 5 },
];

/*
LeetCode Medium.
제출 3.2M, 정답률 67.8%
그리디 풀이 후에 dp도 연습해봤다.
*/

for (let i = 0; i < inputDatas.length; i++) {
    const { data, answer } = inputDatas[i];
    const res = maxProfit(...data);
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
