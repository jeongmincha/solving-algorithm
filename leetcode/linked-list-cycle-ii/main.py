import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_ptr = head
        fast_ptr = head
        prev_fast_ptr = fast_ptr
        
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            prev_fast_ptr = slow_ptr
            fast_ptr = fast_ptr.next.next

            if slow_ptr is fast_ptr:
                break

        if fast_ptr is None or fast_ptr.next is None:
            return None
        
        slow_ptr = head
        while slow_ptr is not fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        return slow_ptr



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testDetectCycle(self):
        root = start = ListNode(1)
        root.next = ListNode(2)
        root.next.next = start

        actual = self.solution.detectCycle(root)
        expected = start
        self.assertEqual(actual, expected)

    def testDetectCycle2(self):
        root = ListNode(3)
        root.next = start = ListNode(2)
        root.next.next = ListNode(0)
        root.next.next.next = ListNode(4)
        root.next.next.next = start
        
        actual = self.solution.detectCycle(root)
        expected = start
        self.assertEqual(actual.val, expected.val)

if __name__ == "__main__":
    unittest.main()
        