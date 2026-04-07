class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #two string, s1 and s2
        #need to figure out of perm of s1 is substring in s2
        #you can use a dictionary
        #if you know s1 is 3 characters long
            #make sliding window
            #turn that portion into a dictionary
            #if ==, return True
        #return False
        
        s1dict = {}
        for letter in s1:
            s1dict[letter] = s1dict.get(letter,0) + 1
        
        for index in range(len(s2)-len(s1)+1): #5
            s2dict = {}
            array = s2[index:len(s1)+index]
            for letter in array:
                s2dict[letter] = s2dict.get(letter,0) + 1
            if s2dict == s1dict:
                return True
        return False

        