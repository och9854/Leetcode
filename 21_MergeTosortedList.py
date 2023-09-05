# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        final_result = ListNode()
        result = final_result
        
        # while both of cur1 and cur2 exist
        while cur1 != None and cur2 != None:
            # compare value
                if cur1.val < cur2.val:
                    # add cur1.val, cur1.next to result
                    result.next = cur1
                    cur1 = cur1.next
                else:
                    result.next = cur2
                    cur2 = cur2.next
                result = result.next 
        # while one of the list is none
        result.next = cur1 if cur1 is not None else cur2
    
    
        return final_result.next
            
        
# Answer1 : Recursion
'''
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
'''

# Answer2: Iteration
'''
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next
'''

# Feedback
## Clarify what to return
## 