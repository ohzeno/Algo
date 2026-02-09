// https://leetcode.com/problems/exclusive-time-of-functions/
struct Solution;

/*
constraints:
*/

impl Solution {
    pub fn exclusive_time(n: i32, logs: Vec<String>) -> Vec<i32> {
        return vec![];
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
        Solution::exclusive_time,
        [
            {data: (,), answer: vec![]},
            {data: (,), answer: vec![]},
            {data: (,), answer: vec![]}
        ]
    );
}

/*
LeetCode Medium.
제출 507.6K, 정답률 66.1%
*/
