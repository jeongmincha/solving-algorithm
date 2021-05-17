# Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        ret = ""
        curr = self

        while curr is not None:
            ret += "{} -> ".format(curr.val)
            curr = curr.next

        return ret[:-4]


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        stack = []

        root = head
        curr = head
        prev = None
        idx = 0

        while curr is not None:
            if idx != 0 and idx % k == 0:
                new_curr = stack.pop()
                if idx == k:
                    root = new_curr
                else:
                    prev.next = new_curr

                while len(stack) > 0:
                    new_node = stack.pop()
                    new_curr.next = new_node
                    new_curr = new_node

                new_curr.next = curr
                prev = new_curr

            stack.append(curr)
            curr = curr.next
            idx += 1

        if len(stack) > 0 and idx % k == 0:
            new_curr = stack.pop()
            if idx == k:
                root = new_curr
            else:
                prev.next = new_curr

            while len(stack) > 0:
                new_node = stack.pop()
                new_curr.next = new_node
                new_curr = new_node

            new_curr.next = None

        return root


solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(head)
print(solution.reverseKGroup(head, 3))