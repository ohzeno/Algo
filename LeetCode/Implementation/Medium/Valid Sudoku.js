// https://leetcode.com/problems/valid-sudoku/

/*
constraints:
  • board.length == 9
  • board[i].length == 9
  • board[i][j] is a digit 1-9 or '.'.
*/

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
    function checkBlock(r, c) {
        const seen = new Set();
        for (let i = r; i < r + 3; i++) {
            for (let j = c; j < c + 3; j++) {
                const val = board[i][j];
                if (val !== ".") {
                    if (seen.has(val)) return false;
                    seen.add(val);
                }
            }
        }
        return true;
    }

    function rowCheck(r, c) {
        const seen = new Set();
        for (let i = 0; i < 9; i++) {
            const val = board[r][i];
            if (val !== ".") {
                if (seen.has(val)) return false;
                seen.add(val);
            }
        }
        return true;
    }

    function colCheck(r, c) {
        const seen = new Set();
        for (let i = 0; i < 9; i++) {
            const val = board[i][c];
            if (val !== ".") {
                if (seen.has(val)) return false;
                seen.add(val);
            }
        }
        return true;
    }

    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            if (r % 3 === 0 && c % 3 === 0) {
                if (!checkBlock(r, c)) return false;
            }
            if (c === 0) {
                if (!rowCheck(r, c)) return false;
            }
            if (r === 0) {
                if (!colCheck(r, c)) return false;
            }
        }
    }
    return true;
};

const inputDatas = [
    {
        data: [
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
        ],
        answer: true,
    },
    {
        data: [
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
        ],
        answer: false,
    },
];

/*
LeetCode Medium.
제출 3.7M, 정답률 64.0%
*/

for (let i = 0; i < inputDatas.length; i++) {
    const { data, answer } = inputDatas[i];
    const res = isValidSudoku(...data);
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
