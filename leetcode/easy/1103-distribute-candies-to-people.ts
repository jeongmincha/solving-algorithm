function distributeCandies(candies: number, num_people: number): number[] {
    const distributed = new Array(num_people).fill(0);

    let current_turn = 1, idx = 0;

    while (candies > 0) {
        distributed[idx] += Math.min(current_turn, candies);
        idx = (idx + 1) % num_people;
        candies -= current_turn;
        current_turn += 1;
    }

    return distributed;
};

const testCases = [
    [7, 4, [1, 2, 3, 1]],
    [10, 3, [5, 2, 3]],
    [1, 5, [1, 0, 0, 0, 0]],
    [10, 4, [1, 2, 3, 4]],
    [11, 4, [2, 2, 3, 4]]
];

for (const testCase of testCases) {
    const [candies, num_people, expected] = testCase;
    console.log(distributeCandies(candies as number, num_people as number));
}