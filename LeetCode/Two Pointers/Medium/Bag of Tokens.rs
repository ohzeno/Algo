// https://leetcode.com/problems/bag-of-tokens/
struct Solution;

/*
constraints:
  • 0 <= tokens.length <= 1000
  • 0 <= tokens[i], power < 10^4
*/

impl Solution {
    pub fn bag_of_tokens_score(tokens: Vec<i32>, power: i32) -> i32 {
        let mut tokens = tokens;
        tokens.sort();
        // rr이 usize라 음수가 되면 언더플로우 발생하니 빈 배열 처리 필요
        if tokens.is_empty() {
            return 0;
        }
        let (mut score, mut power) = (0, power);
        let (mut ll, mut rr) = (0, tokens.len() - 1);
        while ll <= rr {
            if power >= tokens[ll] {
                power -= tokens[ll];
                score += 1;
                ll += 1;
            } else if score >= 1 && ll < rr {
                power += tokens[rr];
                score -= 1;
                rr -= 1;
            } else {
                break;
            }
        }
        return score;
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
        Solution::bag_of_tokens_score,
        [
            {data: (vec![], 85), answer: 0},
            {data: (vec![100], 50), answer: 0},
            {data: (vec![200, 100], 150), answer: 1},
            {data: (vec![100, 200, 300, 400], 200), answer: 2}
        ]
    );
}

/*
LeetCode Medium.
제출 441K, 정답률 59.5%
usize가 상당히 어색하다.
js, py 쓰다가 usize 언더플로우 신경쓰려니 불편함.
*/
