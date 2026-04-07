class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        #iterate through string using l,r index
        #if (most frequent letter + k >= r-l+1):
            #while most frequent letter + k >= r-l+1:
                #hashMap[x] -= 1
                #l += 1
                #frequent = max(hashMap.values())
            #
        hashMap = defaultdict(int)
        l = 0
        freq = 0
        output = 0
        for r in range(len(s)):
            hashMap[s[r]] += 1
            freq = max(freq, hashMap[s[r]])

            while freq+k < r-l+1:
                hashMap[s[l]] -= 1
                l += 1
                freq = max(hashMap.values())
            output = max(r-l+1, output)
        return output


            
            
        