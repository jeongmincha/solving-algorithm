// https://leetcode.com/problems/longest-repeating-character-replacement/

function characterReplacement(s: string, k: number): number {
    let answer = 0;
    let l = 0;
    const counter: {[k: string]: number} = {};

    for (let r = 0; r < s.length; r++) {
        if (s[r] in counter) {
            counter[s[r]] += 1;
        } else {
            counter[s[r]] = 1;
        }

        const maxFrequentCharCount = Math.max(...Object.values(counter));
        while (r - l + 1 - maxFrequentCharCount > k) {
            counter[s[l]] -= 1;
            l += 1;
        }
        answer = Math.max(answer, r - l + 1);    
    }

    return answer;
};

const testCases: [string, number, number][] = [
    [
        "ABAB",
        2,
        4
    ],
    [
        "AABABBA",
        1,
        4
    ]
];

for (const testCase of testCases) {
    const [s, k, expected] = testCase;
    console.log(characterReplacement(s, k));
}

export { };