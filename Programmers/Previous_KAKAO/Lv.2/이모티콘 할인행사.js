// https://school.programmers.co.kr/learn/courses/30/lessons/150368?language=javascript

/*
constraints:
  • 1 ≤ users의 길이 = n ≤ 100
    ◦ users의 원소는 [비율, 가격]의 형태입니다.
    ◦ users[i]는 i+1번 고객의 구매 기준을 의미합니다.
    ◦ 비율% 이상의 할인이 있는 이모티콘을 모두 구매한다는 의미입니다.
      ▪ 1 ≤ 비율 ≤ 40
    ◦ 가격이상의 돈을 이모티콘 구매에 사용한다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입한다는 의미입니다.
      ▪ 100 ≤ 가격 ≤ 1,000,000
      ▪ 가격은 100의 배수입니다.
  • 1 ≤ emoticons의 길이 = m ≤ 7
    ◦ emoticons[i]는 i+1번 이모티콘의 정가를 의미합니다.
    ◦ 100 ≤ emoticons의 원소 ≤ 1,000,000
    ◦ emoticons의 원소는 100의 배수입니다.
*/


function solution(users, emoticons) {
    function product(array, repeat) {
        let cases = [[]];
        for (let i = 0; i < repeat; i++) {
            cases = cases.flatMap(curCase =>
                array.map(elem => [...curCase, elem])
            );
        }
        return cases;
    }

    const saleData = [10, 20, 30, 40];
    const saleCases = product(saleData, emoticons.length);
    let answer = [0, 0];
    for (const saleCase of saleCases) {
        let [plus, totSales] = [0, 0];
        for (const [userSale, userLimit] of users) {
            let cost = 0;
            for (const [emoIdx, emoSale] of saleCase.entries()) {
                if (emoSale >= userSale) {
                    cost += emoticons[emoIdx] * (1 - emoSale / 100);
                }
            }
            if (cost >= userLimit) plus += 1;
            else totSales += cost;
        }
        if (plus > answer[0] || (plus === answer[0] && totSales > answer[1])) {
            answer = [plus, totSales];
        }
    }
    return answer;
}


const inputDatas = [
    {data: [[[40, 10000], [25, 10000]], [7000, 9000]], answer: [1, 5400]},
    {
        data: [[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]],
        answer: [4, 13860]
    }
];

/*
2023 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 7,054명, 정답률 39%
파이썬 풀이를 그대로 옮겼다. js에는 product가 없어서 직접 구현했다.
product 구현이 가장 힘든 부분이었다.
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
    const res = solution(...data);
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
