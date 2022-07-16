function getNextWonderfulNumber(arr: number[]): number[] {
    let start = arr.length - 1;
    let end = arr.length - 1;

    while (start > 0 && arr[start - 1] >= arr[start]) {
        start -= 1;
    }

    if (start <= 0) {
        return [];
    }

    while (arr[end] <= arr[start - 1]) {
        end -= 1;
    }

    [arr[start - 1], arr[end]] = [arr[end], arr[start - 1]];

    end = arr.length - 1;
    while (start < end) {
        [arr[start], arr[end]] = [arr[end], arr[start]];
        start += 1;
        end -= 1;
    }

    return arr;
}

function getMinSwaps(num: string, k: number): number {
    let orgArr = num.split('').map(Number);
    let numArr = num.split('').map(Number);

    for (let i = 0; i < k; i++) {
        numArr = getNextWonderfulNumber(numArr);
    }

    let swap = 0;

    for (let start = 0; start < numArr.length; start++) {
        if (orgArr[start] !== numArr[start]) {
            let end = start + 1;

            while (orgArr[start] != numArr[end]) {
                end += 1;
            }

            while (start !== end) {
                [numArr[end - 1], numArr[end]] = [numArr[end], numArr[end - 1]];

                end -= 1;
                swap += 1;
            }
        }
    }

    return swap;
};

const testCases: [string, number, number][] = [
    ["5489355142", 4, 2],
    ["11112", 4, 4],
    ["00123", 1, 1]
];

for (const testCase of testCases) {
    const [num, k, expected] = testCase;
    console.log(getMinSwaps(num, k));
}

export { };