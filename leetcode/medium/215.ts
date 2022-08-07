// https://leetcode.com/problems/kth-largest-element-in-an-array/

function findKthLargest(nums: number[], k: number): number {
    let l = 0, r = nums.length;

    while (l < r) {
        // randomly pick up a pivot element
        const pivot = nums[r - 1];

        const small = [];
        const large = [];
        const same = [];

        // find elements which is same, larger, smaller than pivot
        for (let i = l; i < r; i++) {
            if (nums[i] < pivot) {
                small.push(nums[i]);
            } else if (nums[i] > pivot) {
                large.push(nums[i]);
            } else {
                same.push(nums[i]);
            }
        }

        nums = [...nums.slice(0, l), ...small, ...same, ...large, ...nums.slice(r)]

        // kth largest one must be in 'large' part, increase l
        if (k <= large.length) {
            l += small.length + same.length
        }
        // kth largest one must be in 'same' part, just return pivot
        else if (k > large.length && k <= same.length + large.length) {
            return pivot;
        }
        // kth largest one must be in 'small' part, decrease k and r
        else if (k > same.length + large.length) {
            k -= (same.length + large.length);
            r -= (same.length + large.length);
        }
    }

    return 0;
};

const testCases: [number[], number, number][] = [
    [
        [3, 2, 1, 5, 6, 4],
        2,
        5
    ],
    [
        [3, 2, 3, 1, 2, 4, 5, 5, 6],
        4,
        4
    ],
    [
        [1],
        1,
        1
    ],
    [
        [-1, 2, 0],
        2,
        0
    ]
];

for (const testCase of testCases) {
    const [nums, k, expected] = testCase;
    console.log(findKthLargest(nums, k));
}

export { };