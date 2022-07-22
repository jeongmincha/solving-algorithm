from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        small_partition_current = ListNode(0)
        large_partition_current = ListNode(0)
        small_partition_first = None
        large_partition_first = None

        while current is not None:
            if current.val < x:
                if small_partition_first is None:
                    small_partition_first = current

                small_partition_current.next = current
                small_partition_current = current
            else:
                if large_partition_first is None:
                    large_partition_first = current

                large_partition_current.next = current
                large_partition_current = current

            current = current.next
        
        small_partition_current.next = large_partition_first
        large_partition_current.next = None

        if small_partition_first is None:
            return head
        else:
            return small_partition_first

test_cases = [
    [
        ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))),
        3,
        ListNode(1, ListNode(2, ListNode(2, ListNode(4, ListNode(3, ListNode(5))))))
    ],
    [
        ListNode(2, ListNode(1)),
        2,
        ListNode(1, ListNode(2)),
    ],
    [
        ListNode(1, ListNode(2, ListNode(3))),
        1,
        ListNode(1, ListNode(2, ListNode(3))),
    ],
    [
        ListNode(3, ListNode(2, ListNode(1))),
        3,
        ListNode(2, ListNode(1, ListNode(3))),
    ]
];

def print_list_nodes(head: Optional[ListNode]) -> str:
    nodes = []
    current = head
    while current is not None:
        nodes.append(str(current.val))
        current = current.next
    
    return ','.join(nodes)

for test_case in test_cases:
    head, x, expected = test_case
    print(print_list_nodes(Solution().partition(head, x)))
