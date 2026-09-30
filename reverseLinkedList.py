"""206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []"""


class LinkNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def reverse(head):
    prev=None
    current=head
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    return prev

def createList(values):
    dummy=LinkNode()
    tail=dummy
    for v in values:
        tail.next=LinkNode(v)
        tail=tail.next
    return dummy.next
def printList(head):
    while head:
        print(head.val,end="-->")
        head=head.next
    print("None")
l=[1,2,3,4,5]
l1=createList(l)
printList(reverse(l1))