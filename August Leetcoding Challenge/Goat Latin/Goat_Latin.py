class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        a = 'a'
        ma = 'ma'
        goat = ''
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        for word in words:
            if word[0] in vowels:
                word = word + ma + a
                
            else:
                word = word[1:] + word[0] + ma + a
                
            a = a + 'a'
            goat = goat + word + ' '
            
        return goat[:-1]
            
        