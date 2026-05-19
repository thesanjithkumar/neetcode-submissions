
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_string = ''.join(c for c in s if c.isalnum()).lower()
        return alnum_string == alnum_string[::-1]