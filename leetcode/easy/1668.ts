function maxRepeating(sequence: string, word: string): number {
    let answer = 0;

    let temp = word;
    while (sequence.includes(temp)) {
        temp += word;
        answer += 1;
    }

    return answer;
};

const testCases: [string, string, number][] = [
    [
        "ababc",
        "ab",
        2
    ],
    [
        "ababc",
        "ba",
        1
    ],
    [
        "ababc",
        "ac",
        0
    ]
];

for (const testCase of testCases) {
    const [sequence, word, expected] = testCase;
    console.log(maxRepeating(sequence, word));
}

export { };