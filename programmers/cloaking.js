function solution(clothes) {
    const hash = {};
    for (const cloth of clothes) {
        const [name, category] = cloth;
        if (category in hash) {
            hash[category] += 1;
        } else {
            hash[category] = 1;
        }
    }

    let answer = 1;
    for (const category in hash) {
        answer *= hash[category] + 1;
    }

    return answer-1;
}

const testCases = [
    [
        [
            ["yellow_hat", "headgear"], 
            ["blue_sunglasses", "eyewear"], 
            ["green_turban", "headgear"]
        ],
        5,
    ]
];

for (const testCase of testCases) {
    const [clothes, expected] = testCase;
    const answer = solution(clothes);
    console.assert(
        answer === expected,
        `${answer}, ${expected}`
    );
}