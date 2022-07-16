function makeAdj(n: number, edges: number[][]): number[][] {
    const adj: number[][] = [];
    for (let i = 0; i < n; i++) {
        adj.push([]);
    }
    for (const edge of edges) {
        adj[edge[0]].push(edge[1]);
        adj[edge[1]].push(edge[0]);
    }
    return adj;
}

function countPairs(n: number, edges: number[][]): number {
    const adj: number[][] = makeAdj(n, edges);

    let numConnectedNodes: number = 0;
    const visited = new Array(n).fill(false);
    const dfs = function (v: number) {
        if (visited[v] === true) {
            return;
        }
        visited[v] = true;
        numConnectedNodes += 1;
        adj[v].forEach(c => {
            dfs(c);
        });
    };

    const components: number[] = [];
    for (let i = 0; i < n; i++) {
        if (visited[i] === false) {
            dfs(i);
            components.push(numConnectedNodes);
            numConnectedNodes = 0;
        }
    }

    let result = 0;
    for (const component of components) {
        result += (n - component) * component;
        n -= component;
    }

    return result;
};

const testCases = [
    [3, [[0, 1], [0, 2], [1, 2]], 0],
    [7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]], 14]
];

for (const testCase of testCases) {
    const [n, edges, expected] = testCase;
    console.log(countPairs(n as number, edges as number[][]));
}

export { };