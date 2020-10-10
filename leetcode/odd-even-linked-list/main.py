import unittest

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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None: return None
        odd = head
        even = head.next
        first_even = even

        while True:
            if (odd is None) or (even is None) or (even.next is None):
                odd.next = first_even
                break
            
            odd.next = even.next
            odd = even.next

            if odd.next is None:
                even.next = None
                odd.next = first_even
                break
            
            even.next = odd.next
            even = odd.next
        
        return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testOddEvenList(self):
        root = ListNode.makeList([1,2,3,4,5])
        actual = self.solution.oddEvenList(root)
        expected = ListNode.makeList([1,3,5,2,4])
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()