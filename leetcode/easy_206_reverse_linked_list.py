# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # Iteratively using a stack
# from collections import deque
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
#         stack = deque()
#         while head:
#             stack.append(head)
#             head = head.next
#         if stack:
#             head = stack.pop()
#             cur = head
#         while stack:
#             node = stack.pop()
#             cur.next = node
#             cur = node
#         cur.next = None
#         return head

#Iteratively using three pointers
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        return prev

# # Recursively
# # This solution essentially relies on the call stack to memorize the pointer to each element!!!!
# # It's slower!
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return p

