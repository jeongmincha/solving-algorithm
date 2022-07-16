function getReversedBinaryArray(num: number): number[] {
    const binary = [];
    while (num > 0) {
        binary.push(num % 2);
        num = num >> 1;
    }
    return binary;
}

function minBitFlips(start: number, goal: number): number {
    const convertedMax = getReversedBinaryArray(Math.max(start, goal));
    const convertedMin = getReversedBinaryArray(Math.min(start, goal));

    let step = 0;
    for (let i = 0; i < convertedMax.length; i++) {
        const maxChar = convertedMax[i];
        const minChar = convertedMin[i] ?? 0;

        if (maxChar !== minChar) {
            step += 1;
        }
    }

    return step;
};

const testCases: [number, number, number][] = [
    [10, 7, 3],
    [3, 4, 3],
    [1, 1, 0],
    [1, 16, 2],
    [0, 10 ** 9, 13],
    [0, 2 ** 30, 1]
];

for (const testCase of testCases) {
    const [start, goal, expected] = testCase;
    console.log(minBitFlips(start, goal));
}

export { };