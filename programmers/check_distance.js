function solution(places) {
    return places.map(place => {
        return place.some((row, rowIndex) => {
            return row.split('').some((elem, index, arr) => {
                if (elem == 'X') {
                    return false;
                }

                const userCount = [
                    arr[index-1] || null,
                    arr[index+1] || null,
                    (place[rowIndex-1] || '').charAt(index),
                    (place[rowIndex+1] || '').charAt(index)
                ].filter(v => v == 'P').length;

                if (
                        (elem == 'P' && userCount > 0) ||
                        (elem == 'O' && userCount >= 2)
                    ) {
                        return true;
                }

                return false;
            }, '');
        }) ? 0 : 1;
    });
}

const testCases = [
    [
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
        ],
        [1,0,1,1,1]
    ]
];

for (const testCase of testCases) {
    const [places, expected] = testCase;
    const answer = solution(places);
    console.assert(
        !(answer > expected || answer < expected),
        `${answer}, ${expected}`
    )
}