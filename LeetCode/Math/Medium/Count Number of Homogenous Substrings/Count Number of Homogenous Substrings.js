// https://leetcode.com/problems/count-number-of-homogenous-substrings/

/*
constraints:
  • 1 <= s.length <= 10^5
  • s consists of lowercase letters.
*/


/**
 * @param {string} s
 * @return {number}
 */
var countHomogenous = function(s) {
    const MOD = 1e9 + 7;
    let tot = 1;
    let n = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1])
            n += 1;
        else
            n = 1;
        tot = (tot + n) % MOD;
    }
    return tot;
};


const inputDatas = [
    {data: ["abbcccaa"], answer: 13},
    {data: ["xy"], answer: 2},
    {data: ["zzzzz"], answer: 15}
];

/*
LeetCode Medium.
제출 228.8K, 정답률 57.4%
파이썬에선 1e9를 그대로 사용하면 float연산으로 부동소수점 문제가 생긴다.
js는 모든 숫자가 기본적으로 64-bit float이라 2^53-1까지는 부동소수점 문제가 없다.
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = countHomogenous(...data);
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
