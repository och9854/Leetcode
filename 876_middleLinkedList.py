class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        cnt = 0
        
        while curr is not None:
            cnt = cnt + 1
            curr = curr.next
        
        ans = int((cnt / 2)) + 1


        curr = head
        for i in range(1, ans):
            print(curr.val)
            curr = curr.next

        return curr
