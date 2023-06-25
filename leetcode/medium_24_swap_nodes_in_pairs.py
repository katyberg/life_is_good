# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check empty head => pass
        # Check single node [1] => pass
        # Check odd/even number of nodes => pass
        # # Version 1
        # prev = None
        # curr = head
        # i = 0
        # # swap val with prev if curr is an even index (0 based)
        # while curr:
        #     if i % 2 == 1:
        #         prev.val, curr.val = curr.val, prev.val
        #     prev = curr
        #     curr = curr.next
        #     i += 1
        # return head

        # Version 2
        new_head = prev = None
        curr = head
        i = 0
        # swap val with prev if curr is an even index (0 based)
        while curr:
            if i % 2 == 1:
                next_node = curr.next  # first memorize next starting point so we don't lose it
                curr.next = prev
                prev.next = next_node
                curr = next_node  # prev does not change
            else:
                prev = curr
                curr = curr.next
            if i == 1:
                new_head = curr
            i += 1
        return head

        # # Recursive version: I like it!
        # if head and head.next:  # <== not this end condition!
        #     temp=head.val
        #     head.val=head.next.val
        #     head.next.val=temp
        #     self.swapPairs(head.next.next)
        # return head

