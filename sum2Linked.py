"""class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry=0
        dummy=ListNode()
        l3=dummy
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            n=val1+val2+carry
            carry=n//10
            digit=n%10
            l3.next=ListNode(digit)
            l3=l3.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
"""


n=243
m=564
print(list(str(n+m)))

