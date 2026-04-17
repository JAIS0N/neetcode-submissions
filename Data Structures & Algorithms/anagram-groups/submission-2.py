class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for st in strs:
            count=[0]*26
            for ch in st:
                count[ord(ch)-ord('a')]+=1
            key=tuple(count)
            if key not in group:
                group[key]=[]
            group[key].append(st)
        return list(group.values())
