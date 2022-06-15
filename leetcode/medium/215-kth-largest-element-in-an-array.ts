function findKthLargest(nums: number[], k: number): number {
    let subMin = Math.min(...nums);
    let subMax = Math.max(...nums);

    if (k === nums.length) {
        return subMin;
    }
    if (k === 1) {
        return subMax;
    }

    while (subMin < subMax) {
        let mid = Math.ceil((subMin + subMax) / 2);

        let countLargerThanMid = 0;
        for (const num of nums) {
            if (num >= mid) {
                countLargerThanMid += 1;
            }
        }
        if (countLargerThanMid < k) {
            subMax = mid - 1;
        } else {
            subMin = mid;
        }
    }

    return subMin;
};

describe('215. findKthLargest()', () => {
    const testCases = [
        [[3, 2, 1, 5, 6, 4], 2, 5],
        [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4],
        [[3, 3, 3, 3, 4, 3, 3, 3, 3], 5, 3],
        [[1, 2, 3, 4], 4, 1],
        [[1, 2, 3, 4], 1, 4],
    ];

    test.each(testCases)(
        'findKthLargest(%o, %d) -> %d',
        (_nums, _k, expected) => {
            const nums = _nums as number[];
            const k = _k as number;

            expect(findKthLargest(nums, k)).toBe(expected);
        }
    );
});