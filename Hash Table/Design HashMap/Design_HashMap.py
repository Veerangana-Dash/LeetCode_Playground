class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val=val
        self.next=None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 100
        self.a=[None]*self.size
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        index = key%self.size
        if(self.a[index]==None):
            self.a[index] = ListNode(key,value)
        else:
            current_Node = self.a[index]
            #update value of head node to required key
            while True:
                if current_Node.key == key:
                    current_Node.val = value
                    return
                if current_Node.next == None:
                    break
                current_Node = current_Node.next
            
            current_Node.next = ListNode(key,value)
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index=key%self.size
        
        if self.a[index]==None:
            return -1
        else:
            current_Node = self.a[index]
            while current_Node:
                if current_Node.key == key:
                    return current_Node.val
                current_Node = current_Node.next
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index=key%self.size
        if self.a[index] != None:
            tempHead = self.a[index]
            if tempHead.key == key:
                self.a[index] = tempHead.next
            else:
                prevNode,current_Node = tempHead, tempHead.next
                while current_Node:
                    if current_Node.key == key:
                        prevNode.next = current_Node.next
                        break
                    prevNode = prevNode.next
                    current_Node = current_Node.next
                
        else:
            return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)