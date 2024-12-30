// https://leetcode.com/problems/powx-n/

/*
constraints:
  -100.0 < x < 100.0
  -2^31 <= n <= 2^31-1
  n is an integer.
  Either x is not zero or n > 0.
  -10^4 <= x^n <= 10^4
*/


/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    function fastPow(base, exp) {
        if (exp === 0) return 1;
        const half = fastPow(base, Math.floor(exp / 2));
        if (exp % 2 === 0) return Math.pow(half, 2);
        return base * Math.pow(half, 2);
    }
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    return Number(fastPow(x, n).toFixed(5));
};


const inputDatas = [
    {"data": [2.00000, 10], "answer": 1024.00000},
    {"data": [2.10000, 3], "answer": 9.26100},
    {"data": [2.00000, -2], "answer": 0.25000}
];

/*
LeetCode Medium.
제출 , 정답률 36.1%
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = myPow(...data);
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
