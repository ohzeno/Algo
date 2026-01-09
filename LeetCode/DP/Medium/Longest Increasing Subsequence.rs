// https://leetcode.com/problems/longest-increasing-subsequence/
struct Solution;

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = vec![1; n];
        for b in 1..n {
            for a in 0..b {
                if nums[a] < nums[b] {
                    dp[b] = dp[b].max(dp[a] + 1);
                }
            }
        }
        return *dp.iter().max().unwrap()
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
                    summary.push_str(&format!("\n  {}\n", label));
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
        Solution::length_of_lis,
        [
            {data: (vec![10, 9, 2, 5, 3, 7, 101, 18]), answer: 4},
            {data: (vec![0, 1, 0, 3, 2, 3]), answer: 4},
            {data: (vec![7, 7, 7, 7, 7, 7, 7]), answer: 1},
        ]
    );
}

/*
LeetCode Medium.
제출 4.2M, 정답률 58.8%
rust 첫 알고리즘 풀이.
아직 양식이나 풀이 매크로 확정 아님.
*/