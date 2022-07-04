function threeConsecutiveOdds(arr: number[]): boolean {
    if (arr.length < 3) {
        return false;
    }

    for (let i = 0; i < arr.length - 2; i++) {
        if (arr[i] % 2 === 1 && arr[i + 1] % 2 === 1 && arr[i + 2] % 2 === 1) {
            return true;
        }
    }
    return false;
};

const testCases = [
    [[1, 2, 3], false],
    [[2, 6, 4, 1], false],
    [[1, 2, 34, 3, 4, 5, 7, 23, 12], true]
]

for (const testCase of testCases) {
    const [arr, expected] = testCase;
    console.log(threeConsecutiveOdds(arr as number[]));
}

export { }