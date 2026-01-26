// https://leetcode.com/problems/search-suggestions-system/

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

class Node {
    constructor() {
        this.children = {};
        this.suggestions = [];
    }
}

class Trie {
    constructor() {
        this.root = new Node();
    }

    insert(product) {
        let cur = this.root;
        for (let c of product) {
            if (!(c in cur.children))
                cur.children[c] = new Node();
            cur = cur.children[c];
            if (cur.suggestions.length < 3)
                cur.suggestions.push(product);
        }
    }
}

/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
var suggestedProducts = function(products, searchWord) {
    products.sort();
    const trie = new Trie();
    for (let product of products) {
        trie.insert(product);
    }
    const result = [];
    let cur = trie.root;
    for (let c of searchWord) {
        if (cur && c in cur.children) {
            cur = cur.children[c];
            result.push(cur.suggestions);
        } else {
            cur = null;
            result.push([]);
        }
    }
    return result;
};


const inputDatas = [
    {data: [["mobile","mouse","moneypot","monitor","mousepad"], "mouse"], answer: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]},
    {data: [["havana"], "havana"], answer: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]},
    {data: [["havana"], "tatiana"], answer: [[], [], [], [], [], [], []]}
];

/*
LeetCode Medium.
제출 657.6K, 정답률 65.1%
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = suggestedProducts(...data);
    if (JSON.stringify(res) === JSON.stringify(answer)) {
        console.log("pass");
    } else {
        let summary = "fail";
        for (const [label, content] of [["expected:", answer], ["got:", res]]) {
            summary += `\n  ${label}\n`;
            summary += `    ${content}`;
            summary = summary.trimEnd();
        }
        console.log(summary);
    }
}
