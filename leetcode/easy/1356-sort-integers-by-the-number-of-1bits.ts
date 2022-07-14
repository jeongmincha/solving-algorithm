function countBits(num: number): number {
    let cnt = 0;
    while (num > 0) {
        if (num & 1) {
            cnt += 1;
        }
        num >>= 1;
    }
    return cnt;
}

function sortByBits(arr: number[]): number[] {
    const arrWithBits: [number, number][] = [];

    arr.forEach(elem => {
        arrWithBits.push([elem, countBits(elem)]);
    });

    arrWithBits.sort((a, b) => {
        return a[1] === b[1] ? a[0] - b[0] : a[1] - b[1];
    });

    return arrWithBits.map(elem => elem[0]);
};

const testCases = [
    [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 4, 8, 3, 5, 6, 7]],
    [[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]]
];

for (const testCase of testCases) {
    const [arr, expected] = testCase;

    console.log(sortByBits(arr));
}

export { };