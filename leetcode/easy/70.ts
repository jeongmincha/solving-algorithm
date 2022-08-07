// https://leetcode.com/problems/climbing-stairs/

function climbStairs(n: number): number {
    const memo = new Array(n + 1).fill(0);
    memo[1] = 1;
    memo[2] = 2;

    for (let i = 3; i <= n; i++) {
        memo[i] = memo[i - 1] + memo[i - 2];
    }

    return memo[n];
};

const testCases: [number, number][] = [
    [
        2,
        2
    ],
    [
        3,
        3
    ]
];

for (const testCase of testCases) {
    const [n, expected] = testCase;
    console.log(climbStairs(n));
}

export { };
