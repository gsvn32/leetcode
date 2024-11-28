# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node=head
        visited=[]
        while(current_node):
            visited.append(current_node)
            current_node=current_node.next
            if(current_node and  current_node in visited):
                return current_node
        
        return None
