class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp = []   

        for i,t in enumerate(temperatures):
            while temp and t > temp[-1][0]:
                temperature,index = temp.pop()
                res[index] = i-index
            
            temp.append((t,i))
        return res

        