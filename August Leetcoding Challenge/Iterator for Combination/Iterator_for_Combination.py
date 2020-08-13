class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.llist = []
        charLen = len(characters) 
        flas=True
        self.llist.append(Node(0))
        self.head=1
        self.c=0
        for combo in combinations(characters,combinationLength):
            self.llist.append(Node(''.join(combo)))
            self.llist[self.c].next = self.llist[self.c+1]
            self.c+=1
        
    def next(self) -> str:
        result = self.llist[self.head].data
        self.head +=1
        return result
        

    def hasNext(self) -> bool:
        if(self.head<=self.c):
            if(self.llist[self.head-1].next!=None):
                return True
            else:
                return False
        else:
            return False
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()