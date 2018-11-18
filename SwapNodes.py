"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """

    def swapPairs(self, head):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        node = dummy

        while (node.next and node.next.next is not None):
            First = node.next
            Second = node.next.next

            First.next = Second.next
            Second.next = First
            node.next = Second
            node = node.next.next

        return dummy.next
