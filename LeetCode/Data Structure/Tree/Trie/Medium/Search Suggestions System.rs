// https://leetcode.com/problems/search-suggestions-system/
struct Solution;

/*
constraints:
  • 1 <= products.length <= 1000
  • 1 <= products[i].length <= 3000
  • 1 <= sum(products[i].length) <= 2 * 10^4
  • All the strings of products are unique.
  • products[i] consists of lowercase English letters.
  • 1 <= searchWord.length <= 1000
  • searchWord consists of lowercase English letters.
*/
use std::collections::HashMap;

struct Node {
    children: HashMap<char, Node>,
    suggestions: Vec<String>,
}

impl Node {
    fn new() -> Self {
        Node {
            children: HashMap::new(),
            suggestions: Vec::new(),
        }
    }
}

struct Trie {
    root: Node,
}

impl Trie {
    fn new() -> Self {
        Trie { root: Node::new() }
    }

    fn insert(&mut self, product: String) {
        let mut cur = &mut self.root;
        for c in product.chars() {
            cur = cur.children.entry(c).or_insert_with(Node::new);
            if cur.suggestions.len() < 3 {
                cur.suggestions.push(product.clone());
            }
        }
    }
}

impl Solution {
    pub fn suggested_products(products: Vec<String>, search_word: String) -> Vec<Vec<String>> {
        let mut products = products;
        products.sort();
        let mut trie = Trie::new();
        for product in products {
            trie.insert(product);
        }
        let mut result = Vec::new();
        let mut cur = Some(&trie.root);
        for c in search_word.chars() {
            if let Some(node) = cur
                && let Some(child) = node.children.get(&c)
            {
                cur = Some(child);
                result.push(child.suggestions.clone());
            } else {
                cur = None;
                result.push(Vec::new());
            }
        }
        return result;
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

macro_rules! svec {
    ($($x:expr),* $(,)?) => {
        vec![$($x.to_string()),*]
    };
}

fn main() {
    run_judge!(
        Solution::suggested_products,
        [
            {data: (svec!["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse".to_string()), answer: vec![svec!["mobile", "moneypot", "monitor"], svec!["mobile", "moneypot", "monitor"], svec!["mouse", "mousepad"], svec!["mouse", "mousepad"], svec!["mouse", "mousepad"]]},
            {data: (svec!["havana"], "havana".to_string()), answer: vec![svec!["havana"], svec!["havana"], svec!["havana"], svec!["havana"], svec!["havana"], svec!["havana"]]},
            {data: (svec!["havana"], "tatiana".to_string()), answer: vec![vec![]; 7]}
        ]
    );
}

/*
LeetCode Medium.
제출 657.7K, 정답률 65.1%
Rust가 Python을 대체할거라는 강력한 주장을 봤었는데,
그렇게 보기엔 직관성이 심각하게 떨어지는 것 같다.
if문 하나 작성하다가 Rust 공부 포기하고 Go나 할까 고민했다.
저 if문도 여러번 갈아엎어서 가장 직관적으로 작성한 것이다.
*/
