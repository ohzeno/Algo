// https://leetcode.com/problems/exclusive-time-of-functions/
struct Solution;

/*
constraints:
  • 1 <= n <= 100
  • 2 <= logs.length <= 500
  • 0 <= function_id < n
  • 0 <= timestamp <= 10^9
  • No two start events will happen at the same timestamp.
  • No two end events will happen at the same timestamp.
  • Each function has an "end" log for each "start" log.
*/

impl Solution {
    pub fn exclusive_time(n: i32, logs: Vec<String>) -> Vec<i32> {
        let mut stack: Vec<[i32; 2]> = Vec::new();
        let mut exc_time = vec![0; n as usize];

        for log in logs {
            let parts: Vec<&str> = log.split(':').collect();
            let (idx, typ, time) = (parts[0], parts[1], parts[2]);
            let (idx, time) = (idx.parse::<i32>().unwrap(), time.parse::<i32>().unwrap());
            if typ == "start" {
                if stack.len() > 0 {
                    let [p_idx, p_st] = *stack.last().unwrap();
                    let duration = time - p_st;
                    exc_time[p_idx as usize] += duration;
                }
                stack.push([idx, time]);
            } else {
                let [p_idx, p_st] = stack.pop().unwrap();
                let duration = time + 1 - p_st;
                exc_time[p_idx as usize] += duration;
                if stack.len() > 0 {
                    let last_idx = stack.len() - 1;
                    stack[last_idx] = [stack[last_idx][0], time + 1];
                }
            }
        }
        return exc_time;
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
            {data: (2, svec!["0:start:0", "1:start:2", "1:end:5", "0:end:6"]), answer: vec![3, 4]},
            {data: (1, svec!["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]), answer: vec![8]},
            {data: (2, svec!["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]), answer: vec![7, 1]}
        ]
    );
}

/*
LeetCode Medium.
제출 507.6K, 정답률 66.1%
*/
