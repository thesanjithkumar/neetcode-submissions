
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = [a.lower() for a in s if re.match("[A-Za-z0-9]", a)]
        if sl == sl[::-1]:
            return True
        return False