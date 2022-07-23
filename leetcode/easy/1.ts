// TC: O(N logN)
function _twoSum(nums: number[], target: number): number[] {
    let numsWithIndex = nums.map((num, idx) => [num, idx]);
    numsWithIndex.sort((a, b) => a[0] - b[0]);

    let left = 0, right = nums.length - 1;
    while (left < right) {
        const twoSum = numsWithIndex[left][0] + numsWithIndex[right][0];
        if (twoSum > target) {
            right -= 1;
        } else if (twoSum < target) {
            left += 1;
        } else {
            break;
        }
    }

    return [numsWithIndex[left][1], numsWithIndex[right][1]];
};

// TC: O(N)
function twoSum(nums: number[], target: number): number[] {
    const seen: { [k: number]: number } = {};

    let answer: number[] = [];
    nums.forEach((num, idx) => {
        if (num in seen) {
            if (seen[num] > idx) {
                answer = [idx, seen[num]];
            } else {
                answer = [seen[num], idx];
            }
            return;
        }
        seen[target - num] = idx;
    });

    return answer;
};

const testCases: [number[], number, number[]][] = [
    [[2, 7, 11, 15], 9, [0, 1]],
    [[3, 2, 4], 6, [1, 2]],
    [[3, 3], 6, [0, 1]]
]

for (const testCase of testCases) {
    const [nums, target, expected] = testCase;
    const answer = twoSum(nums, target);
    console.assert(
        answer.toString() === expected.toString(),
        `solution: ${answer}, expected: ${expected}`
    );
}

export { };