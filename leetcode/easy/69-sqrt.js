/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x < 2) {
        return x;
    }

    let left = 1;
    let right = x;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (mid * mid == x) {
            return mid;
        } else if (mid * mid > x) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left - 1;
};

var mySqrt2 = function(x) {
    if (x === 0 || x === 1) {
        return x;
    }

    let lastSqrt = 1;
    for (i = 2; i < x; i ++) {
        if (i * i <= x) {
            lastSqrt = i;
        } else {
            break;
        }
    }

    return lastSqrt;
};

const testCases = [
    [4, 2],
    [8, 2]
];

for (const testCase of testCases) {
    const [x, output] = testCase;

    console.log(mySqrt(x));
    console.log(mySqrt2(x));
}