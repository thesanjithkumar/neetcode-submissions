class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""

        # Dictionaries to keep track of counts
        countT, window = {}, {}
        
        # 1. Build the shopping list
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        # Variables to track our progress
        have = 0
        need = len(countT) # Number of UNIQUE characters we need
        
        # To store the start and end index of the smallest valid window
        res = [-1, -1] 
        resLen = float("infinity")
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            # If this character is on our list, and we just hit the exact count we need
            if char in countT and window[char] == countT[char]:
                have += 1

            # While our window is valid, try to shrink it from the left!
            while have == need:
                # Is this the smallest window we've seen so far? Save it!
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                # Now, let's remove the left character to shrink the window
                left_char = s[l]
                window[left_char] -= 1
                
                # If removing that character dropped us below what we need, the window is invalid!
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                    
                # Physically slide the left edge forward
                l += 1

        # Extract the start and end indices of our best window
        left_index, right_index = res
        
        # If resLen is still infinity, we never found a valid window. Return "".
        # Otherwise, slice the string to get the answer. (Remember right_index + 1 because Python slicing is exclusive)
        return s[left_index : right_index + 1] if resLen != float("infinity") else ""
