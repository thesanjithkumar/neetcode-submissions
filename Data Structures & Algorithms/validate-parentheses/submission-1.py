class Solution:
    def isValid(self, s: str) -> bool:
        # A list that we will use as our stack
        stack = []
        
        # Dictionary mapping closing brackets to their matching opening brackets
        bracket_map = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Get the top element of the stack if it exists, otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the popped bracket doesn't match the correct opening bracket, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets matched perfectly! (Returns True)
        # If there are still brackets left in the stack, it's invalid. (Returns False)
        return not stack
