class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_maz = dict()
        for s in magazine:
            dict_maz[s] = dict_maz.get(s, 0) + 1
        for s in ransomNote:
            if s not in dict_maz:
                return False
            if dict_maz[s] == 0:
                return False
            dict_maz[s] -= 1
            
        return True
        