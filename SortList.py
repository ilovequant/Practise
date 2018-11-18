'''
4 ->2 ->1 ->3

use merge sort, because here linkedlist is given, can not visit each element flexiblely

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        if not head.next:
            return head

        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(slow)

        return self.mergeList(list1, list2)

    def mergeList(self, list1, list2):
        if not list1 or not list2:
            return list2 or list1

        if list1.val < list2.val:
            list1.next = self.mergeList(list1.next, list2)
            return list1

        if list1.val >= list2.val:
            list2.next = self.mergeList(list1, list2.next)
            return list2

    '''
    iterative way
    '''

    def mergeList(self, list1, list2):
        head = ListNode(0)
        sentinel = head

        while (list1 and list2):
            if list1.val < list2.val:
                sentinel.next = list1
                list1 = list1.next

            else:
                sentinel.next = list2
                list2 = list2.next

            sentinel = sentinel.next

        sentinel.next = list1 if list1 else list2

        return head.next


    '''
    in-place iterative
    '''

    def mergeList(self, list1, list2):
        head = ListNode(0)
        sentinel = head
        head.next = list1

        while (list1 and list2):
            if list1.val < list2.val:
                list1 = list1.next

            else:
                temp1 = head.next
                head.next = list2
                temp2 = list2.next
                list2.next = temp1
                list2 = temp2

            head = head.next

        head.next = list1 if list1 else list2

        return sentinel.next
