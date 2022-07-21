class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    const fakeHead = new ListNode(0);
    fakeHead.next = head;

    let before = fakeHead;
    let prev: ListNode | null = fakeHead;
    for (let i = 0; i < left - 1; i++) {
        before = before.next as ListNode;
    }

    let start = before.next;
    let current = start;

    for (let i = 0; i < right - left + 1; i++) {
        const nextNode = current?.next ?? null;
        if (current)
            current.next = prev;
        prev = current;
        current = nextNode;
    }

    before.next = prev;
    if (start)
        start.next = current;

    return fakeHead.next;
};

function printListNodes(root: ListNode | null): string {
    const values = [];
    let current = root;
    while (current != null) {
        values.push(current.val);
        current = current.next;
    }
    return values.join(', ');
}

const testCases: [ListNode | null, number, number, ListNode | null][] = [
    [
        new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))),
        2,
        4,
        new ListNode(1, new ListNode(4, new ListNode(3, new ListNode(2, new ListNode(5)))))
    ],
    [
        new ListNode(5),
        1,
        1,
        new ListNode(5)
    ]
];

for (const testCase of testCases) {
    const [head, left, right, expected] = testCase;
    console.log(printListNodes(reverseBetween(head, left, right)));
}

export { };