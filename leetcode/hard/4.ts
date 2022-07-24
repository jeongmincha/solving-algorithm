// https://leetcode.com/problems/median-of-two-sorted-arrays/

function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    const m = nums2.length;

    if (n > m)
        return findMedianSortedArrays(nums2, nums1);

    let start = 0;
    let end = n;
    let medianIndex = Math.floor((n + m + 1) / 2);

    let answer = 0;
    while (start <= end) {
        const mid = Math.floor((start + end) / 2);
        const sizeLeft1 = mid;
        const sizeLeft2 = medianIndex - mid;

        const left1 = sizeLeft1 > 0 ? nums1[sizeLeft1 - 1] : -Infinity;
        const left2 = sizeLeft2 > 0 ? nums2[sizeLeft2 - 1] : -Infinity;
        const right1 = sizeLeft1 < n ? nums1[sizeLeft1] : Infinity;
        const right2 = sizeLeft2 < m ? nums2[sizeLeft2] : Infinity;

        if (left1 <= right2 && left2 <= right1) {
            if ((m + n) % 2 == 0)
                answer = (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
            else
                answer = Math.max(left1, left2);
            break;
        }
        else if (left1 > right2) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    return answer;
};

const testCases: [number[], number[], number][] = [
    [[1, 3], [2], 2],
    [[1, 2], [3, 4], 2.5],
    [[3, 4], [1, 2], 2.5],
];

for (const testCase of testCases) {
    const [nums1, nums2, expected] = testCase;
    const answer = findMedianSortedArrays(nums1, nums2);
    console.assert(
        answer === expected,
        `\n- answer: ${answer}\n- expected: ${expected}`
    )
}


export { };