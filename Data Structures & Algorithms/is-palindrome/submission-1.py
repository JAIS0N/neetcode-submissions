class Solution:
    def isPalindrome(self, s: str) -> bool:
        sent=""
        for c in s:
            if c.isalnum(): 
                sent=sent+c.lower()
        i = 0
        j = len(sent) - 1
        while i < j:
            if sent[i] != sent[j]:
                return False
            i += 1
            j -= 1
        return True


        