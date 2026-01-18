// https://leetcode.com/problems/daily-temperatures/
struct Solution;

/*
constraints:
  • 1 <= temperatures.length <= 10^5
  • 30 <= temperatures[i] <= 100
*/

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n = temperatures.len();
        let mut answer = vec![0; n];
        let mut stack: Vec<(i32, usize)> = Vec::new();
        for i in (0..n).rev() {
            let cur_temp = temperatures[i];
            while !stack.is_empty() && stack.last().unwrap().0 <= cur_temp {
                stack.pop();
            }
            if !stack.is_empty() {
                answer[i] = (stack.last().unwrap().1 - i) as i32;
            }
            stack.push((cur_temp, i));
        }
        return answer;
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

fn main() {
    run_judge!(
        Solution::daily_temperatures,
        [
            {data: (vec![73, 74, 75, 71, 69, 72, 76, 73]), answer: vec![1, 1, 4, 2, 1, 1, 0, 0]},
            {data: (vec![30, 40, 50, 60]), answer: vec![1, 1, 1, 0]},
            {data: (vec![30, 60, 90]), answer: vec![1, 1, 0]}
        ]
    );
}

/*
LeetCode Medium.
제출 2.3M, 정답률 68.1%
*/
