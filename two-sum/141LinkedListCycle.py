# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# this solution is O(n) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_node=head
        visited=[]
        while(current_node):
            visited.append(current_node)
            current_node=current_node.next
            if(current_node and  current_node in visited):
                return True
        
        return False
