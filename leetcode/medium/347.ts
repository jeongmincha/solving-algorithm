// https://leetcode.com/problems/top-k-frequent-elements/

function topKFrequent(nums: number[], k: number): number[] {
    // 1. Construct a reversed counter hash map
    const counterMap: { [k: number]: number } = {};
    for (const num of nums) {
        if (num in counterMap) {
            counterMap[num] += 1;
        } else {
            counterMap[num] = 1;
        }
    }
    let reversedCounterMap: { [k: number]: number[] } = {};
    for (let i = 0; i < nums.length; i++) {
        reversedCounterMap[i + 1] = [];
    }
    for (const num in counterMap) {
        const count = counterMap[num];
        reversedCounterMap[count].push(Number(num));
    }

    let answer: number[] = [];
    for (let i = nums.length; i > 0; i--) {
        if (reversedCounterMap[i].length > 0) {
            answer.push(...reversedCounterMap[i]);
            k -= reversedCounterMap[i].length;
        }
        if (k === 0) {
            break;
        }
    }
    return answer;
};

const testCases: [number[], number, number[]][] = [
    [
        [1, 1, 1, 2, 2, 3],
        2,
        [1, 2]
    ],
    [
        [1],
        1,
        [1]
    ],
    [
        [-1, -1],
        1,
        [-1]
    ],
    [
        [1, 2],
        2,
        [1, 2]
    ],
    [
        [4, 1, -1, 2, -1, 2, 3],
        2,
        [-1, 2]
    ]
];

for (const testCase of testCases) {
    const [nums, k, expected] = testCase;
    const answer = topKFrequent(nums, k);
    console.log(answer);
    console.assert(
        answer.sort().join('') === expected.sort().join(''),
        `${answer}, ${expected}`
    );
}

export { };