/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    const memo = [nums[0]];

    for (let idx=1; idx<nums.length; idx++) {
        memo.push(Math.max(nums[idx], nums[idx] + memo[idx-1]));
    }

    return Math.max(...memo);
};

const testCases = [
    [[-2,1,-3,4,-1,2,1,-5,4], 6],
    [[1], 1],
    [[5,4,-1,7,8], 23]
];

for (const testCase of testCases) {
    const [nums, output] = testCase;
    console.log(maxSubArray(nums));
}

