// https://leetcode.com/problems/evaluate-reverse-polish-notation/

function evalRPN(tokens: string[]): number {
    if (tokens.length === 1) {
        return parseInt(tokens[0], 10);
    }

    const stack: number[] = [];
    let answer = 0;

    for (let i = 0; i < tokens.length; i++) {
        const token = tokens[i];
        if (token === '+') {
            answer = 0;
            answer += stack.pop() as number;
            answer += stack.pop() as number;
            stack.push(answer);
        } else if (token === '*') {
            answer = 1
            answer *= stack.pop() as number;
            answer *= stack.pop() as number;
            stack.push(answer);
        } else if (token === '/') {
            const a = stack.pop() as number;
            const b = stack.pop() as number;
            if (a * b < 0) {
                answer = Math.ceil(b / a);
            } else {
                answer = Math.floor(b / a);
            }
            stack.push(answer);
        } else if (token === '-') {
            const a = stack.pop() as number;
            const b = stack.pop() as number;
            answer = b - a;
            stack.push(answer);
        } else {
            stack.push(parseInt(token, 10));
        }
    }

    return answer;
};

const testCases: [string[], number][] = [
    [
        ["2", "1", "+", "3", "*"],
        9
    ],
    [
        ["4", "13", "5", "/", "+"],
        6
    ],
    [
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        22
    ],
    [
        ["4", "-2", "/", "2", "-3", "-", "-"],
        -7
    ]
];

for (const testCase of testCases) {
    const [tokens, expected] = testCase;
    const answer = evalRPN(tokens);
    console.log(answer);
}

export { };