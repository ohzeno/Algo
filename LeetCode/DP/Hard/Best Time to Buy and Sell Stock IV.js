// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

/*
constraints:
  1 <= k <= 100
  1 <= prices.length <= 1000
  0 <= prices[i] <= 1000
*/

/**
 * @param {number} k
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(k, prices) {
    const n = prices.length;
    const dp = Array.from({ length: n }, () =>
        Array.from({ length: k+1 }, () => Array(2).fill(0)),
    );
    dp[0][1][1] = -prices[0];
    for (let b = 1; b < k+1; b++) {
        dp[0][b][0] = -Infinity;
        if (b > 1) dp[0][b][1] = -Infinity;
    }
    for (let t = 1; t < n; t++) {
        for (let d = 1; d < k+1; d++) {
            dp[t][d][0] = Math.max(dp[t-1][d][0], dp[t-1][d][1] + prices[t]);
            dp[t][d][1] = Math.max(dp[t-1][d][1], dp[t-1][d-1][0] - prices[t]);
        }
    }
    return Math.max(...Array(k + 1).fill().map((_, i) => dp[n-1][i][0]));
};

const inputDatas = [
    {"data": [2, [2, 4, 1]], "answer": 2},
    {"data": [2, [3, 2, 6, 5, 0, 3]], "answer": 7}
];

/*
LeetCode Hard.
제출 1.1M, 정답률 44.7%
3과 같은 로직으로 풀었다.
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
