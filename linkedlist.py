# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if len(l1) >= len(l2):
        #     longest_list = l1
        # else:
        #     longest_list = l2

        # for i in longest_list:
        #     # Base case 
        #     sum = l1[i] + l2[i]
            
        link_list = ListNode()
        current = link_list
        left = 0

        while l1 is not None or l2 is not None or left: # Think of None like: "Is the thing I am holding in my hand right now real?"
            # var1 = l1.val
            # var2 = l2.val

            # if var2 == 0 or var2 == 0:
            #     return 0
            if l1 is not None:
                val1 = l1.val
            else:
                val1 = 0
            if l2 is not None:
                val2 = l2.val
            else:
                val2 = 0

            sum = val1 + val2 + left
            left = sum // 10 # Get a left over value
            total = sum % 10 # Get a total value
            current.next = ListNode(total)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next 

        return link_list.next
