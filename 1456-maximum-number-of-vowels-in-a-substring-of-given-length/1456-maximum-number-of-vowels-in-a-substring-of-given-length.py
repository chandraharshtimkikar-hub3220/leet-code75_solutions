class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}

        current_vowels = sum(1 for ch in s[:k] if ch in vowels)
        max_vowels = current_vowels

        if max_vowels == k:
            return k 

        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1

            if s[i - k] in vowels:
                current_vowels -= 1

            if current_vowels > max_vowels:
                max_vowels = current_vowels
                if max_vowels == k:
                    return k

        return max_vowels 
        