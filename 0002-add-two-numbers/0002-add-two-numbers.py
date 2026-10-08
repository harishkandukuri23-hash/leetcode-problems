# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dum=ListNode()
        temp=dum
        car=0
        while l1 or l2 :
            sum=car
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            n=ListNode(sum%10)
            dum.next=n
            dum=dum.next
            car=sum//10
        if car:
            dum.next=ListNode(car)
        return temp.next
