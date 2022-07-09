function maxEqualRowsAfterFlips(matrix: number[][]): number {
    function arrayEquals(arr1: number[], arr2: number[]) {
        return !(arr1 > arr2 || arr1 < arr2);
    }

    const m = matrix.length;
    const n = matrix[0].length;

    let counter: { [k: string]: number } = {};

    for (let i = 0; i < m; i++) {
        let flippedCurrentRow = '';
        for (let j = 0; j < n; j++) {
            flippedCurrentRow += 1 - matrix[i][j];
        }

        const currentRow = matrix[i].join('');

        counter[currentRow] ??= 0;
        counter[flippedCurrentRow] ??= 0;

        counter[currentRow] += 1;
        counter[flippedCurrentRow] += 1;
    }

    return Math.max(...Object.values(counter));
};

const testCases = [
    [[[0, 1], [1, 1]], 1],
    [[[0, 1], [1, 0]], 2],
    [[[0, 0, 0], [0, 0, 1], [1, 1, 0]], 2]
];

for (const testCase of testCases) {
    const [matrix, expected] = testCase;

    console.log(maxEqualRowsAfterFlips(matrix as number[][]));
}

export { };