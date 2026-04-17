class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        dup=set()
        for r,i in enumerate(s) :
            while s[r] in dup:
              dup.remove(s[l])
              l += 1
            dup.add(s[r])
            current=r-l+1
            if current>longest:
                longest=current
        return longest

        