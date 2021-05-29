# Problem: https://leetcode.com/problems/swap-nodes-in-pairs/

import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def fromArray(arr: List[int]):
        current = ListNode(None)
        root = current
        for num in arr:
            current.next = ListNode(num)
            current = current.next
        return root.next
    
    @staticmethod
    def toArray(node) -> List[int]:
        arr = []
        current = node
        while current is not None:
            arr.append(current.val)
            current = current.next
        return arr


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        root = ListNode(-1)
        root.next = head
        p1 = root

        while p1 and p1.next and p1.next.next:
            temp = p1.next.next.next
            p1.next.next.next = p1.next
            p1.next = p1.next.next
            p1 = p1.next.next
            p1.next = temp

        return root.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSwapPairs(self):
        test_cases = [
            {
                'head': [1,2,3,4],
                'output': [2,1,4,3]
            },
            {
                'head': [],
                'output': []
            },
            {
                'head': [1],
                'output': [1]
            },
            {
                'head': [1,2,3],
                'output': [2,1,3]
            },
            # {
            #     'head': [1,2],
            #     'output': [2,1]
            # }
        ]
        for test_case in test_cases:
            head = ListNode.fromArray(test_case['head'])
            expected = test_case['output']
            answer = self.solution.swapPairs(head)
            answer = ListNode.toArray(answer)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
