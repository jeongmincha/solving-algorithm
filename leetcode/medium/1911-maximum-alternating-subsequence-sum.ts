function maxAlternatingSum(nums: number[]): number {
    const memo = new Array(nums.length).fill({}).map(o => [0, 0]);
    memo[0][0] = nums[0];

    for (let i = 1; i < nums.length; i++) {
        memo[i][0] = Math.max(memo[i - 1][0], memo[i - 1][1] + nums[i]);
        memo[i][1] = Math.max(memo[i - 1][1], memo[i - 1][0] - nums[i]);
    }

    return memo[nums.length - 1][0];
};

function maxAlternatingSum2(nums: number[]): number {
    let resultOdd = 0;
    let resultEven = 0;

    for (let i = 0; i < nums.length; i++) {
        resultOdd = Math.max(resultOdd, resultEven + nums[i]);
        resultEven = Math.max(resultEven, resultOdd - nums[i]);
    }

    return resultOdd;
};

const testCases = [
    [[4, 2, 5, 3], 7],
    [[5, 6, 7, 8], 8],
    [[6, 2, 1, 2, 4, 5], 10]
];

for (const testCase of testCases) {
    const [nums, expected] = testCase;
    console.log(maxAlternatingSum2(nums as number[]));
}

export { };