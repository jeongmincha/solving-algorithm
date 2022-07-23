// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

function countSmaller(nums: number[]): number[] {
    function findIndexToAdd(sortedNums: number[], n: number) {
        if (sortedNums.length === 0) {
            return 0;
        }
        let left = 0, right = sortedNums.length - 1;
        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (sortedNums[mid] < n) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return Math.max(left, right);
    }

    nums.reverse();

    let sortedNums: number[] = [];
    const indices = [];

    for (let i = 0; i < nums.length; i++) {
        const index = findIndexToAdd(sortedNums, nums[i]);
        sortedNums.splice(index, 0, nums[i]);
        indices.push(index);
    }

    indices.reverse();
    return indices;
};

const testCases = [
    [[5, 2, 6, 1], [2, 1, 1, 0]],
    [[-1], [0]],
    [[-1, -1], [0, 0]],
    [[1, 2, 3, 4], [0, 0, 0, 0]],
    [[4, 3, 2, 1], [3, 2, 1, 0]]
];

for (const testCase of testCases) {
    const [nums, expected] = testCase;
    console.log(countSmaller(nums));
}

export { };