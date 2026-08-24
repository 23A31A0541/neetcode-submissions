class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case
        if len(s1)> len(s2):
            return False

        count1 = [0]*26
        count2 = [0]*26

        for s in s1:
            count1[ord(s)-ord('a')] += 1

        for i in range(len(s1)):
            count2[ord(s2[i])-ord('a')] += 1
        
        if count1 == count2:
            return True
        
        l = 0

        for r in range(len(s1),len(s2)):
            # expanding window
            count2[ord(s2[r])-ord('a')] += 1
            # shrinking window
            count2[ord(s2[l])-ord('a')] -= 1
            l += 1
            if count1== count2:
                return True

        return False
