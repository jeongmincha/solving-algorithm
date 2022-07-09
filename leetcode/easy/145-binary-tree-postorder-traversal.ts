class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

function postorderTraversal(root: TreeNode | null): number[] {
    if (root === null) {
        return [];
    }
    const result: number[] = [];

    const left = root.left;
    const right = root.right;
    const current = root.val;

    if (left !== null) {
        result.push(...postorderTraversal(left));
    }
    if (right !== null) {
        result.push(...postorderTraversal(right));
    }
    result.push(current);

    return result;
};

const testCases: [TreeNode | null, number[]][] = [
    [
        new TreeNode(
            1,
            null,
            new TreeNode(
                2,
                new TreeNode(3)
            )
        ),
        [3, 2, 1]
    ],
    [null, []],
    [new TreeNode(1), [1]],
    [
        new TreeNode(
            1,
            new TreeNode(
                2,
                new TreeNode(3),
                new TreeNode(4)
            ),
            new TreeNode(
                5,
                new TreeNode(6),
                new TreeNode(7)
            )
        ),
        [3, 4, 2, 6, 7, 5, 1]
    ],
];

for (const testCase of testCases) {
    const [root, expected] = testCase;
    const actual = postorderTraversal(root as TreeNode);

    if (!(actual > expected && actual < expected)) {
        console.log('[CORRECT] ', actual);
    } else {
        console.log('[WRONG]');
        console.log(' - actual: ', actual);
        console.log(' - expected: ', expected);
    }
}

export { };