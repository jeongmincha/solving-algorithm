# Problem: https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = []
        length = 0
        cur = root
        while cur is not None:
            cur = cur.next
            length += 1

        cur = root
        for i in range(k):
            elem = []
            step = int(length / k)
            if i < length % k:
                step += 1

            for _ in range(step):
                elem.append(cur.val)
                cur = cur.next
            res.append(elem)
        return res


if __name__ == "__main__":
    sol = Solution()
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l = ListNode(lst[0])
    cur = l
    for i in range(1, len(lst)):
        cur.next = ListNode(lst[i])
        cur = cur.next
    k = 3
    print(sol.splitListToParts(l, k))
