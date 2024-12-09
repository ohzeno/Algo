// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

/*
constraints:
*/


/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] > prices[i - 1]) {
            profit += prices[i] - prices[i - 1];
        }
    }
    return profit;
};


const inputDatas = [
    {"data": [[7, 1, 5, 3, 6, 4]], "answer": 7},
    {"data": [[1, 2, 3, 4, 5]], "answer": 4},
    {"data": [[7, 6, 4, 3, 1]], "answer": 0},
    {"data": [[1, 3, 2, 1, 4]], "answer": 5},
];

/*
LeetCode Medium.
제출 3.2M, 정답률 67.8%
그리디 풀이.
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