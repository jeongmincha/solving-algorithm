# Problem: https://leetcode.com/problems/merge-two-sorted-lists/

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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        current = root

        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                current = current.next
                p1 = p1.next
            else:
                current.next = p2
                current = current.next
                p2 = p2.next
        
        while p1:
            current.next = p1
            current = current.next
            p1 = p1.next
        
        while p2:
            current.next = p2
            current = current.next
            p2 = p2.next

        return root.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testMergeTwoLists(self):
        test_cases = [
            {
                'l1': [1,2,4],
                'l2': [1,3,4],
                'output': [1,1,2,3,4,4]
            },
            {
                'l1': [],
                'l2': [],
                'output': []
            },
            {
                'l1': [],
                'l2': [0],
                'output': [0]
            }
        ]
        for test_case in test_cases:
            l1 = ListNode.fromArray(test_case['l1'])
            l2 = ListNode.fromArray(test_case['l2'])
            expected = test_case['output']
            answer = self.solution.mergeTwoLists(l1, l2)
            answer = ListNode.toArray(answer)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
