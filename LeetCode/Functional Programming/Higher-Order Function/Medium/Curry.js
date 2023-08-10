// https://leetcode.com/problems/curry/
/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    return function curried(...args) {  // curry 내부에서 정의된 함수이므로 클로저.
        if (args.length >= fn.length) {  // fn.length는 함수의 인자 개수.
            // 클로저라 나중에 재귀 등으로 호출돼도 fn에 접근 가능.
            return fn(...args);  // 채워졌으면 fn에 넣어서 실행.
        }
        return curried.bind(this, ...args);  // args가 채워질 때까지 대기
    };
};

const examples = [
    {
        fn: function sum(a, b) { return a + b; },
        args: [[1], [2]],
        expected: 3
    },
    {
        fn: function sum(a, b, c) { return a + b + c; },
        args: [[1], [2], [3]],
        expected: 6
    },
    {
        fn: function sum(a, b, c) { return a + b + c; },
        args: [[1, 2], [3]],
        expected: 6
    },
    {
        fn: function sum(a, b, c) { return a + b + c; },
        args: [[],[],[1,2,3]],
        expected: 6
    },
    {
        fn: function life() { return 42; },
        args: [[]],
        expected: 42
    }
]

/*
* Leetcode Medium.
* 풀려고 들어와보니 Python이 없고 js, ts만 있었다.
* js를 연습해보는 것도 좋겠다 싶어 js로 풀었다.
* 클로저 개념을 처음 알았고, bind를 오랜만에 썼다.
* 클로저를 파이썬에서도 테스트 해봤는데 정상적으로 작동했다.
* 보안성 면에서 아주 좋은 방법인 듯 하다.
* */

examples.forEach(example => {
    const curried = curry(example.fn);
    let result = curried;

    for (const argGroup of example.args) {
        result = result(...argGroup);
    }

    if (result === example.expected) {
        console.log('Success');
    } else {
        console.log('Fail');
    }
});