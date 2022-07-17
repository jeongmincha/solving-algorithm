function search(nums: number[], target: number): number {
    let start = 0
    let end = nums.length - 1;

    let pivotIndex = 0;
    while (start < end) {
        pivotIndex = Math.floor((start + end) / 2);
        if (pivotIndex > 0 && nums[pivotIndex - 1] > nums[pivotIndex]) {
            break;
        }
        if (nums[pivotIndex] > nums[end]) {
            start = ++pivotIndex;
        } else {
            end = --pivotIndex;
        }
    }

    if (pivotIndex > 0) {
        nums = [...nums.slice(pivotIndex, nums.length), ...nums.slice(0, pivotIndex)];
    }
    pivotIndex = Math.max(pivotIndex, 0);

    start = 0
    end = nums.length - 1;
    while (start <= end) {
        const mid = Math.floor((start + end) / 2);
        if (nums[mid] === target) {
            return (mid + pivotIndex) % nums.length;
        }

        if (target > nums[mid]) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return -1;
};

const testCases: [number[], number, number][] = [
    [[4, 5, 6, 7, 0, 1, 2], 0, 4],
    [[4, 5, 6, 7, 0, 1, 2], 3, -1],
    [[1], 0, -1],
    [[1], 1, 0],
    [[1, 2, 3, 4], 4, 3],
    [[1, 2, 3, 4, 5, 6], 4, 3],
    [[8, 1, 2, 3, 4, 5, 6, 7], 6, 6],
    [[3, 1], 1, 1],
    [[1, 3], 1, 0],
];

for (const testCase of testCases) {
    const [nums, target, expected] = testCase;
    console.log(search(nums, target));
}


export { };