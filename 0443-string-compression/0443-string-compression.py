class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            curr_char = chars[read]
            count = 0

            # count consecutive occurrences of the current character
            while read < n and chars[read] == curr_char:
                read += 1
                count += 1 
            
            # write the character
            chars[write] = curr_char
            write += 1

            # write the count if the greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write