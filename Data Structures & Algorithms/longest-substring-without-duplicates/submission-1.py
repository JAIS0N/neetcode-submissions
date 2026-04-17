class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        char=set()
        l=0
        for i,n in enumerate(s):
            while n in char:
                char.remove(s[l])
                l=l+1
            char.add(n)
            current=i-l+1
            longest=max(longest,current)
        return longest

        