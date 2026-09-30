"""21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 """
#List
"""list1 = [1,2,4]
list2 = [1,3,4]
i=0;j=0
list3=[]
while i<len(list1) and j<len(list2):
    if list1[i]<=list2[j]:
        list3.append(list1[i])
        i=i+1
    else:
        list3.append(list2[j])
        j=j+1
while i<len(list1):
    list3.append(list1[i])
    i=i+1
while j<len(list2):
    list3.append(list2[j])
    j=j+1
print(list3)"""

#Linked List

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def mergeLists(list1,list2):
    dummy=ListNode()
    tail=dummy
    while list1 and list2:
        if list1.val<=list2.val:
            tail.next=list1
            list1=list1.next
        else:
            tail.next=list2
            list2=list2.next
        tail=tail.next
    if list1:
        tail.next=list1
    else:
        tail.next=list2
    return dummy.next


def createLinkedlist(values):
    dummy=ListNode()
    tail=dummy
    for v in values:
        tail.next=ListNode(v)
        tail=tail.next
    return dummy.next
def printLinkedList(list):
    while list:
        print(list.val,end="-->")
        list=list.next
    print("None")
    


list1=[1,2,3]
list2=[1,4,5]
h1=createLinkedlist(list1)
h2=createLinkedlist(list2)
printLinkedList(mergeLists(h1,h2))