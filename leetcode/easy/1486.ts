function xorOperation(n: number, start: number): number {
    let answer = 0;
    for (let i = 0; i < n; i++) {
        answer ^= start + i * 2;
    }
    return answer;
}

function xorOperation2(n: number, start: number): number {
    const arr = [];
    for (let i = 0; i < n; i++) {
        arr.push(start + i * 2);
    }

    const answer = [];
    const maxStrLen = arr[arr.length - 1].toString(2).length;

    for (let charIndex = 0; charIndex < maxStrLen; charIndex++) {
        let current = 0;
        for (let i = 0; i < n; i++) {
            const char = arr[i].toString(2).split('').reverse()[charIndex];
            if (!!char) {
                current += parseInt(char);
            }
        }
        if (current % 2 === 1) {
            answer.unshift(1);
        } else {
            answer.unshift(0);
        }
    }

    return parseInt(answer.join(''), 2);
};

const testCases = [
    [5, 0, 8],
    [4, 3, 8],
];

for (const testCase of testCases) {
    const [n, start, expected] = testCase;
    console.log(xorOperation(n, start));
}

export { };