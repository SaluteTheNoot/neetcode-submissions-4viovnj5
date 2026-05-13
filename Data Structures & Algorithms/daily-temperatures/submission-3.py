class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #array of integers temp, temp[i] is temp on ith day
        #return array where result[i] is
            #number of days after ith day until warmer day
            #if no day in future set as zero
        #return array

        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp,index = stack.pop()
                res[index] = i-index
                
                
            stack.append((t,i))
        

        return res