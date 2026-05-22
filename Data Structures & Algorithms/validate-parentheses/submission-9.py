class Solution:
    def isValid(self, s: str) -> bool:
        braces = {')': '(', ']': '[', '}': '{'}
        s = []

        for i in s:
            if i in braces:
                top = s.pop() if s else "#"

                if top != braces[i]:
                    return False

            s.append(i)

        return not s

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