# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwo(lis1,lis2):
            if not lis1 and not lis2:
                return None
            if not lis1:
                return lis2
            if not lis2:
                return lis1
            dummy = ListNode(0)
            curr = dummy
            while lis1 and lis2:
                if lis1.val > lis2.val:
                    curr.next = lis2
                    lis2 = lis2.next
                    curr = curr.next
                else:
                    curr.next = lis1
                    lis1 = lis1.next
                    curr = curr.next
            curr.next = lis1 if lis1 else lis2
            return dummy.next



        while len(lists) > 1:
            lis1 = lists.pop()
            lis2 = lists.pop()
            lists.append(mergetwo(lis1,lis2))
        return lists[0] if lists else None
        