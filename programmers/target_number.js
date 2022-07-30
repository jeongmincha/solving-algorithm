function dfs(currentIdx, currentValue, numbers, target) {
    if (currentIdx === numbers.length) {
        if (currentValue === target) {
            return 1;
        }
        return 0;
    }

    const l = dfs(currentIdx + 1, currentValue + numbers[currentIdx], numbers, target);
    const r = dfs(currentIdx + 1, currentValue - numbers[currentIdx], numbers, target);
    return l + r;
}

function solution(numbers, target) {
    return dfs(0, 0, numbers, target);
};

const testCases = [
    [
        [1, 1, 1, 1, 1],
        3,
        5,
    ],
    [
        [4, 1, 2, 1],
        4,
        2
    ]
];

for (const testCase of testCases) {
    const [numbers, target, expected] = testCase;
    console.log(solution(numbers, target));
}
