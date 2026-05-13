class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        #iterate, add to stack
        #while stack and stack[-1][0] < t
            #continously pop and inset into result at corr index
        #add val
        #after that return results

        stack = []
        result = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp,index = stack.pop()
                result[index] = i - index
            stack.append((t,i))
        
        return result
        