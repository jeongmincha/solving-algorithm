function findLengthOfLCIS(nums: number[]): number {
    if (nums.length === 1) {
        return 1;
    }

    let answer = 1, cnt = 1;

    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] < nums[i + 1]) {
            cnt += 1;
            answer = Math.max(answer, cnt);
        } else {
            cnt = 1;
        }
    }

    return answer;
};

const testCases = [
    [[1, 3, 5, 4, 7], 3],
    [[2, 2, 2, 2, 2], 1],
    [[100, 1, 100, 1, 100], 1],
    [[1, 2, 3, 4, 5], 5],
    [[5, 4, 3, 2, 1], 5],
    [[1], 1],
    [[1, 3, 5, 4, 2, 3, 4, 5], 4]
];

for (const testCase of testCases) {
    const [nums, expected] = testCase;
    console.log(findLengthOfLCIS(nums as number[]));
}

export { };