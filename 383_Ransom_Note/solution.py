class Solution:
    def canConstruct(self, ransomNote, magazine):
        count = [0] * 26
        
        for c in magazine:
            count[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            idx = ord(c) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1
        
        return True