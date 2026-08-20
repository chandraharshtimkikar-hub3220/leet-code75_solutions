class Solution:
    def reverseWords(self, s: str) -> str:
        # s.split() automatically splits by whitespace and ignores consecutive spaces
        return " ".join(s.split()[::-1])        