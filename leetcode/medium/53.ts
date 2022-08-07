// https://leetcode.com/problems/maximum-subarray/

function maxSubArray(nums: number[]): number {
    let bestSum = -Infinity;
    let endSum = 0;

    for (const n of nums) {
        endSum = Math.max(endSum + n, n)
        bestSum = Math.max(bestSum, endSum)
    }

    return bestSum;
};

const testCases: [number[], number][] = [
    [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        6
    ],
    [
        [1],
        1
    ],
    [
        [5, 4, -1, 7, 8],
        23
    ]
];

for (const testCase of testCases) {
    const [nums, expected] = testCase;
    console.log(maxSubArray(nums));
}

export { };