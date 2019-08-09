class Solution:
    def length_list(self,head):
        length = 1
        current_node = head
        while current_node.next != None:
            length += 1
            current_node = current_node.next
        return length

    def middleNode(Self,head:ListNode) -> ListNode:
        length = self.length_list(head)
        middle = int(length/2)
        current_node = head
        for i in range(middle):
            current_node = current_node.next
        return current_node
