function maxProfit(prices: number[]): number {
    let maxProfit = 0;

    let left = 0;
    let right = 1;

    while (right < prices.length) {
        if (prices[left] > prices[right]) {
            left = right;
            right += 1;
        } else {
            maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
            right += 1;
        }
    }

    return maxProfit;
};

const testCases: [number[], number][] = [
    [
        [7, 1, 5, 3, 6, 4],
        5,
    ]
];

for (const testCase of testCases) {
    const [prices, expected] = testCase;
    const answer = maxProfit(prices);
    console.assert(
        answer === expected,
        `${answer}, ${expected}`
    );
}

export { };