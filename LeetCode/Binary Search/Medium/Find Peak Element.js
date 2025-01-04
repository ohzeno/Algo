// https://leetcode.com/problems/find-peak-element/

/*
constraints:
  1 <= nums.length <= 1000
  -2^31 <= nums[i] <= 2^31 - 1
  nums[i] != nums[i + 1] for all valid i.
*/


/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    let ll = 0, rr = nums.length - 1;
    while (ll < rr) {
        let mid = Math.floor((ll + rr) / 2);
        if (nums[mid] > nums[mid + 1]) {
            rr = mid;
        } else {
            ll = mid + 1;
        }
    }
    return ll;
};


const inputDatas = [
    {"data": [[1,2,3,1]], "answer": 2},
    {"data": [[1,2,1,3,5,6,4]], "answer": 5},
    {"data": [[1]], "answer": 0},
];

/*
LeetCode Medium.
제출 3.7M, 정답률 46.2%
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = findPeakElement(...data);
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
