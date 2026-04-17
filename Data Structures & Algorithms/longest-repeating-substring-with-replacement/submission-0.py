class Solution:
    def characterReplacement(self,s: str, k: int) -> int:
    
        left = 0
        max_frequency = 0
        freq_map = {} 
        for right in range(len(s)):
            
            char_right = s[right]

            freq_map[char_right] = freq_map.get(char_right, 0) + 1
            max_frequency = max(max_frequency, freq_map[char_right])
            replacements_needed = (right - left + 1) - max_frequency
            if replacements_needed > k:
                char_left = s[left]
                freq_map[char_left] -= 1
                left += 1
    
        return (len(s) - 1) - left + 1