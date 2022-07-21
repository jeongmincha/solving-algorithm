function dfs(visited: boolean[][], grid: string[][], x: number, y: number): boolean {
    if (x < 0 || x > grid.length - 1 || y < 0 || y > grid[0].length - 1) {
        return false;
    }
    if (visited[x][y] === true) {
        return false;
    }
    if (grid[x][y] === "0") {
        return false;
    }
    visited[x][y] = true;
    dfs(visited, grid, x + 1, y);
    dfs(visited, grid, x, y + 1);
    dfs(visited, grid, x - 1, y);
    dfs(visited, grid, x, y - 1);
    return true;
}

function numIslands(grid: string[][]): number {
    const visited = [];
    for (let row = 0; row < grid.length; row++) {
        const rowVisited = [];
        for (let col = 0; col < grid[0].length; col++) {
            rowVisited.push(false);
        }
        visited.push(rowVisited);
    }

    let num = 0;

    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (visited[row][col] === false) {
                if (dfs(visited, grid, row, col) === true) {
                    num += 1;
                }
            }
        }
    }

    return num;
};

const testCases: [string[][], number][] = [
    [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        1
    ],
    [
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ],
        3
    ]
];

for (const testCase of testCases) {
    const [grid, expected] = testCase;
    console.log(numIslands(grid));
}

export { };