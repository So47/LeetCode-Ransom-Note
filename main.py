class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        skippedChars = {}
        for char in ransomNote:
            if char not in magazine:
                return False
            elif char in skippedChars:
                char_count_in_skipped_chars = skippedChars[char]
                if char_count_in_skipped_chars > 1:
                    skippedChars[char] = char_count_in_skipped_chars - 1
                else:
                    return False    

            else:    
                char_count = magazine.count(char)
                skippedChars[char] = char_count
        return True
