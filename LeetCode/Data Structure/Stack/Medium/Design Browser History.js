// https://leetcode.com/problems/design-browser-history/

/*
constraints:
  • 1 <= homepage.length <= 20
  • 1 <= url.length <= 20
  • 1 <= steps <= 100
  • homepage and url consist of '.' or lower case English letters.
  • At most 5000 calls will be made to visit, back, and forward.
*/


class BrowserHistory {
    constructor(homepage) {
        this.url = homepage;
        this.back_history = [];
        this.forward_history = [];
    }

    visit(url) {
        this.back_history.push(this.url);
        this.forward_history = []
        this.url = url;
    }

    back(steps) {
        for (let i = 0; i < steps; i++) {
            if (this.back_history.length === 0) break;
            this.forward_history.push(this.url);
            this.url = this.back_history.pop();
        }
        return this.url;
    }

    forward(steps) {
        for (let i = 0; i < steps; i++) {
            if (this.forward_history.length === 0) break;
            this.back_history.push(this.url);
            this.url = this.forward_history.pop();
        }
        return this.url;
    }
}


const inputDatas = [
    {
        input: {
            cmds: [
                "BrowserHistory",
                "visit",
                "visit",
                "visit",
                "back",
                "back",
                "forward",
                "visit",
                "forward",
                "back",
                "back",
            ],
            url_or_n: [
                ["leetcode.com"],
                ["google.com"],
                ["facebook.com"],
                ["youtube.com"],
                [1],
                [1],
                [1],
                ["linkedin.com"],
                [2],
                [2],
                [7],
            ],
        },
        answer: [
            undefined,
            undefined,
            undefined,
            undefined,
            "facebook.com",
            "google.com",
            "facebook.com",
            undefined,
            "linkedin.com",
            "google.com",
            "leetcode.com",
        ],
    },
];

/*
LeetCode Medium.
제출 357.8K, 정답률 78.0%
js로 풀려고 보니 무려 prototype으로 클래스를 구현했다.
릿코드 js 업데이트 안하나...?
*/

function grading(res, ans) {
    if (res === ans) {
        console.log("pass");
    } else {
        let summary = "fail";
        for (const [label, content] of [
            ["expected:", ans],
            ["got:", res],
        ]) {
            summary += `\n  ${label}\n`;
            summary += `    ${content}`;
            summary = summary.trimEnd();
        }
        console.log(summary);
    }
}

for (const inputdata of inputDatas) {
    const { input, answer } = inputdata;
    const { cmds, url_or_n } = input;
    const obj = new BrowserHistory(...url_or_n[0]);

    // Python의 zip 함수 대신 인덱스 기반 루프 사용
    for (let i = 1; i < cmds.length; i++) {
        const cmd = cmds[i];
        const u = url_or_n[i];
        const ans = answer[i];

        let res;
        if (cmd === "visit") res = obj.visit(...u);
        else if (cmd === "back") res = obj.back(...u);
        else if (cmd === "forward") res = obj.forward(...u);

        grading(res, ans);
    }
}
