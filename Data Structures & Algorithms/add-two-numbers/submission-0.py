# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(root):
            curr = root
            num = 0
            mod = 1
            while curr != None:
                num += curr.val * mod
                mod *= 10
                curr = curr.next
            return num
        num1 = traverse(l1)
        num2 = traverse(l2)
        def generate(num):
            root = ListNode(num % 10)
            num //= 10
            curr = root
            while num > 0:
                curr.next = ListNode(num % 10)
                curr = curr.next
                num //=10
            return root
        return generate(num1+num2)

