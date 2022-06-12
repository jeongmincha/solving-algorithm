class ListNode {
    val: Number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

function reverseList(head: ListNode | null): ListNode | null {
    if (head === null) {
        return null;
    }
    if (head.next === null) {
        return head;
    }

    let current = null;
    while (head !== null) {
        current = new ListNode(Number(head.val), current);
        head = head.next;
    }

    return current;
};

const testCases = [
    [
        new ListNode(1, new ListNode(2)),
        new ListNode(2, new ListNode(1))
    ],
    [
        new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))),
        new ListNode(5, new ListNode(4, new ListNode(3, new ListNode(2, new ListNode(1))))),
    ],
    [null, null]
];

for (let index = 0; index < testCases.length; index++) {
    const [head, output] = testCases[index];
    console.dir(reverseList(head));
}

export { };