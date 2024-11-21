// https://school.programmers.co.kr/learn/courses/30/lessons/17680?language=javascript

/*
constraints:

*/

function solution(cacheSize, cities) {
    const HIT = 1;
    const MISS = 5;
    if (cacheSize === 0) return cities.length * MISS;
    let time = 0;
    const cache = new Map();
    for (let city of cities) {
        city = city.toLowerCase();
        if (cache.has(city)) {
            time += HIT;
            cache.delete(city);
            cache.set(city, null);
        } else {
            time += MISS;
            if (cache.size === cacheSize) {
                // Map.prototype.keys()는 이터레이터 객체를 반환해서 next()를 호출해야 한다.
                // next()는 {value: key, done: boolean} 객체를 반환하므로 value를 가져와야 한다.
                const oldestCity = cache.keys().next().value;
                cache.delete(oldestCity);
            }
            cache.set(city, null);
        }
    }
    return time;
}

const inputDatas = [
    {
        data: [
            3,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
            ],
        ],
        answer: 50,
    },
    {
        data: [
            3,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "Jeju",
                "Pangyo",
                "Seoul",
                "Jeju",
                "Pangyo",
                "Seoul",
            ],
        ],
        answer: 21,
    },
    {
        data: [
            2,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "SanFrancisco",
                "Seoul",
                "Rome",
                "Paris",
                "Jeju",
                "NewYork",
                "Rome",
            ],
        ],
        answer: 60,
    },
    {
        data: [
            5,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "SanFrancisco",
                "Seoul",
                "Rome",
                "Paris",
                "Jeju",
                "NewYork",
                "Rome",
            ],
        ],
        answer: 52,
    },
    {data: [2, ["Jeju", "Pangyo", "NewYork", "newyork"]], answer: 16},
    {data: [0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]], answer: 25},
];

/*
2018 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 20,442명, 정답률 64%
js에서도 Map이 입력 순서를 보장하기 때문에 편하게 풀 수 있었다.
python과 마찬가지로 Set이 순서를 보장하니 Set으로도 풀 수 있지만
자료구조 관점에서 오해가 생길 수 있으므로 Map으로 풀었다.
*/

for (let i = 0; i < inputDatas.length; i++) {
    const {data, answer} = inputDatas[i];
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
