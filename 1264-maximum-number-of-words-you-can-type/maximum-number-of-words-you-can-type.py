class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broke = set(brokenLetters)
        count = 0
        for word in text.split():
            if not any(ch in broke for ch in word):
             count +=1
        return count        
        