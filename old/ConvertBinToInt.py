'''

Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.

The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Example-1:
    Input: head = [1,0,1]
    Output : 5
    Explanation: (101) in base 2 = (5) in base 10

Example-2:
    Example 2:
    Input: head = [0]
    Output: 0
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def findLinkedListSize(self,head:ListNode):
        temp = head
        size = 0
        while(temp!=None):
            size+=1
            temp = temp.next
        return size-1

    def getDecimalValue(self, head: ListNode) -> int:
        expVal = self.findLinkedListSize(head)
        # print(numDigits)
        temp = head
        res = 0
        while(temp!=None):
            res+=(2**expVal)*temp.val
            temp = temp.next
            expVal-=1
        # print(res)
        return res
