/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    let mid = Math.floor((left + right) / 2);

    while (nums[mid] !== target && left <= right) {
        if (target < nums[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }

        mid = Math.floor((left + right) / 2);
    }

    return nums[mid] === target ? mid : left;
};

const test_cases = [
    [[1,3,5,6], 5, 2],
    [[1,3,5,6], 2, 1],
    [[1,3,5,6], 7, 4]
];

for (let idx=0; idx<test_cases.length; idx++) {
    const [nums, target, output] = test_cases[idx];
    console.log(searchInsert(nums, target));
}
