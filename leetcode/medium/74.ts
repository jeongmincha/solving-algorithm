// https://leetcode.com/problems/search-a-2d-matrix/

function searchMatrix(matrix: number[][], target: number): boolean {
    let targetRowIdx = -1;
    for (let row = 1; row < matrix.length; row++) {
        if (target < matrix[row][0]) {
            targetRowIdx = row - 1;
            break;
        }
    }
    if (targetRowIdx < 0)
        targetRowIdx = matrix.length - 1;

    const row = matrix[targetRowIdx];
    let left = 0;
    let right = row.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (row[mid] === target) {
            return true;
        } else if (row[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return false;
};

const testCases: [number[][], number, boolean][] = [
    [
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
        13,
        false,
    ],
    [
        [[1]],
        1,
        true,
    ]
];

for (const testCase of testCases) {
    const [matrix, target, expected] = testCase;
    const answer = searchMatrix(matrix, target);
    console.assert(
        answer === expected,
        `${answer}, ${expected}`
    )
}

export { };