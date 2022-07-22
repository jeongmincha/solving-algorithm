import math
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        current1 = l1
        current2 = l2
        current = root
        carry = 0

        while current1 is not None or current2 is not None or carry > 0:
            current_sum = (current1.val if current1 is not None else 0) + \
                (current2.val if current2 is not None else 0) + \
                carry
            carry = math.floor(current_sum / 10)
            current.next = ListNode(current_sum % 10)

            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next
            
            current = current.next
        
        return root.next

test_cases = [
    [
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4))),
        ListNode(7, ListNode(0, ListNode(8))),
    ],
    # [
    #     ListNode(0),
    #     ListNode(0),
    #     ListNode(0)
    # ],
    [
        ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
        None
    ]
]

def print_list_nodes(head):
    nodes = []
    current = head
    while current is not None:
        nodes.append(str(current.val))
        current = current.next
    return ','.join(nodes)

for test_case in test_cases:
    l1, l2, expected = test_case
    print(print_list_nodes(Solution().addTwoNumbers(l1, l2)))