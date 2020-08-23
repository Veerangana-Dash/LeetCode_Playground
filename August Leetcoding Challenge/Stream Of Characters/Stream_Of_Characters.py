
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.store = collections.defaultdict(set)
        self.charlist = ''
        for w in words:
            self.store[w[-1]].add(w)
        

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.charlist += letter
        for i in self.store[letter]:
            start = len(i)
            if(i in self.charlist[-start:]):
                return True
            
        return False
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)   