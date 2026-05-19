class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0
        
        # r will automatically slide from left to right
        for r in range(len(s)):
            
            # If we find a duplicate, shrink the window from the left
            # UNTIL the duplicate is completely removed from the window.
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                
            # Add the new character to our window
            char_set.add(s[r])
            
            # Calculate the length of our current valid window
            # Length of a window is always (right - left + 1)
            window_length = r - l + 1
            max_len = max(max_len, window_length)
            
        return max_len