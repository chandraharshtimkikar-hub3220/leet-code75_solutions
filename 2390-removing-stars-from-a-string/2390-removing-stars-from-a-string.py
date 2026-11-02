class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for c in s:
            ans.pop() if c == "*" else ans.append(c)
        return "".join(ans)
        