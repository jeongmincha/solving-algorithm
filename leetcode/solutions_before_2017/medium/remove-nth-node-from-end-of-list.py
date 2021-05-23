# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

import unittest

# Definition for singly-linked list.
class ListNode:
    @classmethod
    def equalList(cls, x, y):
        curr_x = x
        curr_y = y

        while curr_x is not None:
            if curr_x.val != curr_y.val:
                return False
            curr_x = curr_x.next
            curr_y = curr_y.next

        return True

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        # remove the first node
        if fast is None:
            return head.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testRemoveNthFromEnd(self):
        root = ListNode(1)
        root.next = ListNode(2)
        root.next.next = ListNode(3)
        root.next.next.next = ListNode(4)
        root.next.next.next.next = ListNode(5)
        n = 2
        expected = ListNode(1)
        expected.next = ListNode(2)
        expected.next.next = ListNode(3)
        expected.next.next.next = ListNode(5)
        actual = self.solution.removeNthFromEnd(root, n)

        self.assertTrue(ListNode.equalList(actual, expected))


if __name__ == "__main__":
    unittest.main()