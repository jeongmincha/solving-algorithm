// https://leetcode.com/problems/maximum-subarray/

function maxSubArray(nums: number[]): number {
    let answer = Math.max(...nums);
    let curSum = 0;

    for (const n of nums) {
        curSum = Math.max(curSum + n, n)
        answer = Math.max(answer, curSum)
    }

    return answer;
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