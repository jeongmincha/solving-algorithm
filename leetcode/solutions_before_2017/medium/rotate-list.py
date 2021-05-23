# Problem: https://leetcode.com/problems/rotate-list/

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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None

        fast = head
        slow = head
        n = 0
        while fast is not None:
            n += 1
            fast = fast.next

        k %= n
        fast = head
        for _ in range(k):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        if slow.next:
            new_head = slow.next
            fast.next = head
            slow.next = None
            return new_head
        else:
            return head


class Solution2:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None

        node = head
        array = []
        while node is not None:
            array.append(node.val)
            node = node.next
        n = len(array)
        k %= n
        array = array[n - k :] + array[: n - k]

        root = ListNode(array[0])
        node = root
        for idx in range(1, n):
            node.next = ListNode(array[idx])
            node = node.next
        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.solution2 = Solution2()

    def testRotateRight(self):
        root = ListNode(1)
        root.next = ListNode(2)
        root.next.next = ListNode(3)
        root.next.next.next = ListNode(4)
        root.next.next.next.next = ListNode(5)
        k = 2
        expected = ListNode(4)
        expected.next = ListNode(5)
        expected.next.next = ListNode(1)
        expected.next.next.next = ListNode(2)
        expected.next.next.next.next = ListNode(3)
        actual = self.solution.rotateRight(root, k)
        self.assertTrue(ListNode.equalList(actual, expected))

    def testRotateRight2(self):
        root = ListNode(1)
        root.next = ListNode(2)
        root.next.next = ListNode(3)
        root.next.next.next = ListNode(4)
        root.next.next.next.next = ListNode(5)
        k = 2
        expected = ListNode(4)
        expected.next = ListNode(5)
        expected.next.next = ListNode(1)
        expected.next.next.next = ListNode(2)
        expected.next.next.next.next = ListNode(3)
        actual2 = self.solution2.rotateRight(root, k)
        self.assertTrue(ListNode.equalList(actual2, expected))


if __name__ == "__main__":
    unittest.main()