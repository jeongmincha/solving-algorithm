// https://leetcode.com/problems/course-schedule/

function dfs(
    course: number,
    preMap: { [k: number]: number[] },
    visited: boolean[]
): boolean {
    if (visited[course] === true) {
        return false;
    }
    if (preMap[course].length === 0) {
        return true;
    }

    visited[course] = true;
    for (const preCourse of preMap[course]) {
        if (dfs(preCourse, preMap, visited) === false) {
            return false;
        }
    }
    visited[course] = false;
    preMap[course] = [];
    return true;
}

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const preMap: { [k: number]: number[] } = {};
    for (let i = 0; i < numCourses; i++) {
        preMap[i] = [];
    }

    for (const p of prerequisites) {
        const [course, pre] = p;
        preMap[course].push(pre);
    }

    const visited = new Array(numCourses).fill(false);

    for (let course = 0; course < numCourses; course++) {
        if (dfs(course, preMap, visited) === false) {
            return false;
        }
    }

    return true;
};

const testCases: [number, number[][], boolean][] = [
    [
        2,
        [[1, 0]],
        true
    ],
    [
        2,
        [[1, 0], [0, 1]],
        false
    ],
    [
        3,
        [],
        true
    ],
    [
        5,
        [[1, 4], [2, 4], [3, 1], [3, 2]],
        true,
    ]
];

for (const testCase of testCases) {
    const [numCourses, prerequisites, expected] = testCase;
    const answer = canFinish(numCourses, prerequisites);
    console.assert(
        answer === expected,
        `${answer}, ${expected}`
    );
}

export { };