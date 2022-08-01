// https://leetcode.com/problems/meeting-rooms-ii/

function minMeetingRooms(intervals: number[][]): number {
    const starts = intervals.map(o => o[0]);
    const ends = intervals.map(o => o[1]);

    starts.sort((a, b) => a - b);
    ends.sort((a, b) => a - b);

    let answer = 1;
    let i = 0, j = 0, n = 0;
    while (i < starts.length && j < ends.length) {
        if (starts[i] >= ends[j]) {
            n--;
            j++;
        } else {
            n++;
            i++;
        }
        answer = Math.max(answer, n);
    }
    return answer;
};

const testCases: [number[][], number][] = [
    [
        [[0, 30], [5, 10], [15, 20]],
        2
    ],
    [
        [[7, 10], [2, 4]],
        1
    ],
    [
        [[0, 30], [5, 25], [10, 20]],
        3
    ],
    [
        [[1, 2], [3, 4], [5, 6]],
        1,
    ]
];

for (const testCase of testCases) {
    const [intervals, expected] = testCase;
    const answer = minMeetingRooms(intervals);
    console.log(answer);
}

export { };