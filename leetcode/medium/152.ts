// https://leetcode.com/problems/maximum-product-subarray/

function maxProduct(nums: number[]): number {
    let answer = Math.max(...nums);
    let curMin = 1, curMax = 1;

    for (const n of nums) {
        if (n === 0) {
            curMin = 1, curMax = 1;
            continue;
        }

        const _curMax = n * curMax;
        const _curMin = n * curMin;

        curMin = Math.min(_curMax, _curMin, n)
        curMax = Math.max(_curMax, _curMin, n)

        answer = Math.max(answer, curMax);
    }

    return answer;
};

const testCases: [number[], number][] = [
    [
        [2, 3, -2, 4],
        6
    ],
    [
        [2, 3, -2, -4],
        48
    ],
    [
        [-2, 0, -1],
        0,
    ]
];

for (const testCase of testCases) {
    const [nums, expected] = testCase;
    console.log(maxProduct(nums));
}

export { };