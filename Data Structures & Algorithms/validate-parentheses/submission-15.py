class Solution:
    def isValid(self, s: str) -> bool:
        braces = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in braces:
                top = stack.pop() if stack else "&"

                if top != braces[i]:
                    return False

            else:
                stack.append(i)

        return not stack