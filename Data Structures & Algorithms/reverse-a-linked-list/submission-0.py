# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr != None:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr != None:
            val = stack.pop()
            curr.val = val
            curr = curr.next
        return head
