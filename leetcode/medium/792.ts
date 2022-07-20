function isSubStr(s: string, word: string): boolean {
    if (word.length === 0) {
        return true;
    }

    const firstCharIndex = s.indexOf(word[0]);
    if (firstCharIndex >= 0) {
        return isSubStr(s.slice(firstCharIndex + 1), word.slice(1));
    } else {
        return false;
    }
};

function numMatchingSubseq(s: string, words: string[]): number {
    let cnt = 0;
    words.forEach(word => {
        if (isSubStr(s, word)) {
            cnt += 1;
        }
    });
    return cnt;
};

const testCases: [string, string[], number][] = [
    ["abcde", ["a", "bb", "acd", "ace"], 3],
    ["dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], 2]
];

for (const testCase of testCases) {
    const [s, words, expected] = testCase;
    console.log(numMatchingSubseq(s, words));
}

export { };