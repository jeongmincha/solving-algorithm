function generate(numRows: number): number[][] {
    const answer = [[1]];

    for (let row = 1; row < numRows; row++) {
        const nextRow = [1];
        for (let col = 1; col < row; col++) {
            nextRow.push(answer[row - 1][col - 1] + answer[row - 1][col]);
        }
        nextRow.push(1);
        answer.push(nextRow);
    }

    return answer;
};

const testCases: [number, number[][]][] = [
    [5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]],
    [1, [[1]]]
];

for (const testCase of testCases) {
    const [numRows, expected] = testCase;
    console.log(generate(numRows));
}

export { };