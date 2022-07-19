function minimumTimeRequired(jobs: number[], k: number): number {
    const maxJobs = Math.max(...jobs);
    const sumJobs = jobs.reduce((prev, curr) => prev + curr, 0);

    if (k === 1) {
        return sumJobs;
    }
    if (k === jobs.length) {
        return maxJobs;
    }

    let res = 0;
    let left = maxJobs;
    let right = sumJobs;

    while (left <= right) {
        const assigned = new Array(k).fill(0);
        const mid = Math.floor((left + right) / 2);

        if (isValid(jobs, assigned, mid, 0)) {
            res = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return res;
};

function isValid(jobs: number[], assigned: number[], target: number, index: number) {
    if (index === jobs.length) {
        return true;
    }

    for (let i = 0; i < assigned.length; i++) {
        assigned[i] += jobs[index];
        if (assigned[i] <= target && isValid(jobs, assigned, target, index + 1)) {
            return true;
        }
        assigned[i] -= jobs[index];
        if (assigned[i] === 0) {
            break;
        }
    }

    return false;
}

const testCases: [number[], number, number][] = [
    [[3, 2, 3], 3, 3],
    [[1, 2, 4, 7, 8], 2, 11]
];

for (const testCase of testCases) {
    const [jobs, k, expected] = testCase;
    console.log(minimumTimeRequired(jobs, k));
}

export { };