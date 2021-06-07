export function reverseWords(str: string): string {
    let answer = ""
    let stack = []

    for (var i = 0; i < str.length; i++) {
        const c = str.charAt(i)
        if (c !== " ") {
            stack.push(c)
        } else {
            while (stack.length > 0) {
                answer += stack.pop()
            }
            answer += c
        }
    }
    while (stack.length > 0) {
        answer += stack.pop()
    }
    return answer
}

const testCases = [
    {
        'str': 'The quick brown fox jumps over the lazy dog.',
        'expected': 'ehT kciuq nworb xof spmuj revo eht yzal .god'
    },
    {
        'str': 'apple',
        'expected': 'elppa'
    },
    {
        'str': 'a b c d',
        'expected': 'a b c d'
    },
    {
        'str': 'double  spaced  words',
        'expected': 'elbuod  decaps  sdrow'
    }
]

for (const testCase of testCases) {
    const output = reverseWords(testCase.str)
    if (output != testCase.expected) {
        throw new Error(`${output} != ${testCase.expected}`)
    }
}
console.log(`All tests cleared!`)