class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #array of strings with words
        #find longest common prefix between strings
        #if none, return empty ""

        #lets start with any time complexity
        #find shortest word, put that as cap
        length_cap = 201
        for string in strs:
            length_cap = min(len(string),length_cap)
        
        #iterate through each word seeing if they match and if not, return length_track
        length_track = 0

        condition = True
        while condition:
            if length_track == length_cap:
                break
            
            letter = strs[0][length_track]
            
            for string in strs:
                if string[length_track] != letter:
                    condition = False
            if not condition:
                break

            length_track += 1
        
        if length_track == 0:
            return ""
        else:
            return strs[0][:length_track]

