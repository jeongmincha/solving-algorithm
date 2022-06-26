function findMaxIndex(arr: number[]): number {
    let idx;
    for (idx = 0; idx < arr.length; idx++) {
        if (arr[idx] === arr.length) {
            break;
        }
    }
    return idx;
}

function pancakeSort(arr: number[]): number[] {
    const flipIndices: number[] = [];

    let currentSize = arr.length;
    while (currentSize > 1) {
        const maxIndex = findMaxIndex(arr.slice(0, currentSize)) + 1;

        if (maxIndex === 1) {
            arr = arr.slice(0, currentSize).reverse();
            flipIndices.push(currentSize);
        } else if (maxIndex !== currentSize) {
            arr = [...arr.slice(0, maxIndex).reverse(), ...arr.slice(maxIndex)];
            flipIndices.push(maxIndex);

            arr = arr.slice(0, currentSize).reverse();
            flipIndices.push(currentSize);
        }
        currentSize -= 1;
    }

    return flipIndices;
};

const testCases = [
    [[3, 2, 4, 1], [4, 2, 4, 3]],
    [[1, 2, 3], []],
    [[4, 3, 2, 1], [4]]
];

for (const testCase of testCases) {
    const [arr, expected] = testCase;
    console.log(pancakeSort(arr));
}

export { };