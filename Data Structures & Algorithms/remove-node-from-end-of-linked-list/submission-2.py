# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverselis(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        

        def remove(h, n):
            dummy = ListNode(0, h)
            curr = dummy
            count = 0
            while curr.next:
                count += 1
                if count == n:
                    curr.next = curr.next.next
                    break
                curr = curr.next
            return dummy.next
        
        h = reverselis(head)
        h = remove(h,n)
        h = reverselis(h)
        return h

        