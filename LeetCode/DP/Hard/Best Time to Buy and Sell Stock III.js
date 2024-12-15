// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

/*
constraints:
*/

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    const n = prices.length;
    const dp = Array.from({ length: n }, () =>
        Array.from({ length: 3 }, () => Array(2).fill(0)),
    );
    dp[0][1][1] = -prices[0];
    dp[0][1][0] = dp[0][2][0] = dp[0][2][1] = -Infinity;
    for (let i = 1; i < n; i++) {
        for (let j = 1; j <= 2; j++) {
            dp[i][j][0] = Math.max(dp[i-1][j][0], dp[i-1][j][1] + prices[i]);
            dp[i][j][1] = Math.max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i]);
        }
    }
    return Math.max(dp[n-1][0][0], dp[n-1][1][0], dp[n-1][2][0]);
};

const inputDatas = [
    { data: [[3, 3, 5, 0, 0, 3, 1, 4]], answer: 6 },
    { data: [[1, 2, 3, 4, 5]], answer: 4 },
    { data: [[7, 6, 4, 3, 1]], answer: 0 },
];

/*
LeetCode Hard.
제출 1.4M, 정답률 49.3%
이건 오히려 dp가 이해하기 편한듯.
return 부분을 Math.max(...dp[n-1].map(x => x[0]))으로 바꿨다가
직관성이 떨어지는 것 같아서 다시 바꿨다.
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
