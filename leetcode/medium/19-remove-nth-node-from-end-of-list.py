# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        fast = current

        for _ in range(n):
            fast = fast.next
        
        found = False
        while fast is not None:
            if fast.next is None:
                found = True
                temp = current.next.next
                current.next = temp

            current = current.next
            fast = fast.next
        
        if found:
            return head
        else:
            return head.next



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testRemoveNthFromEnd(self):
        test_cases = [
            {
                'head': [1,2,3,4,5],
                'n': 2,
                'output': [1,2,3,5]
            },
            {
                'head': [1],
                'n': 1,
                'output': []
            },
            {
                'head': [1,2],
                'n': 1,
                'output': [1]
            }
        ]
        for test_case in test_cases:
            head = ListNode.fromArray(test_case['head'])
            n = test_case['n']
            expected = test_case['output']
            answer = self.solution.removeNthFromEnd(head, n)
            answer = ListNode.toArray(answer)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
