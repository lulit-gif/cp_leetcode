class ListNode:
    def __init__(self,val=0, next =none):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        d = ListNode()
        cur = d

        while list1 and list2:
            if list1.val<list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next 
        cur.next = list1 if list1 else list2
        return d.next
    

    

   
    
    

       