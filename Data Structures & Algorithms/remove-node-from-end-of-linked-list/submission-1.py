# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverse_linked_list(head)
       
        i = 1
        
        curr = head
        prev = None
        next_node = None

        while curr != None:
            next_node = curr.next
            if i == n:
                if next_node is not None and prev is not None:
                    prev.next = next_node
                    break
                elif prev is None:
                    head = curr.next
                    break
                else:
                    prev.next = None
            prev = curr
            curr = curr.next
            i+= 1
        head = self.reverse_linked_list(head)
        return head

    def reverse_linked_list(self, head):
        if head == None:
            return None
        pre = None
        curr = head
    
        while curr != None:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        return pre
    def print_list(self,head):
        curr = head
        print("[",end=" ")
        while curr != None:
            print(curr.val, end=" ")
            curr = curr.next
        print("]")
