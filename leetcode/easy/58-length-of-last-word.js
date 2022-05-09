/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    if (!s.includes(" ")) {
        return s.length;
    }

    let currWordLength = 0;

    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] !== " ") {
            currWordLength += 1;
        } else if (currWordLength > 0) {
            return currWordLength;
        }
    }

    return currWordLength;
};

const testCases = [
    // ["Hello World", 5],
    // ["   fly me   to   the moon  ", 4],
    // ["luffy is still joyboy", 6],
    ["a ", 1]
];

for (const testCase of testCases) {
    const [s, output] = testCase;
    console.log(lengthOfLastWord(s));
}