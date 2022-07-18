function isAdditiveNumber(num: string): boolean {
    for (let i = 1; i < num.length / 2; i++) {
        for (let j = i + 1; j < num.length; j++) {
            const first = num.slice(0, i);
            const second = num.slice(i, j);

            if (isValid(num, first, second, 0)) {
                return true;
            }
        }
    }

    return false;
}

function isValid(num: string, first: string, second: string, startIndex: number): boolean {
    const nextIndex = startIndex + first.length + second.length;
    if (nextIndex === num.length) {
        return true;
    }
    if ((first[0] === '0' && first.length > 1) || (second[0] === '0' && second.length > 1)) {
        return false;
    }

    const sum = parseInt(first) + parseInt(second);
    const sumStr = sum.toString(10);

    if (num.slice(nextIndex).startsWith(sumStr)) {
        return isValid(num, second, sumStr, startIndex + first.length);
    } else {
        return false;
    }
}

const testCases: [string, boolean][] = [
    ["112358", true],
    ["124", false],
    ["123", true],
    ["1203", false],
    ["1023", false],
    ["101", true],
    ["0235813", false],
    ["112341235", true],
    ["123411235", true],
    ["199100199", true]
];

for (const testCase of testCases) {
    const [num, expected] = testCase;
    console.log(isAdditiveNumber(num));
}

export { };
