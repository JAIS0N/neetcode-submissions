class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = [0] * 26
        freq_window = [0] * 26

        for char in s1:
            freq_s1[ord(char) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):
            freq_window[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > len(s1):
                freq_window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if freq_window == freq_s1:
                return True

        return False
