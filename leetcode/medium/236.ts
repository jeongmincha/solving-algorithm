// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

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

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    if (root === null || root.val === p?.val || root.val === q?.val) {
        return root;
    }
    const left = lowestCommonAncestor(root.left, p, q);
    const right = lowestCommonAncestor(root.right, p, q);

    if (!left) {
        return right;
    } else if (!right) {
        return left;
    } else {
        return root;
    }
};

const testCases: [TreeNode | null, TreeNode | null, TreeNode | null, TreeNode | null][] = [
    [
        new TreeNode(3, new TreeNode(5, new TreeNode(6), new TreeNode(2, new TreeNode(7), new TreeNode(4))), new TreeNode(1, new TreeNode(0), new TreeNode(8))),
        new TreeNode(5, new TreeNode(6), new TreeNode(2, new TreeNode(7), new TreeNode(4))),
        new TreeNode(1, new TreeNode(0), new TreeNode(8)),
        new TreeNode(3, new TreeNode(5, new TreeNode(6), new TreeNode(2, new TreeNode(7), new TreeNode(4))), new TreeNode(1, new TreeNode(0), new TreeNode(8))),
    ]
];

for (const testCase of testCases) {
    const [root, p, q, expected] = testCase;
    console.log(lowestCommonAncestor(root, p, q));
}

export { };