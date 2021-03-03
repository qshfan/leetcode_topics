# 0024_swap_nodes_in_pairs.py
# Medium
# Keys: #recursion #linkedlist


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head

    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        def helper(node):
            if node.next and node.next.next:
                tmp = node.next
                node.next = node.next.next
                tmp.next = node.next.next
                node.next.next = tmp
                helper(node.next.next)

        helper(dummy)

        return dummy.next