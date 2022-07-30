function solution(priorities, location) {
    let turn = 0;
    const queue = priorities;
    while (queue.length > 0) {
        console.log('queue: ', queue, location);
        const current = queue.shift();
        if (current >= Math.max(...queue)) {
            turn += 1;

            if (location === 0) {
                break;
            }   
        } else {
            queue.push(current);
        }

        location -= 1;
        if (location < 0)
            location = queue.length - 1;
    }

    return turn;
}

const testCases = [
    [[2,1,3,2],2,1],
    [[1,1,9,1,1,1],0,5]
];

for (const testCase of testCases) {
    const [priorities, location, expected] = testCase;
    const answer = solution(priorities, location);
    console.assert(answer === expected,
        `${answer}, ${expected}`);
}