class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i,j = 0,0
        l1,l2= len(word1),len(word2)

        while i<l1 and j<l2:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])

        return ''.join(res)
            