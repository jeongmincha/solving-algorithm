// https://leetcode.com/problems/text-justification/

function makeFullJustifiedSentence(words: string[], maxWidth: number): string {
    if (words.length <= 1) {
        return makeLeftJustifiedSentence(words, maxWidth);
    }

    let numSpaces = maxWidth - words.reduce((prev, curr) => prev + curr.length, 0);

    const spaces = new Array(words.length - 1).fill('');
    for (let i = 0; i < numSpaces; i++) {
        spaces[i % (words.length - 1)] += ' ';
    }

    const totalWords = [];
    for (let i = 0; i < words.length - 1; i++) {
        totalWords.push(words[i]);
        totalWords.push(spaces[i]);
    }
    totalWords.push(words[words.length - 1]);

    return totalWords.join('');
};

function makeLeftJustifiedSentence(words: string[], maxWidth: number): string {
    const leftPart = words.join(' ');
    return leftPart + new Array(maxWidth - leftPart.length).fill(' ').join('');
};

function fullJustify(words: string[], maxWidth: number): string[] {
    const lines = [];

    let currentLine: string[] = [];
    let currentLen = 0;

    for (const word of words) {
        currentLen += word.length;
        if (currentLen > maxWidth) {
            currentLen = word.length + 1;
            lines.push(makeFullJustifiedSentence(currentLine, maxWidth));
            currentLine = [word];
        } else {
            currentLen += 1;
            currentLine.push(word);
        }
    }
    if (currentLine.length > 0) {
        lines.push(makeLeftJustifiedSentence(currentLine, maxWidth));
    }

    return lines;
};

const testCases: [string[], number, string[]][] = [
    // [
    //     ["This", "is", "an", "example", "of", "text", "justification."],
    //     16,
    //     [
    //         "This    is    an",
    //         "example  of text",
    //         "justification.  "
    //     ]
    // ],
    // [
    //     ["What", "must", "be", "acknowledgment", "shall", "be"],
    //     16,
    //     [
    //         "What   must   be",
    //         "acknowledgment  ",
    //         "shall be        "
    //     ]
    // ],
    [
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],
        20,
        [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
    ]
];

for (const testCase of testCases) {
    const [words, maxWidth, expected] = testCase;
    const answer = fullJustify(words, maxWidth);
    console.assert(
        answer.toString() === expected.toString(),
        `\n- solution: ${answer},\n- expected: ${expected}`
    );
}


export { };