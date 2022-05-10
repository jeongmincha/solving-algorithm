/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for (let i = digits.length - 1; i >= 0; i --) {
        if (++digits[i] > 9) {
            digits[i] = 0;
        } else {
            return digits;
        }
    }
    digits.unshift(1);
    return digits;
};

const testCases = [
    [[1,2,3], [1,2,4]],
    [[4,3,2,1], [4,3,2,2]],
    [[9], [1,0]],
];

for (const testCase of testCases) {
    const [digits, output] = testCase;
    console.log(plusOne(digits));
}