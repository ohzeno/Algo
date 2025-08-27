// https://www.acmicpc.net/problem/30805
const realFile = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const realCodeLines = require("fs").readFileSync(realFile).toString().trim().split("\n");
let realCodeLineIdx = 0;
const input = () => realCodeLines[realCodeLineIdx++];
/*
constraints:
*/



/*
현 시점 Gold IV. 제출 7226. 정답률 31.680 %
*/
