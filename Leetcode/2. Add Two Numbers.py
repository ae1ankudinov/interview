'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''


def print_linked_list(node):
    while node:
        print(node.val, ' --> ', end='')
        node = node.next

def reverse_linked_list(node):
    prev = None
    cur = node
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    node = prev

    return node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity - O(l1+l2) = O(n)
# Space complexity - O(max(l1, l2)) = O(n)
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        dummy = cur = ListNode()
        s = 0
        while l1 and l2:
            s += (l1.val + l2.val)
            cur.next = ListNode(s%10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
            s //= 10

        while l1:
            s += l1.val
            cur.next = ListNode(s % 10)
            cur = cur.next
            l1 = l1.next
            s //= 10

        while l2:
            s += l2.val
            cur.next = ListNode(s % 10)
            cur = cur.next
            l2 = l2.next
            s //= 10

        return dummy.next




l1_3 = ListNode(3)
l1_2 = ListNode(4, l1_3)
l1_1 = ListNode(2, l1_2)

l2_3 = ListNode(4)
l2_2 = ListNode(6, l2_3)
l2_1 = ListNode(5, l2_2)

s = Solution()
print_linked_list(s.addTwoNumbers(l1_1, l2_1))

