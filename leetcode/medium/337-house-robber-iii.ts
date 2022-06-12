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

// f(root) = with root + without root
function findRobbingCandidates(root: TreeNode | null): number[] {
    if (root === null) {
        return [0, 0];
    }

    const lefts = findRobbingCandidates(root.left);
    const rights = findRobbingCandidates(root.right);

    return [
        root.val + lefts[1] + rights[1],
        Math.max(...lefts) + Math.max(...rights)
    ]
}

function rob(root: TreeNode | null): number {
    if (root === null) {
        return 0;
    }

    return Math.max(...findRobbingCandidates(root));
};

const testCases = [
    {
        root: new TreeNode(3, new TreeNode(2, null, new TreeNode(3)), new TreeNode(3, null, new TreeNode(1))),
        output: 7
    },
    {
        root: new TreeNode(3, new TreeNode(4, new TreeNode(1), new TreeNode(3)), new TreeNode(5, null, new TreeNode(1))),
        output: 9
    }
];

for (const testCase of testCases) {
    const { root, output } = testCase;
    // console.log(root);
    console.log(rob(root));
}

export { }