// https://leetcode.com/problems/word-break/

function wordBreak(s: string, wordDict: string[]): boolean {
    const dp = new Array(s.length + 1).fill(false);
    dp[s.length] = true;    // base case

    for (let i = s.length - 1; i >= 0; i--) {
        for (const w of wordDict) {
            if ((i + w.length <= s.length) && s.substring(i, i + w.length) === w) {
                dp[i] = dp[i + w.length];
            }
            if (dp[i] === true) {
                break;
            }
        }
    }
    
    return dp[0];
};


const testCases: [string, string[], boolean][] = [
    [
        "leetcode",
        ["leet", "code"],
        true,
    ],
    [
        "applepenapple",
        ["apple", "pen"],
        true
    ],
    [
        "catsandog",
        ["cats", "dog", "sand", "and", "cat"],
        false
    ]
];

for (const testCase of testCases) {
    const [s, wordDict, expected] = testCase;
    console.log(wordBreak(s, wordDict));
}

export { };
