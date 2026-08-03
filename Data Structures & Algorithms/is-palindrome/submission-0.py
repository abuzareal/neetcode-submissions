class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = "".join(c for c in s if c.isalnum()).lower()
        i, j = 0, len(ch) - 1
        while i < j:
            if ch[i] != ch[j]:
                return False
            i += 1
            j -= 1
        return True