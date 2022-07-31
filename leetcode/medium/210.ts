// https://leetcode.com/problems/course-schedule-ii/

function dfs(
    course: number,
    adjs: { [k: number]: number[] },
    visited: { [k: number]: boolean },
    answer: Set<number>,
): boolean {
    if (visited[course] === true) { // cycle appears
        return false;
    }
    if (adjs[course] === undefined || adjs[course].length === 0) {
        return true;
    }

    visited[course] = true;
    for (const p of adjs[course]) {
        if (dfs(p, adjs, visited, answer) === false) {
            return false;
        }
        answer.add(p);
    }
    delete visited[course];

    return true;
}

function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    const adjs: { [k: number]: number[] } = {};
    for (const p of prerequisites) {
        const [last, first] = p;
        if (last in adjs) {
            adjs[last].push(first);
        } else {
            adjs[last] = [first];
        }
    }

    const visited: { [k: number]: boolean } = {};
    const answer = new Set<number>();

    for (let course = 0; course < numCourses; course++) {
        if (dfs(course, adjs, visited, answer) === false) {
            return [];
        } else {
            answer.add(course);
        }
    }

    return Array.from(answer);
};

const testCases: [number, number[][], number[]][] = [
    [
        2,
        [[1, 0]],
        [0, 1]
    ],
    [
        4,
        [[1, 0], [2, 0], [3, 1], [3, 2]],
        [0, 2, 1, 3]
    ],
    [
        1,
        [],
        [0]
    ],
    [
        2,
        [[1, 0], [0, 1]],
        []
    ]
];

for (const testCase of testCases) {
    const [numCourses, prerequisites, expected] = testCase;
    const answer = findOrder(numCourses, prerequisites);
    console.log(answer);
}

export { };