class Solution:
    def isValid(self, s: str) -> bool:
        braces = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            
            if i in braces:

                top_e = stack.pop() if stack else "#"

                if top_e != braces[i]:
                    return False

            else:
                stack.append(i)


        return not stack