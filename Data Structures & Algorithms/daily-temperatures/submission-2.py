class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #have an array of numbers
        #must output an array
            #the number of indexes away a larger number from ith index
        #you can do this by making a stack
            #when a new temp is added, you pop all number less than number
            #somehow find a way to chain index to temperature
                #if use 2d array
                    #array
        output = [0] * len(temperatures)
            #output[index] = new_index-index
        #return output
        tempStack = []
        for index,temp in enumerate(temperatures):
            while tempStack and temp > tempStack[-1][0]:
                temperature, tempIndex = tempStack.pop()
                output[tempIndex] = index - tempIndex
            tempStack.append((temp,index))
        return output


