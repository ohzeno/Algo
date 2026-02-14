// https://leetcode.com/problems/bag-of-tokens/

/*
constraints:
  • 0 <= tokens.length <= 1000
  • 0 <= tokens[i], power < 10^4
*/


/**
 * @param {number[]} tokens
 * @param {number} power
 * @return {number}
 */
var bagOfTokensScore = function(tokens, power) {
    tokens.sort()
    let ll = 0, rr = tokens.length - 1;
    let score = 0;
    while (ll <= rr) {
        if (power >= tokens[ll]) {
            power -= tokens[ll];
            score += 1;
            ll += 1;
        } else if (score >= 1 && ll < rr) {
            power += tokens[rr];
            score -= 1;
            rr -= 1;
        } else {
            break;
        }
    }
    return score;
};


const inputDatas = [
    {data: [[100], 50], answer: 0},
    {data: [[200,100], 150], answer: 1},
    {data: [[100,200,300,400], 200], answer: 2}
];

/*
LeetCode Medium.
제출 441K, 정답률 59.5%
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = bagOfTokensScore(...data);
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
