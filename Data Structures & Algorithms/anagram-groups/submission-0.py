class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            origin = s
            s = list(s)
            s.sort()
            k = ''.join(s)
            m.setdefault(k,[]).append(origin)
        res = []
        for x,y in m.items():
            res.append(y)
        return res
