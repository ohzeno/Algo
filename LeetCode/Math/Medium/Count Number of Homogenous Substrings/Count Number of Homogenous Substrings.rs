// https://leetcode.com/problems/count-number-of-homogenous-substrings/
struct Solution;

/*
constraints:
  • 1 <= s.length <= 10^5
  • s consists of lowercase letters.
*/

impl Solution {
    pub fn count_homogenous(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut tot: i64 = 1;
        let mut n: i64 = 1;
        let bytes = s.as_bytes();
        for i in 1..bytes.len() {
            if bytes[i] == bytes[i - 1] {
                n += 1;
            } else {
                n = 1;
            }
            tot = (tot + n) % MOD;
        }
        return tot as i32;
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
        Solution::count_homogenous,
        [
            {data: ("abbcccaa".to_string()), answer: 13},
            {data: ("xy".to_string()), answer: 2},
            {data: ("zzzzz".to_string()), answer: 15}
        ]
    );
}

/*
LeetCode Medium.
제출 228.8K, 정답률 57.4%
1e9같은 지수표기법은 정수타입에 사용할 수 없음
*/
