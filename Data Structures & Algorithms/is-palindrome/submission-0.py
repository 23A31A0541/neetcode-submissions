import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = re.sub(r'[^a-zA-Z0-9]',"",s.lower())
        return rev==rev[::-1]