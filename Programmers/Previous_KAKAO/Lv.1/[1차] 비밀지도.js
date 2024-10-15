// https://school.programmers.co.kr/learn/courses/30/lessons/17681?language=javascript

/*
constraints:

*/

function solution(n, arr1, arr2) {
    return arr1.map((a, i) =>
        (a | arr2[i])
            .toString(2)
            .padStart(n, "0")
            .replace(/0/g, " ")
            .replace(/1/g, "#"),
    );
}

const inputDatas = [
    {
        data: [5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]],
        answer: ["#####", "# # #", "### #", "#  ##", "#####"],
    },
    {
        data: [6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]],
        answer: ["######", "###  #", "##  ##", " #### ", " #####", "### # "],
    },
];

/*
2018 KAKAO BLIND RECRUITMENT
Lv.1. 현 시점 완료한 사람 38,409명, 정답률 70%
파이썬이랑 같은 풀이.
*/

for (let i = 0; i < inputDatas.length; i++) {
    const { data, answer } = inputDatas[i];
    const res = solution(...data);
    if (JSON.stringify(res) === JSON.stringify(answer)) {
        console.log("pass");
    } else {
        let summary = "fail";
        for (const [label, content] of [
            ["expected:", answer],
            ["got:", res],
        ]) {
            summary += `\n  ${label}\n`;
            summary += `    ${content}`;
            summary = summary.trimEnd();
        }
        console.log(summary);
    }
}
