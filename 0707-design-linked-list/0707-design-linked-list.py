class Node:
    def __init__(self, val=None , next=None):
        self.val = val
        self.next  = None
    
    

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
        

    def get(self, index: int) -> int:
        # if index == 0 and self.head is not None:
        #     return self.head.val
        if  index < 0 or index >= self.size :
            return -1
        if self.head is None:
            return -1
    
        temp = self.head 
           
        for _ in range(index):
            temp = temp.next

        # return temp.val
        return temp.val

        

    def addAtHead(self, val: int) -> None:
        # temp = self.head
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        temp = self.head
        node = ListNode(val)
        if temp is None:
            self.head = node
        else:

            while temp.next:
                temp = temp.next
            temp.next = node
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        
        
        if index < 0 or index > self.size:
            return 
        if index == 0:
            self.addAtHead(val)
        else:
            temp = self.head
            node = ListNode(val)
            for _ in range(index-1):
                temp = temp.next
            # saver = temp.next
            node.next = temp.next
            temp.next = node
            # temp.next = node
            # node.next = saver
            self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            # the head will be the one after the prev head 
        else:
            for _ in range(index-1):
                temp = temp.next
            temp.next = temp.next.next
        self.size-=1
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)