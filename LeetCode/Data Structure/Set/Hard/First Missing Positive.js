// https://leetcode.com/problems/first-missing-positive/

/*
constraints:
  1 <= nums.length <= 10^5
  -2^31 <= nums[i] <= 2^31 - 1
*/


/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
    const numsSet = new Set(nums);
    for (let i = 1; i <= nums.length + 1; i++) {
        if (!numsSet.has(i)) return i;
    }
};


const inputDatas = [
    {"data": [[1,2,0]], "answer": 3},
    {"data": [[3,4,-1,1]], "answer": 2},
    {"data": [[7,8,9,11,12]], "answer": 1}
];

/*
LeetCode Hard.
제출 3.3M, 정답률 40.3%
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = firstMissingPositive(...data);
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
