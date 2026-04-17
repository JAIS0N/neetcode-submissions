class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freq = [0] * 128

        for c in t:
                freq[ord(c)] += 1

        left = 0
        required = len(t)
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
                if freq[ord(s[right])] > 0:
                        required -= 1
                freq[ord(s[right])] -= 1

                while required == 0:
                        if right - left + 1 < min_len:
                                min_len = right - left + 1
                                start = left

                        freq[ord(s[left])] += 1
                        if freq[ord(s[left])] > 0:
                                required += 1
                        left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]
