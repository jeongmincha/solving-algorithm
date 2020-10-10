import unittest
# from typings import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        result = ""
        node = self
        while node != None:
            result += str(node.val) + "->"
            node = node.next
        return result[:-2]
    
    def __eq__(self, other):
        if other is None: return False
        node = self
        while node != None and other != None:
            if node.val != other.val:
                return False
            node = node.next
            other = other.next
        return True

    @classmethod
    def makeList(cls, lst):
        head = ListNode(lst[0])
        node = head
        for elem in lst[1:]:
            node.next = ListNode(elem)
            node = node.next
        return head


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        p = dummy = ListNode(0)
        dummy.next = head

        for _ in range(m-1):
            p = p.next
        
        curr, prev = p.next, None

        for _ in range(n-m+1):
            curr.next, prev, curr = prev, curr, curr.next
        p.next.next = curr
        p.next = prev

        return dummy.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testReverseBetween(self):
        root = ListNode.makeList([1,2,3,4])
        actual = self.solution.reverseBetween(root, 2, 3)
        expected = ListNode.makeList([1,3,2,4])
        self.assertEqual(actual, expected)
    
    def testReverseBetween2(self):
        root = ListNode.makeList([3,5])
        actual = self.solution.reverseBetween(root, 1, 2)
        expected = ListNode.makeList([5,3])
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()