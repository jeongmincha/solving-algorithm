// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
    }
}

function kthSmallest(root: TreeNode | null, k: number): number {
    let nVisited = 0;
    let stack = [];
    let current = root;

    while (current || stack.length > 0) {
        while (current) {
            stack.push(current);
            current = current.left;
        }
        current = stack.pop() as TreeNode;
        nVisited += 1;
        if (nVisited === k)
            return current.val;

        current = current.right;
    }

    return 0;
};

const testCases: [TreeNode | null, number, number][] = [
    [
        new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4)),
        1,
        1
    ],
    [
        new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4)),
        2,
        2
    ],
    [
        new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4)),
        3,
        3
    ],
    [
        new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4)),
        4,
        4
    ]
];

for (const testCase of testCases) {
    const [root, k, expected] = testCase;
    const answer = kthSmallest(root, k);
    console.assert(
        answer === expected,
        `${answer}, ${expected}`
    )
}

export { };