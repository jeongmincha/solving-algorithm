# Problem: https://leetcode.com/problems/add-two-numbers/

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def convertArray(arr):
        root = ListNode(-1)
        current = root

        for num in arr:
            current.next = ListNode(num)
            current = current.next

        return root.next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return TypeError

        current_self = self
        current_other = other

        while current_self is not None and current_other is not None:
            if current_self.val != current_other.val:
                return False

            current_self = current_self.next
            current_other = current_other.next

            if (current_self is not None and current_other is None) or (
                current_self is None and current_other is not None
            ):
                return False

        return True

    def __str__(self):
        string = ""
        current = self
        while current is not None:
            string += "{}, ".format(current.val)
            current = current.next
        return string[:-2]


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_l1 = l1
        current_l2 = l2

        root = ListNode(-1)
        current = root
        round_up = 0

        while (current_l1 is not None) or (current_l2 is not None) or (round_up != 0):
            if current_l1 is None and current_l2 is None:
                if round_up == 1:
                    current.next = ListNode(1)
                    break

            current_val = round_up
            if current_l1 is not None:
                current_val += current_l1.val
            if current_l2 is not None:
                current_val += current_l2.val

            current.next = ListNode(current_val % 10)

            if current_val >= 10:
                round_up = 1
            else:
                round_up = 0

            if current_l1 is not None:
                current_l1 = current_l1.next
            if current_l2 is not None:
                current_l2 = current_l2.next

            current = current.next

        return root.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testAddTwoNumbers(self):
        test_cases = [
            {
                "l1": ListNode.convertArray([2, 4, 3]),
                "l2": ListNode.convertArray([5, 6, 4]),
                "expected": ListNode.convertArray([7, 0, 8]),
            },
            {
                "l1": ListNode.convertArray([0]),
                "l2": ListNode.convertArray([0]),
                "expected": ListNode.convertArray([0]),
            },
            {
                "l1": ListNode.convertArray([9, 9, 9, 9, 9, 9, 9]),
                "l2": ListNode.convertArray([9, 9, 9, 9]),
                "expected": ListNode.convertArray([8, 9, 9, 9, 0, 0, 0, 1]),
            },
        ]
        for test_case in test_cases:
            l1 = test_case["l1"]
            l2 = test_case["l2"]
            expected = test_case["expected"]
            answer = self.solution.addTwoNumbers(l1, l2)

            self.assertEqual(expected, answer)


if __name__ == "__main__":
    unittest.main()
