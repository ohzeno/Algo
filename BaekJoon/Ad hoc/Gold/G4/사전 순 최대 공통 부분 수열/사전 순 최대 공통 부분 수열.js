// https://www.acmicpc.net/problem/30805
const file = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const lines = require('fs').readFileSync(file).toString().trim().split('\n');
let lineIdx = 0;
const input = () => lines[lineIdx++];

/*
constraints:
*/


function find(pA, pB) {
    let aStN = 0
    const bD = {}
    for (let i = pB; i < m; i++)
        (bD[B[i]] = bD[B[i]] || []).push(i)
    let aStI, bStI
    for (let i = pA; i < n; i++) {
        let a = A[i]
        if ((a <= aStN) || !(a in bD))
            continue
        aStI = i
        aStN = a
        bStI = Math.min(...bD[a])
    }
    return aStN ? [aStN].concat(find(aStI + 1, bStI + 1)) : []
}

const n = parseInt(input())
const A = input().split(' ').map(x => parseInt(x));
const m = parseInt(input())
const B = input().split(' ').map(x => parseInt(x));
const res = find(0, 0)
const k = res.length
console.log(k)
if (k > 0)
    console.log(...res)


/*
현 시점 Gold IV. 제출 7226. 정답률 31.680 %
백준에선 js를 처음으로 풀어봤다.
양식이 릿코드나 프로그래머스와 달라서 수정할 유틸 함수들이 많다.
*/