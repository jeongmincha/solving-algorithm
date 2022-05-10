/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    if (a.length > b.length) {
        const diff = a.length - b.length;
        for (let i=0; i<diff; i++) {
            b = "0" + b;
        }
    }
    if (b.length > a.length) {
        const diff = b.length - a.length;
        for (let i=0; i<diff; i++) {
            a = "0" + a;
        }
    }
    const maxLength = Math.max(a.length, b.length);

    let carry = 0;
    const output = [];
    for (let i = 1; i <= maxLength; i ++) {
        const curr = parseInt(a[a.length - i]) + parseInt(b[b.length - i]) + carry;
        if (curr >= 2) {
            output.unshift((curr - 2).toString());
            carry = 1;
        } else {
            output.unshift(curr.toString());
            carry = 0;
        }
    }

    if (carry > 0) {
        output.unshift("1");
    }

    return output.join('');
};

const testCases = [
    ["11", "1", "100"],
    ["1010", "1011", "10101"]
];

for (const testCase of testCases) {
    const [a, b, output] = testCase;
    console.log(addBinary(a, b));
}