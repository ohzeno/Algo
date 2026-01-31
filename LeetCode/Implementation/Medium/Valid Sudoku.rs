// https://leetcode.com/problems/valid-sudoku/
struct Solution;
use std::collections::HashSet;

/*
constraints:
  • board.length == 9
  • board[i].length == 9
  • board[i][j] is a digit 1-9 or '.'.
*/

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let check_block = |r: usize, c: usize| -> bool {
            let mut seen = HashSet::new();
            for i in r..r + 3 {
                for j in c..c + 3 {
                    let val = board[i][j];
                    if val != '.' {
                        if seen.contains(&val) {
                            return false;
                        }
                        seen.insert(val);
                    }
                }
            }
            return true;
        };

        let row_check = |r: usize, _c: usize| -> bool {
            let mut seen = HashSet::new();
            for i in 0..9 {
                let val = board[r][i];
                if val != '.' {
                    if seen.contains(&val) {
                        return false;
                    }
                    seen.insert(val);
                }
            }
            return true;
        };

        let col_check = |_r: usize, c: usize| -> bool {
            let mut seen = HashSet::new();
            for i in 0..9 {
                let val = board[i][c];
                if val != '.' {
                    if seen.contains(&val) {
                        return false;
                    }
                    seen.insert(val);
                }
            }
            return true;
        };

        for r in 0..9 {
            for c in 0..9 {
                if r % 3 == 0 && c % 3 == 0 {
                    if !check_block(r, c) {
                        return false;
                    }
                }
                if c == 0 {
                    if !row_check(r, c) {
                        return false;
                    }
                }
                if r == 0 {
                    if !col_check(r, c) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}

#[macro_export]
macro_rules! run_judge {
    (
        $func:path,
        [ $( { data: ( $($arg:expr),* ), answer: $ans:expr } ),* $(,)? ]
    ) => {
        $(
            let result = $func($($arg),*);
            let expected = $ans;
            if result == expected {
                println!("pass");
            } else {
                let mut summary = String::from("fail");
                for (label, content) in [("expected:", &expected), ("got:", &result)] {
                    summary.push_str(&format!("
  {}
", label));
                    summary.push_str(&format!("    {:?}", content));
                }
                summary = summary.trim_end().to_string();
                println!("{}", summary);
            }
        )*
    };
}

#[allow(unused_macros)]
macro_rules! svec {
    ($($x:expr),* $(,)?) => {
        vec![$($x.to_string()),*]
    };
}

fn main() {
    run_judge!(
        Solution::is_valid_sudoku,
        [
            {data: (vec![vec!['5', '3', '.', '.', '7', '.', '.', '.', '.'], vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'], vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'], vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'], vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'], vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'], vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'], vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'], vec!['.', '.', '.', '.', '8', '.', '.', '7', '9']]), answer: true},
            {data: (vec![vec!['8', '3', '.', '.', '7', '.', '.', '.', '.'], vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'], vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'], vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'], vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'], vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'], vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'], vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'], vec!['.', '.', '.', '.', '8', '.', '.', '7', '9']]), answer: false}
        ]
    );
}

/*
LeetCode Medium.
제출 3.7M, 정답률 64.0%
러스트는 사용하지 않는 변수에 경고를 표시해서 인자에 _추가.
러스트 fn은 상위 스코프의 변수를 참조할 수 없어서 클로저로 작성.
아직은 문법이 익숙하지 않다. 몇백문제 풀어야 좀 익숙해질듯.
*/
